"""
Name: vehicle_oop_final.py
Author: Rebecca Burwinkel
Date: May 5 2023
Purpose: FINAL: Programming for a vehicle using OOP
"""

##---------------------IMPORTS AND VARIABLES---------------------##
# Utils for plain title
import utils
# Rich for fancier titles
import rich
from rich.console import Console
from rich.panel import Panel
# Pygame for sounds
import pygame
from pygame import mixer
# Sleep for dramatic (or not so dramatic) pauses
from time import sleep
# Random for randomness
import random
# Import sys to aid in program ends
import sys

# Variable
crew_size = 0
ship_speed = 10

##------------------------------------MAIN------------------------------------##
# Define main to use class and its methods
def main():
    ship = Ship()

##------------------------------------CLASS-----------------------------------##
# Define class 
class Ship():
    # Def init
    def __init__(self):
    # Min 4 attributes 
        # Self._____
        self.music()
        self.titles()
        self.crew_size = 0
        self.scene()
        self.intro()
        self.actions(ship_speed, crew_size)

##----------------------------------ACTIONS-----------------------------------##
    # Min 4 methods
    def actions(self, ship_speed, crew_size):
        # Let user know they have choices to make
        print("A few choices await you. Do you wish to: ")
        
        while True:
            # User to be prompted on possible action to take
            # Determine next program action 
            # (map, compass, tossing someone, spyglass, exit)
            print("[A]djust speed, read the [M]ap, Check [C]ompass, [T]hrow someone overboard, [L]ook through spyglass. ")
            sleep(1)
            print("You may also return to port (E[X]it)")
            sleep(1)

            # User input
            action_choice = input("Make your choice. ")
            # Force lowercase for if/elifs
            action_choice = action_choice.lower()

            # Action choice = [A]djust speed
            if action_choice == "a":
                # Advise current speed
                print(f"The ship is going {ship_speed} knots.")
                # Give choices for change/maintain
                adjust_speed = input("Do you want to [P]ick up speed, [S]low, [M]aintain, or [D]rop the anchor? ")
                # lower for if/elif
                adjust_speed = adjust_speed.lower()
                
                # Speed up
                if adjust_speed == "p":
                    if ship_speed == 20:
                        print(f"You are going {ship_speed} and cannot go any faster.\n")
                    else:
                        ship_speed = ship_speed + 2
                        print(f"You have sped up to {ship_speed} knots.\n")
                    
                # Slow down
                elif adjust_speed == "s":
                    if ship_speed == 0:
                        print("You are stopped and cannot go slower.\n")
                    else:
                        ship_speed = ship_speed - 2
                        print(f"You are slowed to {ship_speed} knots.\n")

                # Keep pace
                elif adjust_speed == "m":
                    print(f"You hold your speed of {ship_speed} knots.\n")

                # Stop (anchor)
                elif adjust_speed == "d":
                    ship_speed == 0
                    print("You have stopped the ship. Are you wanting to sunbathe or what?")
                    raise_anchor = input("Do you want to raise the anchor? Y/N ")
                    raise_anchor = raise_anchor.lower()
                    if raise_anchor == "y":
                        print("You may continue on your journey.")
                    else:
                        print("Enjoy the sun!")
                        sys.exit()

                # Bogus
                else:
                    print("Please make a valid selection.")

            # Action choice: Check the [M]ap
            elif action_choice == "m":
                sleep(1.5)
                print("\nVYou pull out your map, taking note of your surroundings.") 
                print("You now have a better idea of where you are in your journey.")

            # Check [C]ompass
            elif action_choice == "c":
                sleep(1.5)
                # Choices for random
                directions = ["North", "South", "East", "West"]
                print("\nYou pull out your compass, and were able to verify your direction:", random.choice(directions))

            # [T]hrow someone overboard
            elif action_choice == "t":
                sleep(1.5)
                print("\nLooks like someone was messing off and was thrown overboard.")
                # Reduce reported crew size by one
                self.crew_size -= 1
                
                # Prints based on how many are left
                if crew_size == 1:
                    print(f"There is {self.crew_size} crew member left. They are watching you, rather nervously so.")                
                elif self.crew_size == 0:
                    print(f"You have {self.crew_size} crew members left. Return to port, you can't do this alone.")
                    sys.exit()
                else:
                    print(f"There are {self.crew_size} crew members left. Hopefully they learn from this example!")

            # [L]ook through spyglass
            elif action_choice == "l":
                # ENEMIES WILL BE SPOTTED!!!
                sleep(1.5)
                ship_side = ["Port", "Starboard", "Bow", "Stern"]
                print("\nEnemies!", random.choice(ship_side), "side! What will you do?")
                # New options reserved for the spotted foes!
                reaction_to_enemy = input(f"Do you [F]ire the cannon, [B]oard enemy ship, or [R]un away? ")
                # Lower for if/elif
                reaction_to_enemy = reaction_to_enemy.lower()

                # [F]ire the cannons
                if reaction_to_enemy == "f": 
                    sleep(1.5)   
                    print("\nThe cannon is fired! The enemy ship starts to sink!")

                # [B]oard enemy ship
                elif reaction_to_enemy == "b":
                    sleep(1.5)
                    print("\nYou have successfully boarded their ship.")
                    ship_action = input("Do you want to make someone walk the [P]lank, or do you [L]oot? ")
                    # Force lower for if/elif
                    ship_action = ship_action.lower()

                    # Make someone walk the [P]lank! 
                    if ship_action == "p":
                        sleep(1.5)
                        print("\nThe enemy begs for mercy, but are forced to walk regardless.")

                    # [L]oot and plunder
                    elif ship_action == "l":
                        sleep(1.5)
                        print("\nYou have found their treasure chest, their gold and gems now yours! ")

                # [R]un away (taunt as coward)
                elif reaction_to_enemy == "r":
                    sleep(1.5)
                    print("\nAll of the seas will know you are a coward! Have you thought of a new line of work?")
                    # End program
                    sys.exit()

            # Go to port (E[X]it)
            elif action_choice == "x":
                sleep(1.5)
                print("\nYou will safely arrive back to port soon. Safe travels! ")
                break

            # Bogus input
            else:
                print("Please make a valid selection.")
             
