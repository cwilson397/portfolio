###############################################
# Programmer Name: Colby Wilson
# week 01 prove: Favorite Color Hex code
# date: 4/24/2024
# purpose: to take a user input and output the color and corresponding hex code
###############################################

# defining main function
def main():
    # defines the color choices and hex code lists
    colors = ['red', 'yellow', 'blue', 'green', 'orange', 'purple', 'pink', 'brown', 'white', 'gray', 'cyan', 'magenta']
    hex_codes = ['#FF0000', '#FFFF00', '#0000FF', '#008000', '#FFA500', '#800080', '#FFC0CB', '#A52A2A', '#FFFFFF', '#808080', '#00FFFF', '#FF00FF']

    # instances a while true loop, so that if an invalid number is entered it will start the loop over
    while True:
        # outputs the favorite color list
        print("Please select your favorite color out of the following list: ")
        for i, color in enumerate(colors, start=1):
            print(f"{i}. {color}")

        # accepts the user's choice
        choice = int(input("Enter the number corresponding to your favorite color: "))
    
        # takes the choice and outputs the part of the arrays that are corresponding to the choice, will start the loop over if invalid choice is entered
        if 1 <= choice <= len(colors):
            favorite_color = colors[choice - 1]
            hex_code = hex_codes[choice - 1]
            print("You selected the color: ", favorite_color, " it has a hex code of : ", hex_code)
            break
        else:
            print("Invalid choice. Please select a number within the range.")

# calls the main function
main()