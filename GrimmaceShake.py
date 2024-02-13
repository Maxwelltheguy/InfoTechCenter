print("*********************************************************************************")
print("Gasoline Branch\n\n")

#import libraries here
import random

def gasLavelGauge():
    gasLevelList = ["Empty","Low","Quarter Tanks","Half Tank","Three Quarter Tank","Full Tank"]
    currentGasLevel = random.choice(gasLevelList)
    return currentGasLevel


print(gasLavelGauge())