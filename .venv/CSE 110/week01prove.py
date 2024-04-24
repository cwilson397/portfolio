# defining main function
def main():
    #defines the color choices and hex code lists
    colors = ['red', 'yellow', 'blue', 'green', 'orange', 'purple', 'pink', 'brown', 'white', 'gray', 'cyan', 'magenta']
    hex_codes = ['#FF0000', '#FFFF00', '#0000FF', '#008000', '#FFA500', '#800080', '#FFC0CB', '#A52A2A', '#FFFFFF', '#808080', '#00FFFF', '#FF00FF']

    #instances a while true loop, so that if an invalid number is added
    while True:
        print("Please select your favorite color out of the following list: ")
        for i, color in enumerate(colors, start=1):
            print(f"{i}. {color}")

        choice = int(input("Enter the number corresponding to your favorite color: "))
    

        if 1 <= choice <= len(colors):
            favorite_color = colors[choice - 1]
            hex_code = hex_codes[choice - 1]
            print("You selected the color: ", favorite_color, " it has a hex code of : ", hex_code)
            break
        else:
            print("Invalid choice. Please select a number within the range.")

if __name__ == "__main__":
    main()