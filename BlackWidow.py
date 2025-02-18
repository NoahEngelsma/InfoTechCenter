import random
from time import sleep

# Display developer information
print("***********************************************\n")
print("Developer: Noah Engelsma\n")


# Function to randomly determine the current gas level
def gas_level_gauge():
    return random.choice(["Empty", "Low", "Quarter", "Half", "Three Quarter", "Full"])


# Function to randomly select a gas station name
def gas_stations():
    return random.choice(["Shell", "Marathon", "Speedway", "Circle K", "Wesco", "7/11", "Meijer", "Buc-ees"])


# Function to check gas level and provide an appropriate alert
def gas_level_alert():
    gas_level = gas_level_gauge()  # Get the current gas level

    # Dictionary mapping gas levels to alert messages
    gas_messages = {
        "Empty": "***WARNING YOU ARE OUT OF GAS*** Calling AAA...\n",
        "Low": "***WARNING YOU ARE LOW ON GAS CHECKING GPS FOR CLOSEST GAS STATION***\n",
        "Quarter": "***WARNING YOU ARE ALMOST OUT OF GAS CHECKING FOR CLOSEST GAS STATION***\n",
        "Half": "You are at half tank, consider refueling soon.\n",
        "Three Quarter": "You have a three-quarter tank of gas.\n",
        "Full": "***YOU HAVE A FULL TANK OF GAS*** Vroom Vroom!\n"
    }

    # Print the alert message based on gas level
    print(gas_messages[gas_level])

    # If gas level is Low or Quarter, provide information about the nearest gas station
    if gas_level in ["Low", "Quarter"]:
        # Generate a random distance to the nearest gas station based on gas level
        miles_to_station = round(random.uniform(1, 50) if gas_level == "Low" else random.uniform(25.1, 50), 1)
        print(f"The closest Gas Station is {gas_stations()}, which is {miles_to_station} miles away.\n")


# Call the function to execute the gas level alert system
gas_level_alert()
