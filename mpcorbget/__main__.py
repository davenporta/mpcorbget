from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
from __future__ import with_statement
from builtins import input
import mpcorbget as mpc

def main():
    """Handy dandy quick ephemeris tool"""
    print("QuickEphem v1.1 | Code by Alex Davenport\n----------------------------------------------")
    asteroid = input("Asteroid Designation: ")
    observatory = input("Observatory Code: ")
    datetime = input("UTC (YYYY/MM/DD HH:MM:SS): ")
    ast = mpc.MPCORB(asteroid)
    observatory = mpc.Observatory(observatory)
    geo = ast.geocentric(datetime)
    topo = ast.topocentric(observatory.location, datetime)
    print("----------------------------------------------")
    print(geo)
    print()
    print(topo)

if __name__ == "__main__":
    main()
