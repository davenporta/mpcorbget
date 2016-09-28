import requests
import string
import ephem
from math import atan2, degrees

class MPCORB:
    """This class represents a minor planet contained within the IAU Minor Planet Center database.
    It retrieves the most recent data about the target from MPCORB.DAT.

    Arguments:
        obj (string) - unpacked minor planet designation
    """

    def __init__ (self, obj):
        """Attributes:
        obj - unpacked designation
        objdata - raw mpc data
        pdes - packed mpc designation
        rdes - readable name and designation of minor planet
        flags - (wip) raw hex data from mpc concerning minor planet class
        H - H mag
        G - slope parameter
        orbEl - dictionary of orbital elements with epoch
        xephem - mpc data in XEphem format
        target - pyephem EllipticalBody object
        """

        self.obj = obj
        self.objdata = self.getMPC()
        self.pdes = self.objdata[0:7].strip()
        self.rdes = self.objdata[166:194].strip()
        self.flags = self.objdata[161:165].strip()
        self.H = float(self.objdata[8:13].strip())
        self.G = float(self.objdata[14:19].strip())
        self.orbEl = {"epoch":self.dateUnpack(self.objdata[20:25].strip()),"ME":float(self.objdata[26:35].strip()),"w":float(self.objdata[37:46].strip()),"O":float(self.objdata[48:57].strip()),"i":float(self.objdata[59:68].strip()),"e":float(self.objdata[70:79].strip()),"a":float(self.objdata[92:103].strip()),"n":float(self.objdata[80:91].strip())}

        self.xephem = self.rdes + ",e," + str(self.orbEl["i"]) + "," + str(self.orbEl["O"]) + "," + str(self.orbEl["w"]) + "," + str(self.orbEl["a"]) + "," + str(self.orbEl["n"]) + "," + str(self.orbEl["e"]) + "," + str(self.orbEl["ME"]) + "," + self.orbEl["epoch"] + ",2000,H" + str(self.H) + "," + str(self.G)
        self.target = ephem.readdb(self.xephem)

    def getMPC(self):
        """returns line from MPCORB.DAT"""
        print("----------------------------------------------\nFetching MPCORB.DAT")
        mpcorb = requests.get("http://www.minorplanetcenter.net/iau/MPCORB/MPCORB.DAT", stream=True)
        asteroid = "(%s)" % self.obj
        for line in mpcorb.iter_lines(decode_unicode=True):
            if self.obj in line:
                mpcorb.close()
                print('SUCCESS')
                return line

    def getObs(self, code):
        """returns line from mpc observatory code list"""
        print("----------------------------------------------\nFetching Observatory Data")
        obslist = requests.get("http://www.minorplanetcenter.net/iau/lists/ObsCodes.html", stream=True)
        code = str(code).upper() + " "
        for line in obslist.iter_lines(decode_unicode=True):
            if code in line:
                obslist.close()
                print('SUCCESS')
                return line

    def dateUnpack(self, packed):
        """unpacks 5 character mpc date format into database format MM/DD/YYYY"""
        yearcode = {"I":"18","J":"19","K":"20"}
        daycode = "123456789ABCDEFGHIJKLMNOPQRSTUV"
        year = yearcode[packed[0]]+packed[1:3]
        month = daycode.index(packed[3])+1
        day = daycode.index(packed[4])+1
        return "%s/%s/%s" % (month, day, year)

    def geocentric(self, obstime):
        """returns geocentric coordinates of target given time
        Arguments:
        obstime - date in YYYY/MM/DD HH/MM/SS format
        """
        self.target.compute(obstime)
        return "RA: %s\nDec: %s" % (self.target.a_ra, self.target.a_dec)

    def topocentric(self, obs, obstime):
        """returns topocentric coordinates of target given observatory code and date
        Arguments:
        obs - 3-character IAU observatory code
        obstime - date in YYYY/MM/DD HH/MM/SS format
        """
        obsstring = self.getObs(obs)
        cosl = float(obsstring[13:21].strip())
        sinl = float(obsstring[21:29].strip())

        location = ephem.Observer()
        location.date = obstime
        location.lon = obsstring[4:13]
        location.lat = str(degrees(atan2(sinl,cosl)))
        location.elevation = 300
        self.target.compute(location)
        return "Alt: %s\nAz: %s" % (self.target.alt, self.target.az)

if __name__ == "__main__":
    print("QuickEphem v1.0 | Code by Alex Davenport\n----------------------------------------------")
    asteroid = input("Asteroid Designation: ")
    observatory = input("Observatory Code: ")
    datetime = input("UTC (YYYY/MM/DD HH:MM:SS): ")
    ast = MPCORB(asteroid)
    geo = ast.geocentric(datetime)
    topo = ast.topocentric(observatory, datetime)
    print("----------------------------------------------")
    print(geo)
    print()
    print(topo)
