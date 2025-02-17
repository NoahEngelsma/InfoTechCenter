print("\n***************************************\n")
print("Gasoline Branch - Developer: Noah Engelsma\n")

import random
from time import sleep

def gasLevelGauge():
  gasLevelList = ["Empty", "Low", "Quarter", "Half", "Three Quarter", "Full"]
  return random.choice(gasLevelList)

def gasStations():
        gasStationsList = ["Shell", "Marathon", "Speedway", "Circle K", "Wesco", "7/11", "Meijer", "Buc-ees"]
        return random.choice(gasStationsList)

def gasLevelAlert():
    milesToGasStationLow = round(random.uniform(1,25),1)
    milesToGasStationQuarterTank = round(random.uniform(25.1,50),1)
    gasLevelIndicator = gasLevelGauge()
    if gasLevelIndicator == "Empty":
        print("***WARNING YOU ARE OUT OF GAS***\n")
        sleep(1.25)
        print("Calling AAA")
    elif gasLevelIndicator == "Low":
        print("***WARNING YOU ARE LOW ON GAS CHECKING GPS FOR CLOSEST GAS STATION***\n")
        sleep(1.25)
        print("The closest Gas Station is", gasStations(), "which is", milesToGasStationLow, "miles away.\n")
    elif gasLevelIndicator == "Quarter":
        print("***WARNING YOU ARE ALMOST OUT OF GAS CHECKING FOR CLOSEST GAS STATION***\n")
        sleep(1.25)
        print("The closest Gas Station is", gasStations(), "which is", milesToGasStationQuarterTank, "miles away.\n")
    elif gasLevelIndicator == "Half Tank":
        print("***WARNING YOU ARE ON A HALF TANK OF GAS***\n")
    elif gasLevelIndicator == "Three Quarter Tank":
        print("***WARNING YOU ARE ON A THREE QUARTER TANK OF GAS***\n")
    else: print("***WARNING YOU HAVE A FULL TANK OF GAS*** Vroom Vroom!\n")

gasLevelAlert()
