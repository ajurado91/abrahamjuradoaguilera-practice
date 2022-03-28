from classes.land import Land
from classes.bicycle import Bicycle
from classes.car import Car

if __name__ == "__main__":

    bicycle = Bicycle('bicycle', 1000, True, False)
    car = Car('car', 120000, True, True)
    land = Land('land', 100000, True)

    transportList = [bicycle, car, land]

    for transport in transportList:
        transport.display_data()
