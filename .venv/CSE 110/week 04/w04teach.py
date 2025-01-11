############################################
# Physics Calculator
# Colby Wilson
# 05/13/2024
#############################################

import math

# different functions

# skydiver
def skydiver():
    # user inputs
    mass = float(input("Enter the mass of the skydiver (in Kg): "))
    height = float(input("Enter the height of the skydiver (in meters): "))
    # calculates the cross sectional area
    cross_section = 0.7 * height # assumes based on the height
    time = float(input("Enter the time falling (in seconds): "))
    gravity = 9.8 # m/2^2 (Earth's gravity)
    fluid_density = 1.3 #  air density on earth
    drag_constant = (2 * fluid_density * cross_section)/ mass # calculates the drag constant

    # processing
    c = (drag_constant * fluid_density * cross_section) / (2 * mass)
    velocity = (mass * gravity /c) * (1 - math.exp(-c * time/mass))
   
    # output
    print(f"The Velocity of the skydiver after {time} seconds is: {round(velocity, 3)}, m/s")
         

def bowlingBall():
    # the user inputs
    mass = float(input("Enter the mass of the bowling ball (in kg): "))
    radius = float(input("Enter the radius of the bowling ball (in meters): "))
    time = float(input("Enter the time (in seconds): "))
    gravity = 9.8  # m/s^2 (Earth's gravity)
    fluid_density = 1.3  # air density on earth
    drag_constant = 0.5  # Drag constant for a sphere

    # processing
    cross_sectional_area = math.pi * (radius ** 2)
    c = drag_constant * (fluid_density * cross_sectional_area) / (2 * mass)
    velocity = (mass * gravity / c) * (1 - math.exp(-c * time / mass))

    # output
    print(f"The velocity of the bowling ball after {time} seconds is: {round(velocity, 3)} m/s")



def loaf_of_bread():
    # the user inputs
    mass = float(input("Enter the mass of the loaf of bread (in kg): "))
    radius = float(input("Enter the radius of the loaf of bread (in meters): "))
    time = float(input("Enter the time (in seconds): "))
    gravity = 9.8  # m/s^2 (Earth's gravity)
    fluid_density = 1.3  # air density on earth
    drag_constant = 1.1  # Drag constant for a cylinder 

    # processing
    cross_sectional_area = math.pi * (radius ** 2)
    c = drag_constant * (fluid_density * cross_sectional_area) / (2 * mass)
    velocity = (mass * gravity / c) * (1 - math.exp(-c * time / mass))
    
    # output
    print("The velocity of the loaf of bread after", time, "seconds is:", round(velocity, 3), "m/s")

def custom():
    # the user inputs to allow for completely custom calculations
    # object name
    object_name = str(input("Enter the name of the object: "))
    where = str(input("Enter where the object is moving falling: "))
    mass = float(input("Enter the mass of the object (in kg): "))
    time = float(input("Enter the time (in seconds): "))
    gravity = float(input("Enter the gravity (in m/2^2): "))
    fluid_density = float(input("Enter the density of the fluid (in kg/m^3) (assume air is a fluid): "))
    drag_constant = float(input("Enter the drag constat: "))
    rad = float(input("Enter the radius of the object: "))

    cross_section = math.pi * (rad ** 2)
    c = (drag_constant * (fluid_density * cross_section) / (2 * mass))
    velocity = ((mass * gravity) / c) * (1 - math.exp(-c * time/mass))

    print(f"The velocity of {object_name} after {time} seconds is: {round(velocity, 3)} m/s.")



def main():
    
    # menu item to run above functions or do a calculation based on custom numberws
    while True:
        print("==================================")
        print("Welcome to the physics calculator!")
        print("Please enter a selection from below. ")
        print("1.) Loaf of Bread.")
        print("2.) Bowling Ball. ")
        print("3.) Skydiver. ")
        print("4.) Custom. ")
        print("5.) quit")
        print("===================================")

        

        # choice
        choice = int(input("Enter your Selection: "))

        # menu, that makes it so only the ideal things are allowed.
        if choice == 1:
            loaf_of_bread()
        elif choice == 2:
            bowlingBall()
        elif choice == 3:
            skydiver()
        elif choice == 4:
            custom()
        elif choice == 5:
            print("Exiting Calculator!")
            break
        else:
            print("Invalid Selction please try again.")




main()