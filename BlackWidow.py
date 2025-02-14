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




print(gasLevelGauge())
print(gasStations())
