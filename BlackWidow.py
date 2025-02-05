print("\n***************************************************\n")

print("\tWeather Branch - Developer: Noah Engelsma")

#Import Libaries Here!
import random
from time import sleep
#Weather function to determine the weather
def weather():
    weatherForecastList = ["snowing", "blizzard", "icy", "rainy", "windy", "sunny"]
    weatherCondition = random.choice(weatherForecastList)
    return weatherCondition

print (weather())
