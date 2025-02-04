# Import necessary libraries
import sys
import time

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
              + LIGHT_GREEN + "Access Granted\n" + RESET)


