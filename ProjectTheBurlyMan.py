

"""
 Welcome Screen will start our program letting
drivers know that the InfoTech Center 2023 is loading
"""

# Import Libraries Here
import time
import sys
import random
from time import sleep


timetosleep = 2

print("\nWelcome - Infotech Center 2023\n")
time.sleep(timetosleep)

#Add code to have the ellipsis add a dot evey .5 seconds
x = 0
ellipsis= 0

while x != 20:
    x += 1
    message = ("InfoTech Center 2023 is loading..." + "." * ellipsis)
    ellipsis = ellipsis + 1
    sys.stdout.write("\r" + message) # \r prints a carriage return first, so, message is printed on top of the previous line
    time.sleep(0.5)
    if ellipsis == 4:
        ellipsis = 0
    if x == 20:
        print("\n\nOperating System Loaded - Brain Data Chip Scanned - Access Granted")


print("\n******************************************\n")
print("Checking Current Gasoline Levels\n")

sleep(1.5)

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

print("\n**************************************************\n")

print("Weather Branch\n")

#Create a function randomly choosing the weather from a list
def weather():
    weatherForcast = ["Snowing","Blizzard","Thunder","Rain","Cloudy","Clear","Windy"]
    weatherCondition = random.choice(weatherForcast)
    return weatherCondition

# Variable to call weather() once in our Vehicle Response System - VRS
weatherAlert = weather()

# VRS() will allow my vehicle to respond based on weather conditions
def vehicleResponseSystem():
    if weatherAlert == "Snowing":
        print("\nNational Weather Service has updated your alarm by 30 minutes because of the forcast of",weatherAlert)
        print("Vehicle Response System has been engaged only allowing you to drive 60 MPH.")
    elif weatherAlert == "Blizzard":
        print("\nNational Weather Service has updated your alarm by 50 minutes because of the forcast of", weatherAlert)
        print("Vehicle Response System has been engaged only allowing you to drive 40 MPH.")
    elif weatherAlert == "Thunder":
        print("\nNational Weather Service has updated your alarm by 40 minutes because of the forcast of", weatherAlert)
        print("Vehicle Response System has been engaged only allowing you to drive 45 MPH.")
    elif weatherAlert == "Rain":
        print("\nNational Weather Service has updated your alarm by 35 minutes because of the forcast of", weatherAlert)
        print("Vehicle Response System has been engaged only allowing you to drive 50 MPH.")
    elif weatherAlert == "Cloudy":
        print("\nThe weather forcast is calling for a", weatherAlert, "day, Enjoy your drive!")
    elif weatherAlert == "clear":
        print("\nThe weather forcast is calling for a", weatherAlert, "day, Enjoy your drive with the blue sky!")
    else:
        print("\nThe weather forcast is calling for a", weatherAlert, "day, Enjoy your drive with the wind in the air!")

vehicleResponseSystem()

