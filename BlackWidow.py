# Print a decorative line for better output formatting
print("\n***************************************************\n")

# Display program title and developer name
print("Weather Branch - Developer: Noah Engelsma\n")

# Import necessary libraries
import random  # Used to randomly select weather conditions
from time import sleep  # (Not used in this program but could be for delays)
# Function to randomly determine the weather condition
def weather():
    # List of possible weather conditions
    weatherForecastList = ["snowing", "blizzard", "icy", "rainy", "windy", "sunny"]
    # Randomly select a weather condition from the list
    weatherCondition = random.choice(weatherForecastList)
    return weatherCondition  # Return the selected weather condition
# Call the weather function to get the current weather alert
weatherAlert = weather()
# Function to determine the vehicle response based on the weather condition
def vehicleResponseSystem():
    if weatherAlert == "snowing":
        print("The National Weather Service has updated your alarm by 30 minutes because"
        " it is", weatherAlert, "outside.")
        sleep(1)
        print("VRS has been engaged only allowing us to drive 55MPH.")
    elif weatherAlert == "blizzard":
        print("The National Weather Service has updated your alarm by 60 minutes because"
        " it is a", weatherAlert, "outside!")
        sleep(1)
        print("VRS has been engaged only allowing us to drive 45MPH.")
    elif weatherAlert == "icy":
        print("The National Weather Service has updated your alarm by 90 minutes because"
        " it is", weatherAlert, "outside!")
        sleep(1)
        print("VRS has been engaged only allowing us to drive 35MPH.")
    elif weatherAlert == "rainy":
        print("The National Weather Service has updated your alarm by 10 minutes because"
        " it is", weatherAlert, "outside!")
        sleep(1)
        print("VRS has been engaged only allowing us to drive 65MPH.")
    elif weatherAlert == "windy":
        print("The National Weather Service has updated your alarm by 5 minutes because"
        " it is", weatherAlert, "outside!")
        sleep(1)
        print("VRS has been engaged only allowing us to drive 70MPH.")
    else:
        print("The National Weather Service is calling"
        " for", weatherAlert, "skies. Have a good day!")
        sleep(1)
        print("VRS has been disengaged")

# Call the vehicleResponseSystem function to display the alert message
vehicleResponseSystem()
# Print a closing decorative line for better output formatting
print("\n***************************************************\n")