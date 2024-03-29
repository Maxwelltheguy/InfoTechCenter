


#Import Libraries Here
import time
import sys
import random
from time import sleep

#Welcome Branch Starts here
timeToSleep = 2

print("\n\nWelcome to InfoTech Center V1.0\n")
time.sleep(timeToSleep)

#Code to have an ellipsis add a dot every .5 seconds
x = 0
ellipsis = 0

while x != 20:
    x += 1
    message = ("InfoTech Center Operating System Loading" + "." * ellipsis)
    ellipsis += 1
    sys.stdout.write("\r" + message) #\r prints a carriadge return first
    time.sleep(.5)
    if ellipsis == 4:
        ellipsis = 0
    if x == 20:
        print("\n\nOperating System Booted Up - Retina Scanned - Access Granted!\n")


#Gasoline branch starts here
print("*********************************************************************************")
print("Gasoline Branch\n\n")

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


print("\n*********************************************************************************")

print("Weather Branch\n")

#Create a function that randomly chooses the weather from a list
def weather():
    weatherForcast = ["snowy", "blizzard", "rainy", "foggy", "windy", "icy", "sunny", ]
    weatherConditions = random.choice(weatherForcast)
    return weatherConditions

#Varialble to call the weather() function once VRS(Vehicle Response System) is determined
weatherAlert = weather()

def vehicleResponseSystem():
    if weatherAlert == "snowy":
        print("\nNational Weather Service has updated our alarm by 30 minutes because of the forecast of",weatherAlert,
              "weather conditions")
        sleep(1.5)
        print("VRS has been only allowing you to drive 50mph.")
    elif weatherAlert == "blizzard":
        print("\nNational Weather Service has updated our alarm by 45 minutes because of the forecast of", weatherAlert,
              "weather conditions")
        sleep(1.5)
        print("VRS has been only allowing you to drive 40mph.")
    elif weatherAlert == "rainy":
        print("\nNational Weather Service has updated our alarm by 10 minutes because of the forecast of", weatherAlert,
              "weather conditions")
        sleep(1.5)
        print("VRS has been only allowing you to drive 60mph.")
    elif weatherAlert == "foggy":
        print("\nNational Weather Service has updated our alarm by 15 minutes because of the forecast of", weatherAlert,
              "weather conditions")
        sleep(1.5)
        print("VRS has been only allowing you to drive 55mph.")
    elif weatherAlert == "icy":
        print("\nNational Weather Service has updated our alarm by 60 minutes because of the forecast of", weatherAlert,
              "weather conditions")
        sleep(1.5)
        print("VRS has been only allowing you to drive 30mph.")
    elif weatherAlert == "windy":
        print("\nNational Weather Service has updated our alarm by 5 minutes because of the forecast of", weatherAlert,
              "weather conditions")
        sleep(1.5)
        print("VRS has been only allowing you to drive 70mph.")
    else:
        print("\nYou do not need to worry about weather, it is a", weatherAlert,"day out today")
        sleep(1.5)
        print("VRS has been disengaged")


vehicleResponseSystem()

