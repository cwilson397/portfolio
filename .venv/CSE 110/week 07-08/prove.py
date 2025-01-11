###############################################################################
# Bordle
# Colby Wilson
# 06/03/2024
# A wordle inspired game created because I am bored lol
###############################################################################

import random
import time

# The random word generator
def word_Choice():
    # Randomly select a number between 1 and 10
    num = random.randint(1, 10)

    # Return a word based on the random number
    if num == 1:
        return "moroni"
    elif num == 2:
        return "branch"
    elif num == 3:
        return "loops"
    elif num == 4:
        return "building"
    elif num == 5:
        return "choice"
    elif num == 6:
        return "lemon"
    elif num == 7:
        return "mission"
    elif num == 8:
        return "piano"
    elif num == 9:
        return "computer"
    elif num == 10:
        return "hamster"

# Hint generation function
def generate_hint(secret_Word, guess):
    # Initialize an empty list to hold the hint characters
    hint = []

    # Loop through each character in the secret word
    for i in range(len(secret_Word)):
        if guess[i] == secret_Word[i]:
            # Append the uppercase letter if it matches the exact position
            hint.append(guess[i].upper())
            
        elif guess[i] in secret_Word:
            # Append the lowercase letter if it is in the word but not at the same position
            hint.append(guess[i].lower())

        else:
            # Append an underscore if the letter is not in the word
            hint.append('_')

    # Join the list into a string with spaces in between each character
    return ' '.join(hint)

def main():
    # Welcome message
    print("*****************************************************************")
    print("Welcome to Bordle, a play on wordle not limited to only 5 letters")
    print("*****************************************************************")

    # Initial prompt to start the game
    start_game = input("Start Game? (yes/no): ").strip().lower()

    if start_game != "yes":
        print("Exiting game...")
        time.sleep(2)
        return  # Exit the function if the user does not want to start the game

    play_Game = True

    while play_Game:
        # Get a random secret word
        secret_Word = word_Choice()
        guessed = False
        guess_count = 0
        # Initial hint with underscores
        hint = "_ " * len(secret_Word)
        print(f"\nYour hint is: {hint.strip()}")

        # Loop until the word is guessed
        while guessed == False:
            # Get the user's guess
            guess = input("What is your guess? ").strip().lower()
            
            # Check if the guess length matches the secret word length
            if len(guess) != len(secret_Word):
                print(f"Sorry, the guess must have the same number of letters as the secret word.")
                continue

            # Increment the guess count
            guess_count += 1

            # Check if the guess is correct
            if guess == secret_Word:
                print(f"Congratulations! You guessed it!")
                print(f"It took you {guess_count} guesses.")
                guessed = True
            else:
                # Generate and display the hint
                hint = generate_hint(secret_Word, guess)
                print(f"Your hint is: \n{hint}")

        # Ask if the user wants to play again
        play_Again = input("Would you like to play again (yes/no): ").strip().lower()
        if play_Again != "yes":
            # Exit the game if the user does not want to play again
            print("Exiting game...")
            time.sleep(2)
            play_Game = False

# Run the main function
main()