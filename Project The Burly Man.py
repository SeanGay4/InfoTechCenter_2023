print("******************************************")
print("Gasoline Branch\n")

# Import libraries here

import random
from time import sleep

# Function that lists Gas Stations, randomly choosing one, and Return its value

def gasLevelGauge():
    gasLevelList = ["Empty Tank" , "Low Tank" , "1/4 Tank" , "1/2 Tank" , "3/4 Tank" , "Full Tank"]
    currentGasLevel = random.choice (gasLevelList)
    return currentGasLevel

# Function will call the gasLevelGauge to determine gas level and find a close gas station if gas is low
def gasLevelAlert():
    milesToGasStationsLow = round(random.uniform(1,25),1)
    milesToGasStationsQuarterTank = round(random.uniform(25.1, 50), 1)
    