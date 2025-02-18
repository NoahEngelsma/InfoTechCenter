import random
from time import sleep
print("***********************************************\n")
print("Developer: Noah Engelsma")

def gas_level_gauge():
    return random.choice(["Empty", "Low", "Quarter", "Half", "Three Quarter", "Full"])


def gas_stations():
    return random.choice(["Shell", "Marathon", "Speedway", "Circle K", "Wesco", "7/11", "Meijer", "Buc-ees"])


def gas_level_alert():
    gas_level = gas_level_gauge()
    gas_messages = {
        "Empty": "***WARNING YOU ARE OUT OF GAS***\nCalling AAA...",
        "Low": "***WARNING YOU ARE LOW ON GAS CHECKING GPS FOR CLOSEST GAS STATION***\n",
        "Quarter": "***WARNING YOU ARE ALMOST OUT OF GAS CHECKING FOR CLOSEST GAS STATION***\n",
        "Half": "You are at half tank, consider refueling soon.",
        "Three Quarter": "You have a three-quarter tank of gas.",
        "Full": "***YOU HAVE A FULL TANK OF GAS*** Vroom Vroom!"
    }

    print(gas_messages[gas_level])

    if gas_level in ["Low", "Quarter"]:
        miles_to_station = round(random.uniform(1, 50) if gas_level == "Low" else random.uniform(25.1, 50), 1)
        print(f"The closest Gas Station is {gas_stations()}, which is {miles_to_station} miles away.\n")


gas_level_alert()