##---------------------------------INTRO/INPUT--------------------------------##
    def intro(self):
        # User input: Ask for name of the crew leader   
        leader = input("\"And what be your name?\"  ")
        # Small pause. Welcome them to the ship, as how many crew members
        sleep(1)
        print(f"\n\"Ye be welcome to the Jolly Roger, Cap'n {leader}!\"  " )

        # User input: Ask for crew size using utils to catch mistakes
        crew_size = utils.get_int("\"'ow many ye be bringing with?\"  " )
        sleep(1)

        # If zero crew
        if crew_size == 0:
            print("\"I thought they was just late! Ye can't be sailin' alone! Be gone!\"")
            # Do not let them continue, end program
            sys.exit()

        # For 1 crew
        elif crew_size == 1:
            print("\"Best be hopin' for no trouble. Too risky for me likin' but ye be Cap'n!\"")

        elif crew_size <= 5:
            print("\n\"That be a small crew. Better 'ope none be thrown overboard!\"" )

        # Pick on them for bringing too many
        elif crew_size >=15:
            print("\n\"Be careful matey! That there many an' ye might sink!\"" )

        else:
            print(f"\n\"I think that {crew_size} be sounding mighty fine!\"" )

        # User input: Ask for name of the first mate
        first_mate = input("\"And what be your First Mate's name?\"  " )
        print(f"\n\"Ye be welcome to the Jolly Roger too, {first_mate}!\"  " )

        # Scene setting / set-up for last user input
        print()
        sleep(3)
        print("As you are greeted to your ship, a descending shadow approaches from the north.")
        sleep(2)
        print("Before you have time to register the what, a large parrot lands on your shoulder.")
        sleep(2)
        print("A hearty laugh erupts from the man who looks to the bird with an even wider grin.\n ")
        sleep(2)

        # User input: Naming the new friend
        parrot = input("\"Looks such as yerself got a new mate! What be ye goin' to name 'im?\"  ")
        print(f"\"I think that {parrot} be a mighty fine name!\"")

        # Summary of all user input
        sleep(2)
        print()
        print(f"\"So Cap'n {leader}, let's get ye an' yer {crew_size} crew includin' {first_mate} out o' 'ere\"")
        sleep(1)
        print(f"\"An' {parrot} o'course too!\"")

        # Small pause. Ask if they want adventure or treasure, get user input
        sleep(1)
        print()
        quest = input(f"\"Tell me Captain {leader}, are ye seeking [A]dventure? Or [T]reasure!!!\"  ")
        # Force lower for if/elif
        quest = quest.lower()

        # Adventure
        if quest == "a":
            print("\"Findin' treasure been always me favorite, but I be not runnin' the ship.\"")
            sleep(1)
            print("\"If we be bein' technical though, findin' treasure be an adventure!\"")
            sleep(1.5)

        # Treasure
        elif quest == "t":
            print("\"Now that there sounds like a jolly time!\"")
            sleep(1)
            print("\"Maybe ye can brin' somethin' aft fer me?\"")
            sleep(1.5)

        # Some other answer
        else:
            print("\"Taking secrets to ye grave I see?\"")
            sleep(1)
            print("The man waves a dismissive hand to you before turning to walk off.")

        # Pause
        sleep(1.5)
        # Board ship, variation based on crew size
        # Average or large crew
        if crew_size > 5:
            print()
            sleep(1)
            print("Boarding the ship, you take a moment to survey the ship's supplies along with your crew.  ")
            sleep(2.5)
            print("Barking out orders, the crew moves into place, hoisting the anchor and unfurling the sails.")
        # Small crew
        elif crew_size > 1:
            print()
            sleep(1)
            print("Looking around after you board, you start to question your choice to take a small crew.")
            sleep(2.5)
            print("Barking out orders to your crew, they scramble to hoist the anchor and unfurl the sails.")
        else:
            print()
            sleep(1)
            print("It's a simple process to board, having only the two. Well... two and the parrot.")
            sleep(2.5)
            print(f"You look to {first_mate} and nod. Almost immediately you regret not bringing a crew.")
            sleep(2.5)
            print(f"You see the blur as {first_mate} tries to fill far too many shoes, running from station to station.")
       
        # Set the scene with small pauses in description
        sleep(2.5)
        print("\nThe ship slowly begins to move, the wind filling the sails and pushing the ship out to sea. ")
        sleep(2.5)
        print("Standing tall at the helm, your eyes scan the horizon as you watch for any signs of danger. \n")
        sleep(3)
        
        # Saving this for later
        self.crew_size = crew_size

