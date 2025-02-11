import random  # For random weather selection
from time import sleep  # For potential delays


# Print a decorative line for better output formatting
def print_separator():
    print("\n" + "*" * 51 + "\n")


# Display program title and developer name
def display_title():
    print("Weather Branch - Developer: Noah Engelsma\n")


# Function to randomly determine the weather condition
def get_weather():
    return random.choice(["snowing", "blizzard", "icy", "rainy", "windy", "sunny"])


# Function to determine the vehicle response based on the weather condition
def vehicle_response_system(weather_alert):
    responses = {
        "snowing": (30, 55),
        "blizzard": (60, 45),
        "icy": (90, 35),
        "rainy": (10, 65),
        "windy": (5, 70),
    }

    if weather_alert in responses:
        delay, speed = responses[weather_alert]
        print(
            f"The National Weather Service has updated your alarm by {delay} minutes because it is {weather_alert} outside.")
        sleep(1)
        print(f"VRS has been engaged only allowing us to drive {speed}MPH.")
    else:
        print(f"The National Weather Service is calling for {weather_alert} skies. Have a good day!")
        sleep(1)
        print("VRS has been disengaged.")


# Main program execution
if __name__ == "__main__":
    print_separator()
    display_title()
    weather_alert = get_weather()
    vehicle_response_system(weather_alert)
    print_separator()
