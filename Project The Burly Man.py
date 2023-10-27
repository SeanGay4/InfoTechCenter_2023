print("******************************************")
print("Gasoline Branch\n")

# Import libraries here

import random
from time import sleep

def gasLevelGauge():
    gasLevelList = ["Empty Tank" , "Low Tank" , "1/4 Tank" , "1/2 Tank" , "3/4 Tank" , "Full Tank"]
    currentGasLevel = random.choice (gasLevelList)
    return currentGasLevel



