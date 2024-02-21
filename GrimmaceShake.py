print("*********************************************************************************")
print("Gasoline Branch\n\n")

#import libraries here
import random
from time import sleep

#Function that lists Gas Stations, randomly choosing one and returning it's value
def gasLavelGauge():
    gasLevelList = ["Empty","Low","Quarter Tank","Half Tank","Three Quarter Tank","Full Tank"]
    currentGasLevel = random.choice(gasLevelList)
    return currentGasLevel

#Function that lists Gas Stations, randomly choosing one and returning it's value
def listOfGasStations():
    gasStations = ["Shell","Speedway","Marathon","Circle K","Moble","Costco","Meijer","7Eleven"]
    gasStationsNearby = random.choice(gasStations)
    return  gasStationsNearby

#Function will call the gasLevelGauge to determin our gas level and then find a close gas station
# by calling the listOfGasStations if we are on Low or Quarter tank
def gasLevelAlert():
    milesToGasStationsLow = round(random.uniform(1,25),1)
    milesToGasStationsQuarterTank = round(random.uniform(25.1, 50),1)
    gasLavelIndicator = gasLavelGauge()
    if gasLavelIndicator == "Empty":
        print("***WARNING - YOU ARE ON EMPTY***")
        sleep(1.25)
        print("\n    ***Calling Triple AAA***")
    elif gasLavelIndicator == "Low":
        print("Your gas tank is extremely low, checking Google Maps for the closest gas station.")
        sleep(2.25)
        print("The closest gas station is",listOfGasStations(),"which is",milesToGasStationsLow,"miles away.")
    elif gasLavelIndicator == "Quarter Tank":
        print("Your gas tank is on a quarter tank, checking Google Maps for the closest gas station.")
        sleep(2.25)
        print("The closest gas station is ",listOfGasStations()," which is",milesToGasStationsQuarterTank," miles away.")
    elif gasLavelIndicator == "Half Tank":
        print("Your gas tank is halfway full wich is plenty to get to your destination")
    elif gasLavelIndicator == "Three Quarter":
        print("Your gas tank is at three quarter tank")
    else:print("Your gas tank full")
        


gasLevelAlert()

