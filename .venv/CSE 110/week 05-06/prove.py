#######################################################
# Programmer: Colby Wilson
# Program Date: 05/20/2024
# Description: A simple text adventure game. 
#######################################################

import os
import platform
import time

# clear the screen
def clear_terminal():
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')

# invalid choice function
def invalid():
    clear_terminal()
    print("Invalid choice please try again.")


def main():
    # all endings easter egg
    ending_counter = 0
    # initialization of the main loop
    
    while True:

        # introduction of the game
        print("Welcome to Murder Mystery at the STC!")
        start_Game = str.lower(input("Start Game? "))


        if start_Game == "no" or "n":
            print("I guess this mystery will need to be solved another time. :/")
            clear_terminal()
            break
        else:
            protagonist_gender = str.lower(input("Do you wish to play as a Male or Female? "))
            if protagonist_gender == "male":
                victum_gender = "female"
                victum_pro1 = "she"
                victum_pro2 = "her"
            else:
                victum_gender = "male"
                victum_pro1 = "he"
                victum_pro2 = "him"
                victum_pro3 = "his"
            print("We enter this mysterious world now...")
        
        solved = "False"
        roomSTC = "lobby1"
        while solved == "False":
            if roomSTC == "lobby1":
                # game start
                clear_terminal()
                print("====================================================================================================")
                print("You enter into the STC Lobby, a howling wind is blowing outside.")
                print("You are blinded by the harsh artificial light, when with a sudden clap of thunder, all lights go out")
                print("Before the lights can come back on you hear a blood-curtling scream. When the lights come on")
                print("You hear a click, and realize that the doors have been locked, unable to be unlocked.")
                print("You see a person laying at the foot of the stairs, a knife laying next to them in a pool of blood.")
                print("When you look around, you see a FLASHLIGHT sitting on a table, a KEY sticking out from underneath the stairs, and a ringing PHONE right next to you.")
                print("====================================================================================================")
                print()

                # setting key variables
                flashlight = False
                key = False
                phone = False
                l1Choice2 = "lobby"
                l1Choice = str.lower(input("What do you choose to investigate further? "))
                # choice tree pt2
                if l1Choice == "flashlight":
                    # clear terminal
                    clear_terminal()
                    print("====================================================================================================")
                    print("You walk over to the table...")
                    time.sleep(1) # delays for 2 seconds
                    print("Upon reaching the table, you see that not only is this a flashlight,")
                    print("it can also be used as a blacklight!") 
                    flashlight = True
                    print("You decide that its time to get a move on, after all the killer is locked in here with you.") 
                    print("Looking around you see a DOOR, an ELEVATOR, and a set of STAIRS")
                    print("====================================================================================================")
                    print()
                    
                    # second choice tree
                    while l1Choice2 == "lobby":
                        l1Choice2 = str.lower(input("Where do you decide to go?"))
                        
                        # second tree choice 1
                        if l1Choice2 == "door":
                            clear_terminal()
                            roomSTC = "door"
                            print("====================================================================================================")
                            print("As you walk over to the door the lights cut out again")
                            print("You turn on the flash light and see this text on the door")
                            print("Look under you")
                            print("====================================================================================================")
                            print()
                            dchoice = bool(input("Do you look down? "))
                            if dchoice == True:
                                clear_terminal()
                                print("===============================================================================")
                                print("You look down and suddenly you are greated by a hole where the floor used to be")
                                print("You start falling...")
                                time.sleep(7)
                                print("You are still falling...")
                                time.sleep(1)
                                print("It is starting to get hotter, when suddenly everything fades to black")
                                print("You the vr headset off, looking at your team...")
                                print('"Well how was it"')
                                print('"It was great, although we need to work on that falling sequence at the end, it was a little long"')
                                print('"Alright everyone back to the beginning lets see what happens next"')
                                print("====================================================================================================")
                                print()

                                clear_terminal()
                                solved = "true6"
                                print("You found the sixth ending, also known as the Murder Myster at the STC: The Game: The VR experience")
                                ending_counter = ending_counter+1
                            else:
                                print("====================================================================================================")
                                print("Out of the principal of the matter you refuse to look down, opening the door, you find the people filming this scene")
                                print("Your director yells at you for ruining the scene, 'Back to one!'")
                                print("====================================================================================================")

                                clear_terminal()
                                print("you found the seventh ending, otherwise known as the movie ending")
                                print("play again to find the other endings.")
                                solved = "true7"
                                ending_counter = ending_counter+1

                        # second tree choice 2
                        elif l1Choice2 == "elevator":
                            clear_terminal()
                            roomSTC = "elevator"
                            print("====================================================================================================")
                            print("You walk over the the elevator")
                            print("The doors open and you step inside")
                            print("Once the door closes the power goes out again")
                            print("You are trapped inside of the elevator")
                            print("====================================================================================================")
                            print()
                            
                            clear_terminal()
                            solved = "true8"
                            print("You have found the eigth ending, the stuck ending, play again to find the others")
                            ending_counter = ending_counter+1
                       
                        # second tree choice 3
                        elif l1Choice2 == "stairs":
                            clear_terminal()
                            roomSTC == "stairs"
                            
                            print("====================================================================================================")
                            print("Turning on the black light you see footprints leading to the stairs")
                            print("Following the footsteps you walk up the stairs")
                            print("At the top of the stairs you see two paths the footprints take")
                            print("One going LEFT and one going RIGHT")
                            print("====================================================================================================")

                            while True:
                                schoice = str.lower(input("Which way do you go? "))
                                if schoice == "left":
                                    print("====================================================================================================")
                                    print("following the footprints to the right, you are guided to the corner office.")
                                    print("It's the biggest office in the area")
                                    print("You try to open the door but it's locked, luckily it is thin enough that you can kick it down")
                                    time.sleep(1)
                                    print("After taking yourself a second to sike yourself up, you make a jumping kick to kick in the door")
                                    print("The door swings wildly open, flinging the door knob as you knocked that out of the door")
                                    print("The killer having his back turned, turns aroundly suddenly")
                                    print("He is greated by the flying doorknob knocking him out cold")
                                    print("You quickly react, grabbing the nearest thing to tie him up, luckily you were a scout")
                                    print("Tying him up you use a glove to pick up the knife he still has, carrying it away from him, dragging")
                                    print("Dragging the killer along with you, suddenly as you reach the bottom floor")
                                    print("There is a loud click, the police were able to disengange the lockdown")
                                    print(f"They take your statement, upon the choroner checking on the victum, turns out {victum_pro1} was alive this whole time")
                                    print(f"You had always had a bit of a crush on {victum_pro2}, so when she recovers and asks you out, you feel on top of the world")
                                    print("=======================================================================================================")
                                    print()

                                    clear_terminal()
                                    print("Epilogue")
                                    print("====================================================================================================")
                                    print(f"10 years down the line you and {victum_pro2} have lived happily ever after, having gotten married a year after the incident")
                                    print("having had 2 kids, with another on the way")
                                    print("From time to time, you still joke about how you guys got together, but you both have lived a happy life")
                                    print("The End")


                                    clear_terminal()
                                    print("You have found the First ending, otherwise known as the Canonical Ending")
                                    print("Play again to find the other endings.")
                                    solved = "true1"
                                    ending_counter = ending_counter+1
                                elif schoice == "right":
                                    clear_terminal()
                                    print("====================================================================================================")
                                    print("Turning right the footprints lead you towards the bathroom")
                                    print("Entering in you realize that there is no one there")
                                    print("The police storm the building and arrest you as the murderer")
                                    print("You are stuck in jail for the rest of your life, after a make believe trial")
                                    print("====================================================================================================")

                                    clear_terminal()
                                    print("You have found the prison ending play again to find the others")
                                    ending_counter = ending_counter+1

            
                                # fun invalid choice lol
                                else:
                                    clear_terminal()
                                    print("=========================================================================")
                                    print("You can't decide so you just stand there looking both ways, hoping for a clue")
                                    print("=========================================================================")
                        # second tree secret choice
                        elif l1Choice2 == "lobby":
                            clear_terminal()
                            print("====================================================================================================")
                            print("You decide to stay in the lobby, even though more people could be dying as you stand there")
                            print("====================================================================================================")
                            print()
                        # invalid choice tree
                        else: 
                            invalid
                # first choice tree part 2
                elif l1Choice == "key":
                    clear_terminal()
                    print("====================================================================================================")
                    print("You walk over to the key...")
                    time.sleep(1)
                    print("Upon reaching the key, you bend down to pick it up.")
                    print("It is a small simple thing, having a few ridges, a hole for a key ring, and a faded tag")
                    print("Looking closer you see it is too faded to read more than 2 numbers, a 4 and a 5")
                    print("You see a DOOR right behind the stairs, you also know there are a lot of rooms UPSTAIRS")
                    print("====================================================================================================")
                    print()

                    # choice loop
                    while l1Choice2 == "lobby":
                        l1Choice2 = str.lower(input("Where do you chose to go? "))
                        if l1Choice2 == "door":
                            clear_terminal()
                            roomSTC = "door2"
                            print("====================================================================================================")
                            print("You walk over to the door...")
                            print("As you get closer the key slowly gets heavier in your hand")
                            print("It starts to get so heavy you can barely carry it anymore")
                            print("Once you reach the door, it is so heavy that it takes all of your strength to put it into the door, and turn it")
                            print("It does turn, however once you open the door you are greated by a black hole")
                            print("Everything gets sucked in ending life as you know it")
                            print("====================================================================================================")
                            print()
                            solved = "true2"

                            clear_terminal()
                            print("You just found the, Black hole ending.")
                            print("Otherwise known as I had to come up with so many endings I threw this one in as a joke")
                            print("Play again to find the other endings")
                            ending_counter = ending_counter+1
                        
                        # key choice tree part 2
                        elif l1Choice2 == "upstairs":
                            clear_terminal()
                            roomSTC = "upstairs"
                            print("====================================================================================================")
                            print("You begin to walk up the stairs...")
                            time.sleep(3)
                            print("You reach the top of the stairs, finding the path to the right, where you remember all the classrooms being")
                            print("To be blocked off by Construction equipment, you walk to the left finding a door in front of you.")
                            print("You try to open the door but find it to be locked, luckily you have a KEY with you")
                            print("====================================================================================================")
                            print()
                            while True:
                                unlock = bool(input("Do you Unlock the door? "))
                                clear_terminal()
                                # third ending
                                if unlock == True:
                                    clear_terminal()
                                    print("====================================================================================================")
                                    print("You push the key into the keyhole, turning it gently you hear a click.")
                                    print("With a turn of the knob and a push the door gently opens..")
                                    print("You see someone covered in blood in the room, they are dead too, turns out it was a Murder/Suicide")
                                    print("Never being good with the sight of blood you run to the nearest bathroom, and end up throwing up")
                                    print("The doors are off lockdown now, and you call 911, to report the crime.")
                                    print("====================================================================================================")
                                    solved = "true3"

                                    clear_terminal()
                                    print("You found the third ending. The blood ending, please play again to find all the other endings")
                                    ending_counter = ending_counter+1
                                else:
                                    clear_terminal()
                                    print("====================================================================================================")
                                    print("You stand there paralyzed by indecision")
                                    time.sleep(5)
                                    print("You decide its finally time to make a decision")
                                    print("====================================================================================================")
                                    
                        # easter egg
                        elif l1Choice2 == "lobby":
                            clear_terminal()
                            print("====================================================================================================")
                            print("You decide to stay in the lobby, even though more people could be dying as you stand there")
                            print("====================================================================================================")
                            print()
                            roomSTC = "lobby"
                        # invalid stuff
                        else:
                            invalid
                            roomSTC = "lobby"

                # phone tree story, completed
                elif l1Choice == "phone":
                    # phone tree story
                    clear_terminal()
                    print("====================================================================================================")
                    print("You decide to check out that phone, as it is playing the world's most annoying song as it's ringtone.")
                    print("Upon picking the phone up you answer it...")
                    time.sleep(1)
                    print("You hear nothing on the other side, except for the faint buzz of some low consistent sound")
                    print("To you it kinda sounds like the kinda of thing you would hear when standing outside of an elevator mechanics room,")
                    print("or maybe even a server room")
                    print("You know the elevator mechanics are below you a floor, only accesible by the ELEVATOR from where you are,")
                    print("however there is a server room just up the STAIRS nearby")
                    print("====================================================================================================")
                    
                    while roomSTC == "lobby":
                        clear_terminal()
                        l1Choice2 = str.lower(input("Where do you choose to go? "))
                        # phone choice tree secret choice
                        if l1Choice2 == "lobby":
                            clear_terminal()
                            print("====================================================================================================")
                            print("You decide to stay in the lobby, even though more people could be dying as you stand there")
                            print("====================================================================================================")
                            print()
                            roomSTC = "lobby"
                        
                        # phone choice tree 1st choice
                        elif l1Choice2 == "stairs":
                            roomSTC = "stairs"
                            clear_terminal()
                            print("====================================================================================================")
                            print("You walk up the stairs...")
                            time.sleep(2)
                            print("You don't remember the stair being this long, but yet you keep on walking")
                            time.sleep(1)
                            print("When you finally reach the top of the stairs you're greated with a peculiar sight...")
                            print("You seem to remember there being a wide open mezzanine like area at the top of the stairs")
                            print("However now you are only greated by a singular door cracked open door")
                            print()
                            print("====================================================================================================")
                            print()
                            step_in = bool(input("Do you step in? y/n "))
                            while step_in == False:
                                clear_terminal()
                                step_in = bool(input("Do you step in? y/n "))
                                # easter egg for fun
                                if step_in == False:
                                    clear_terminal()
                                    print("===============================================")
                                    print("You stand there paralyzed by indecision.")
                                    time.sleep(5)
                                    print("You decide its finally time to make a decision.")
                                    print("===============================================")
                                
                                # ending 4
                                else:
                                    clear_terminal()
                                    print("====================================================================================================")
                                    print("You push the door open...")
                                    print("Finding it completely dark, there seems to be no one around")
                                    print("Feeling around the wall for the light switch, you find one and flip on the lights")
                                    print()
                                    print("Suddenly you feel a sharp pain in your back")
                                    print('You try to run way, but you fall down the stairs')
                                    print("Once at the bottom of the stairs, you look up, and see yourself stairing back at you")
                                    print("You see a bright light that seems to come forward and envelope you.")
                                    print("====================================================================================================")
                                    solved = "True4"

                                    print("You found the forth ending, the bad one, play again to find the rest.")
                                    ending_counter = ending_counter+1

                        # phone choice tree  2nd choice
                        elif l1Choice2 == "elevator":
                            clear_terminal()
                            
                            # sets loop variable
                            roomSTC = "elevator"
                            print("====================================================================================================")
                            print("You walk over to the elevator and press the button.")
                            time.sleep(2)
                            print("After it finally shows up you step in a press the button to go down a level")
                            time.sleep(3)
                            print("it finally reaches the bottom floor")
                            print("You step out a walk over to the mechanical room")
                            print("You find the door unlocked")
                            print("====================================================================================================")
                            print()
                            
                            while step_in == False:
                                clear_terminal()
                                step_in = bool(input("Do you step in? y/n "))
                                # easter egg for fun
                                if step_in == False:
                                    clear_terminal()
                                    print("===============================================")
                                    print("You stand there paralyzed by indecision.")
                                    time.sleep(5)
                                    print("You decide its finally time to make a decision.")
                                    print("===============================================")
                                
                                # ending 5
                                else:
                                 
                                    clear_terminal()
                                    print("====================================================================================================")
                                    print("You walk in to the room")
                                    print("Finding it completely dark, you find another ringing phone, this time sounding like your alarm")
                                    print("You answer the phone...")
                                    print()
                                    print("You see the light of your bedroom infront of you, your roommate having flipped on the light")
                                    print('They say: "come on dude! its time to get moving')
                                    print("You realize that it was all a dream which explains why you weren't able to read any of the many clocks around")
                                    print("====================================================================================================")
                                    solved = "True5"

                                    clear_terminal()
                                    print("You found the 5th ending, play again to find the rest")
                                    ending_counter = ending_counter+1
                           
                        else:
                            invalid

                # invalid stuff            
                else:
                    invalid
        
    # thanks for playing
   
    if ending_counter == 9:
        clear_terminal()
        print("You were able to go through and find all of the endings")
        print("Unfotunately this doesn't mean much, but I am truly grateful someone was able to see all of the different pathways I set in this thing")
        print("I may go through and create a more complicated version of this game some day, however for now, I hope you enjoyed this")
        print("By the way, coming up with so many different endings, and storylines as you saw was very hard")
        print("Good Bye.")
        print("Exiting program...")
        time.sleep(10)
        clear_terminal()
    else:
        clear_terminal()
        print("Thank you for playing")
        print("I hope you enjoyed your exprience here today")

main()