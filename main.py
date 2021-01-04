# main.py
# Midnight Rider
# A text adventure game that is riveting.
# IGN gives it 4 stars out of 100.
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

    # Variables
    done = False
    km_travelled = 0           # 100 km is goal
    agents_distance = -20.0
    turns = 0                  # represents turns taken
    tofu = 3                   # how much tofu is left, 3 is max capacity
    fuel = 50                  # how much fuel is left, 50 is a full tank
    hunger = 0                 # hunger increases with number of turns


    while not done:
        # TODO: Check if reached END GAME
        # Give the player their choices
        print(CHOICES)
        # Handle user's input
        users_choice = input("What do you want to do? ").lower().strip("!,.? ")
        if users_choice == "e":
            print(f"\t---Status Check---")
            print(f"\tkm travelled {km_travelled} km")
            print(f"\tFuel left: {fuel}")
            print(f"\tAgents are {abs(agents_distance)} km behind you")
            print(f"\t You have {tofu} left")
            print("\t-----")
            time.sleep(1)
        elif users_choice == "q":
            done = True
        # TODO: Change the environment based on choice and RNG
    # OutroductionE
    print("Thanks for playing! Please play again. =)")


if __name__ == '__main__':
    main()

