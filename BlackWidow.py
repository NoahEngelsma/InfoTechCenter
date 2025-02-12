# Import necessary libraries
import sys
import time
import random  
from time import sleep 


# Define ANSI escape codes for colors
CYAN = "\033[96m"  # Light Cyan for the developer message
GREEN = "\033[92m"  # Green for system status messages
YELLOW = "\033[93m"  # Yellow for the loading animation
LIGHT_GREEN = "\033[92m"  # Bright Green for access confirmation
RESET = "\033[0m"  # Reset color to default after each message

# Display a welcome message with developer info in cyan
print(CYAN + "\nWelcome Branch - Developer: Noah Engelsma" + RESET)

# Display version information for the system in green
print(GREEN + "\nWelcome to InfoTechCenter V1.0\n" + RESET)

# Initialize variables
x = 0  # Counter to track the number of loop iterations
ellipsis = 0  # Controls the number of dots in the loading message animation

# Start the loop to simulate the system boot-up process
while x != 20:
    x += 1  # Increment the counter for each iteration
    
    # Create the loading message with an increasing number of dots
    message = (YELLOW + "Infotech Center System Booting" + "." * ellipsis + RESET)
    
    ellipsis += 1  # Increase the number of dots to simulate progress
    sys.stdout.write("\r" + message)  # Overwrite the previous message to create a loading effect
    sys.stdout.flush()  # Ensure the output updates properly
    time.sleep(0.5)  # Pause for half a second to simulate processing time
    
    # Reset the ellipsis counter after reaching 3 dots to repeat the cycle
    if ellipsis == 4:
        ellipsis = 0
    
    # Once the loop reaches 20 iterations, print the final success message
    if x == 20:
        print(GREEN + "\n\nOperating System Booted Up - Retina Scanned - " 
              + LIGHT_GREEN + "Access Granted" + RESET)




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
            f"The National Weather Service has updated your alarm by {delay} minutes because it is {weather_alert} outside.\n")
        sleep(1)
        print(f"VRS has been engaged only allowing us to drive {speed}MPH.")
    else:
        print(f"The National Weather Service is calling for {weather_alert} skies. Have a good day!")
        sleep(1)
        print("\nVRS has been disengaged.")

# Main program execution
if __name__ == "__main__":
    print_separator()
    display_title()
    weather_alert = get_weather()
    vehicle_response_system(weather_alert)
    print_separator()

