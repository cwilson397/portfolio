def main():
    colors = ['red', 'yellow', 'blue', 'green', 'orange', 'purple', 'pink', 'brown', 'white', 'gray', 'cyan', 'magenta']

    print("Please select your favorite color out of the following list: ")
    for i, color in enumerate(colors, start=1):
        print(f"{i}. {color}")