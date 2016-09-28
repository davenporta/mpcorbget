import mpcorbget as mpc

def main():
    """Handy dandy quick ephemeris tool"""
    print("QuickEphem v1.0 | Code by Alex Davenport\n----------------------------------------------")
    asteroid = input("Asteroid Designation: ")
    observatory = input("Observatory Code: ")
    datetime = input("UTC (YYYY/MM/DD HH:MM:SS): ")
    ast = mpc.MPCORB(asteroid)
    geo = ast.geocentric(datetime)
    topo = ast.topocentric(observatory, datetime)
    print("----------------------------------------------")
    print(geo)
    print()
    print(topo)

if __name__ == "__main__":
    main()
