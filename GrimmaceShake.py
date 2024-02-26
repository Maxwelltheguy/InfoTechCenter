print("\n***********************************************************************************************************\n")

print("Weather Branch\n")

#Import Libraries Here
import random
from time import sleep

#Create a function that randomly chooses the weather from a list
def weather():
    weatherForcast = ["snowy", "blizzards", "rainy", "foggy", "windy", "icy", "sunny", ]
    weatherConditions = random.choice(weatherForcast)
    return weatherConditions

#Varialble to call the weather() function once VRS(Vehicle Response System) is determined
weatherAlert = weather()

def vehicleResponseSystem():
    if weatherAlert == "snowy":
        print("\nNational Weather Service has updated our alarm by 30 minutes because of the forecast of",weatherAlert,
              "weather conditions")
        print("VRS has been only allowing you to drive 50mph.")
    elif weatherAlert == "blizzard":
        print("\nNational Weather Service has updated our alarm by 45 minutes because of the forecast of", weatherAlert,
              "weather conditions")
        print("VRS has been only allowing you to drive 40mph.")
    elif weatherAlert == "rainy":
        print("\nNational Weather Service has updated our alarm by 10 minutes because of the forecast of", weatherAlert,
              "weather conditions")
        print("VRS has been only allowing you to drive 60mph.")


vehicleResponseSystem()