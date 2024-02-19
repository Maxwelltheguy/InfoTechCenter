print("*********************************************************************************")
print("Gasoline Branch\n\n")

#import libraries here
import random

#Function that lists Gas Stations, randomly choosing one and returning it's value
def gasLavelGauge():
    gasLevelList = ["Empty","Low","Quarter Tanks","Half Tank","Three Quarter Tank","Full Tank"]
    currentGasLevel = random.choice(gasLevelList)
    return currentGasLevel

#Function that lists Gas Stations, randomly choosing one and returning it's value
def listOfGasStations():
    gasStations = ["Shell","Speedway","Marathon","Circle K","Moble","Costco","Meijer","7Eleven"]
    gasStationsNearby = random.choice(gasStations)
    return  gasStationsNearby

print(gasLavelGauge())
print(listOfGasStations())