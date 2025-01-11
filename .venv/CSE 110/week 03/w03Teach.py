#####################################################
# Shape calculator
# Programmer: Colby 
# 05/08/2024
#####################################################
import math

# the square calculations
def square():

    # user input
    sLength = float(input("Enter the length of the side in the square: "))

    # process
    sPerim = float(sLength * 4)
    sArea = float(sLength * sLength)
    sVolume = float(sArea * sLength)


    # output
    print(f"---------------------")
    print(f"The Length is {sLength:.2f}, the permiter would be {sPerim:.2f}, the area for that square is {sArea:.2f}, the volume for the cube would be {sVolume:.2f}.")
    print(f"---------------------")

# the rectangle calcualtions, can handle square
def rectangle():

    # user input
    rLength = float(input("Enter the length: "))
    rWidth = float(input("Enter the width: "))
    rHeight = float(input("Enter the height: "))

    # process
    rPerim = float((rLength * 2) + (rWidth * 2))
    rArea = float(rLength * rWidth)
    rVolume = float(rArea * rHeight)

    # output
    print(f"---------------------")
    print(f"The Length is {rLength:.2f}, the permiter would be {rPerim:.2f}, the area for that rectangle is {rArea:.2f}, the volume for the prism would be {rVolume:.2f}.")
    print(f"---------------------")

# the circle calcutions
def circle():

    # user input
    cRad = float(input("Enter the radius: "))

    # process 
    cCirc = float(2 * math.pi * cRad)
    cArea = float(math.pi * cRad**2)
    cVolume = float((4/3) * math.pi * cRad**3)

    # output
    print(f"---------------------")
    print(f"The radius is {cRad:.2f}, the circumference would be {cCirc:.2f}, the area for that circle is {cArea:.2f}, the volume for the sphere would be {cVolume:.2f}.")
    print(f"---------------------")

def main():

    # Menu selection, runs the menu until the user quits
    while True:
        # The menu
        print("Welcome to the Shape Calculator, please select the shape you would like to calculate below.")
        print("Square: 1")
        print("Rectangle: 2")
        print("Circle: 3")
        print("Quit: 4")

        # The choice loop
        choice = int(input("Enter your selection: "))
        if choice == 1:
            square()
        elif choice == 2:
            rectangle()
        elif choice == 3:
            circle()
        elif choice == 4:
            break
        else:
            print("Invalid Selection, please enter a valid choice.")

main()