

        # Import necessary libraries
import sys
import time

# Display a welcome message with developer info
print("\nWelcome Branch - Developer: Noah Engelsma")

# Display version information for the system
print("\nWelcome to InfoTechCenter V1.0\n")

# Initialize variables
x = 0  # Counter to track the number of loop iterations
ellipsis = 0  # Variable to manage the number of dots in the loading message

# Start the loop to simulate the system boot-up
while x != 20:
    x += 1  # Increment the counter for each iteration
    message = ("Infotech Center System Booting" + "." * ellipsis)  # Create the loading message with increasing dots
    ellipsis += 1  # Increase the number of dots to simulate progress
    sys.stdout.write("\r" + message)  # Print the loading message, overwriting the previous one
    time.sleep(.5)  # Pause for half a second to simulate loading time
    
    # Reset the ellipsis counter after 3 dots for a repeating cycle
    if ellipsis == 4:
        ellipsis = 0
    
    # Once the loop reaches 20 iterations, print the success message
    if x == 20:
        print("\n\nOperating System Booted Up - Retina Scanned - Access Granted\n")