##-------------------------------SCENE SETTING--------------------------------##
    def scene(self):
        # Scene setting
        sleep(1)
        print("A worn path takes you as far as it can before you transition to the planks of the long dock.")
        sleep(2.5)
        print("The rhythmic creaking of boards beneath your feet mixes with the sound of nearby waves.")
        sleep(2.5)
        print("Glancing out over the water you see your ship waiting, its sails billowing gently in the breeze. \n") 
        sleep(3)
        print("Your attention is quickly drawn back to just before the ship, right at the end of the dock.")
        sleep(2.5)
        print("A grizzled man with an eyepatch and a dirty and unkempt beard stood, leaned casually against a post.")
        sleep(2.5)
        print("Tattered clothes hang loose to his frame, and the scent of cheap booze quickly fills your nostrils.\n")
        sleep(2.5)
        print("You see his broken gaze is fixed on you, and he gives a lazy, yellow-toothed grin before speaking.")
        sleep(3)
        # Introductions 
        print("\"Ahoy there mate. Let me introduce meself. I be Edison 'Lazy Eye' Kaiser, keeper o' the port.\"")
        sleep(2.5)

##-----------------------------INTRO TITLE/GRAPHICS---------------------------##
    def titles(self):
        print()
        # Initialize the Rich console to make fancier title
        console = Console()

        # Fancier title from rich
        console.print(
            Panel.fit(
            "                  Voyages on the Jolly Roger:                   \n                      An Adventure at Sea",
            style="bold blue",
            subtitle="by Rebecca L. Burwinkel"))

        # Art credit: https://ascii.co.uk/art/skulls
        pirate_skull = """
                               ______
                            .-"      "-.
                           /            \ 
               _          |              |          _
              ( \         |,  .-.  .-.  ,|         / )
               > "=._     | )(__/  \__)( |     _.=" <
              (_/"=._"=._ |/     /\     \| _.="_.="\_)
                     "=._ (_     ^^     _)"_.="
                         "=\__|IIIIII|__/="
                        _.="| \IIIIII/ |"=._
              _     _.="_.="\          /"=._"=._     _
             ( \_.="_.="     `--------`     "=._"=._/ )
              > _.="                            "=._ <
             (_/   jgs                              \_) """
       
        print(pirate_skull)
        sleep(1)
        print()
        # Text title from utils
        print(utils.title("              Behave or ye 'ave to walk the plank!              "))
        print()

##-----------------------------------MUSIC------------------------------------##
    def music(self):
        # Sound things
        # Init sound mixer
        pygame.mixer.init()

        # Load audio file 
        # Sound credit: https://www.chosic.com/download-audio/27942/
        # Renamed for linking ease
        pygame.mixer.music.load('oceansound.mp3')

        # Set Preferred volume (0-1 scale, wanting quiet)
        pygame.mixer.music.set_volume(0.1)

        # Play the music (set for looping)
        pygame.mixer.music.play(15,0.0)

ship = Ship()
ship.crew_size()
"""
if __name__ == "__main__":
    main()"""
