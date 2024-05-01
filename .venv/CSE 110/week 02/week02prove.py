######################################################
# Programmer Name: Colby Wilson
# week 01 prove: Mad Lib
# date: 4/30/2024
# purpose: take multiple user inputs and output
# it as part of a mad lib
#######################################################

# defining madlib generation function for a seperate one, I coded all of this before I saw that a mdalib was provided so I added that in as a seperate one that you can
# select from in order to not have wasted all that time
def generate_madLib1():
    # getting all inputs necessary for the madlib function
    adjective1 = str(input("Enter an adjective: "))
    adjective2 = str(input("Enter another adjective: "))
    typeBird1 = str(input("Enter a type of bird: "))
    roomHouse1 = str(input("Enter a room in the house: "))
    verbPt1 = str(input("Enter a verb in past tense: "))
    verb2 = str(input("Enter a verb: "))
    relativeName1 = str(input("Enter a relative's name(Ex: Dad/Grandma): "))
    noun1 = str(input("Enter a noun: "))
    liquid1 = str(input("Enter a liquid: "))
    verbIng1 = str(input("Enter a verb ending in -ing: "))
    partBody = str(input("Enter a part of the body(Plural): "))
    nounPl1 = str(input("Enter a plural Noun: "))
    verbIng2 = str(input("Enter another verb ending in -ing: "))
    noun2 = str(input("Enter another noun: "))

    # print/process
    print("It was a ", adjective1, " cold November day. I woke up to the ", adjective2, " smell")
    print("of ", typeBird1, " roasting in the ", roomHouse1, " downstairs. I ", verbPt1, " down the stairs")
    print("to see if I could help ", verb2, " the dinner. My mom said, 'See if ", relativeName1, " needs a fresh")
    print(noun1, "' So I carried a tray of glasses full of ", liquid1, " into the ", verbIng1, " room. When I got there,")
    print("I couldn't believe my ", partBody, "! There were ", nounPl1, " ", verbIng2, " on the ", noun2, "!")

# defining generate_madlib for the provided madlib
def generate_madlib2():
    # prompts the user for the needed variables
    adjective1 = str(input("Enter an adjective: "))
    adjective2 = str(input("Enter another adjective: "))
    animal1 = str(input("Enter an animal: "))
    verb1 = str(input("Enter a verb: "))
    exclamation = str(input("Enter an exclamation: "))
    verb2 = str(input("Enter another verb: "))
    verb3 = str(input("Enter one more verb: "))

    # Print/process the madlib
    print("The other day, I was really in trouble. It all started when I saw a very")
    print(adjective1,",", animal1, ",", verb1, "down the hallway. '", exclamation, "!' I yelled. But all")
    print("I could think to do was to", verb2, "over and over. Miraculously,")
    print("that caused it to stop, but not before it tried to", verb3, "\nright in front of my family.")



# defining main
def main():
    # selection menu
    while True:
        print("Welcome to the Mad lib generator. Please follow all instructions to make this as simple as possible.")
        print("1. Thanksgiving")
        print("2. Suprise")
        print("3. Exit")

        choice = input("Enter your selection 1/2/3: ")

        if choice == '1':
            generate_madLib1()
        elif choice == '2':
            generate_madlib2()
        elif choice == '3':
            print("Exiting Program...")
            break
        else:
            print("Invalid choice please try again")


main()