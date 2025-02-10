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
    elif weatherAlert == "icy":
        print("The National Weather Service has updated your alarm by 90 minutes because"
        " it is", weatherAlert, "outside!")
    elif weatherAlert == "rainy":
        print("The National Weather Service has updated your alarm by 10 minutes because"
        " it is", weatherAlert, "outside!")
    elif weatherAlert == "windy":
        print("The National Weather Service has updated your alarm by 5 minutes because"
        " it is", weatherAlert, "outside!")
    else:
        print("The National Weather Service is calling"
        " for", weatherAlert, "skys have a good day!")
    

vehicleResponseSystem()    