#########################################
# Wednesday January 15th, 2025
# Tire Volume Program
# Programmed by Colby Wilson
#########################################

import math
from datetime import datetime

# Main function
def main():
    # Prompt user for tire dimensions
    print("Tire Volume Calculator")
    width = float(input("Enter the width of the tire in mm (e.g., 205): "))
    aspect_ratio = float(input("Enter the aspect ratio of the tire (e.g., 60): "))
    diameter = float(input("Enter the diameter of the wheel in inches (e.g., 15): "))

    # Calculate the tire volume
    volume = (math.pi * width**2 * aspect_ratio * (width * aspect_ratio + 2540 * diameter)) / 10_000_000_000
    print(f"\nThe approximate volume of the tire is {volume:.2f} liters.")

    # Get current date
    current_date = datetime.now().strftime("%Y-%m-%d")

    # Append data to volumes.txt
    with open("volumes.txt", "a") as file:
        file.write(f"{current_date}, {width}, {aspect_ratio}, {diameter}, {volume:.2f}\n")

    print("Tire data has been saved to volumes.txt.")

# Run the program
main()
