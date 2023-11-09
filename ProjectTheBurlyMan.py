print("******************************************")
print("Gasoline Branch\n")

# Import libraries here

import random
from time import sleep

# Function that lists Gas Stations, randomly choosing one, and Return its value

def gasLevelGauge():
    gasLevelList = ["Empty Tank", "Low Tank", "1/4 Tank", "1/2 Tank", "3/4 Tank", "Full Tank"]
    currentGasLevel = random.choice(gasLevelList)
    return currentGasLevel

# Function with a list of Gas Stations

def listOfGasStations():
    gasStations = ["Shell", "Speedway", "Exxon", "Meijer", "Costco", "Marathon", "BP", "Circle K", "Wesco"]
    gasStationsNearby = random.choice(gasStations)
    return gasStationsNearby

# Function will call the gasLevelGauge to determine gas level and find a close gas station if gas is low
def gasLevelAlert():
    milesToGasStationsLow = round(random.uniform(1,25),1)
    milesToGasStationsQuarterTank = round(random.uniform(25.1, 50), 1)
    gasLevelIndicator = gasLevelGauge()
    if gasLevelIndicator == "Empty":
        print("***WARNING - YOU ARE ON EMPTY***")
        sleep(1.25)
        print("Calling Triple AAA")
    elif gasLevelIndicator == "Low Tank":
        print("Your gas tank is extremely low, checking Google Maps for the closest gas station.")
        sleep(1.5)
        print("The closest gas station is", listOfGasStations(), "which is", milesToGasStationsLow, "miles away.")
    elif gasLevelIndicator == " 1/4 Tank":
        print("You have a Quarter Tank of gasoline, checking Google Maps for the closest gas station.")
        sleep(1.5)
        print("The closest gas station is", listOfGasStations(), "which is", milesToGasStationsQuarterTank, "miles away.")
    elif gasLevelIndicator == "1/2 Tank":
        print("Your gas tank has a half of a tank which is plenty to get to your destinations.")
    elif gasLevelIndicator == "3/4 Tank":
        print("Your gas tank is at three quarter tank!")
    else:
        print("Your gas tank is full - Yeah! - Congratulations! - Vroom Vroom!")

gasLevelAlert()