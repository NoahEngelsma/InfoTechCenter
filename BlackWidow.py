print("\n***************************************************\n")

print("Weather Branch - Developer: Noah Engelsma\n")

#Import Libaries Here!
import random
from time import sleep

#Weather function to determine the weather
def weather():
    weatherForecastList = ["snowing", "blizzard", "icy", "rainy", "windy", "sunny"]
    weatherCondition = random.choice(weatherForecastList)
    return weatherCondition

weatherAlert = weather()

def vehicleResponseSystem():
    if weatherAlert == "snowing":
        print("The National Weather Service has updated your alarm by 30 minutes because"
        " it is", weatherAlert, "outside.")
    elif weatherAlert == "blizzard":
        print("The National Weather Service has updated your alarm by 60 minutes because"
        " it is a", weatherAlert, "outside!")

vehicleResponseSystem()    