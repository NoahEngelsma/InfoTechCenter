print("\n***************************************\n")
print("Gasoline Branch - Developer: Noah Engelsma\n")


import random
from time import sleep

def gasLevelGauge():
  gasLevelList = ["Empty", :"Low", "Quarter", "Half", "Three Quarter", "Full"]
  return random.choice(gasLevelList)
  
