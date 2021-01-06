# main.py
# Midnight Rider
# A text adventure game that is riveting.
# IGN gives it 4 stars out of 100.

import random
import sys
import textwrap
import time

INTRODUCTION = """
WELCOME TO MIDNIGHT RIDER
WE'VE STOLEN A CAR. WE NEED TO GET IT HOME.
THE CAR IS SPECIAL.
THE GOVERNMENT WANTS IT FOR THEIR GAIN.
WE CAN'T LET THAT HAPPEN.
ONE GOAL: SURVIVAL... and THE CAR.
REACH THE END BEFORE THE MAN GON GETCHU.
"""
CHOICES = """
    ----
    A. Eat a Tofu
    B. Travel at a moderate speed
    C. Speed ahead at full throttle
    D. Stop for fuel at a refuelling station (No food available)
    E. Status Check
    Q. QUIT
    ----
"""
def intro():
    for char in textwrap.dedent(INTRODUCTION):
        time.sleep(0.05)
        sys.stdout.write(char)
        sys.stdout.flush()
    time.sleep(1)
def main():
    intro()

    # CONSTANTS
    MAX_FUEL_LEVEL = 50
    MAX_TOFU_LEVEL = 3

    # Variables
    done = False
    km_travelled = 0           # 100 km is goal
    agents_distance = -20.0
    turns = 0                  # represents turns taken
    tofu = MAX_TOFU_LEVEL                   # how much tofu is left, 3 is max capacity
    fuel = MAX_FUEL_LEVEL                  # how much fuel is left, 50 is a full tank
    hunger = 0                 # hunger increases with number of turns


    while not done:
        # Check if reached END GAME
        if km_travelled = MAX_DISTANCE TRAVELLED:
            # WIN
            #
        # Give the player their choices
        print(CHOICES)
        # Handle user's input
        users_choice = input("What do you want to do? ").lower().strip("!,.? ")

        if users_choice == "a":
            # Eat
            if tofu > 0:
                tofu -= 2
                hunger = 0
                print()
                print("--------Mmmmm, soy bean goodness!")
                print("--------Your hunger is sated.")
                print(f"--------You have {tofu} remaining.")
                print()
            else:
                print()
                print("--------You have no tofu left, too bad, so sad.")
                print()

        elif users_choice == "b":
            # Drive at a moderate speed
            player_distance_now = random.randrange(6, 11)
            agents_distance_now = random.randrange(7, 15)

            # Burn fuel, less than option c
            fuel -= random.randrange(2, 7)

            # Player distance travelled
            km_travelled += player_distance_now

            # Agents distance travelled
            agents_distance -= (player_distance_now - agents_distance_now)

            # Give the user feedback
            print("")
            print(f"--------You sped ahead {player_distance_now} km!")
            if hunger >= 30:
                print("--------Your stomach is currently rumbling. Food is advised.")
            print("")

        elif users_choice == "c":
            # Drive fast
            player_distance_now = random.randrange(10, 16)
            agents_distance_now = random.randrange(7, 15)

            # Burn more fuel than option b
            fuel -= random.randrange(5, 11)

            # Player distance travelled
            km_travelled += player_distance_now

            # Agents distance travelled
            agents_distance -= (player_distance_now - agents_distance_now)

            # Give the user feedback
            print("")
            print(f"--------You sped ahead {player_distance_now} km!")
            if hunger >= 30:
                print("--------Your stomach is currently rumbling. Food is advised.")
            print("")

        elif users_choice == "d":
            # Refuel
            # Fill the fuel tank
            fuel = MAX_FUEL_LEVEL

            # Consider the agents coming closer
            agents_distance += random.randrange(7, 15)

            # Give the user feedback
            print("")
            print("--------You filled the fuel tank.")
            print("--------The agents got closer...")
            if hunger >= 30:
                print("--------Your stomach is currently rumbling. Food is advised.")
            print("")
        elif users_choice == "e":
            print(f"\t---Status Check---")
            print(f"\tkm travelled {km_travelled} km")
            print(f"\tFuel left: {fuel}")
            print(f"\tAgents are {abs(agents_distance)} km behind you")
            print(f"\t You have {tofu} left")
            print("\t-----")
            time.sleep(1)
        elif users_choice == "q":
            done = True

        # Increase hunger
        if users_choice not in ["a", "e"]:
            hunger += random.randrange(5, 13)

        # TODO: Change the environment based on choice and RNG
    # Outroduction
    print("Thanks for playing! Please play again. =)")


if __name__ == '__main__':
    main()

