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

WIN = """
You pressed the button to open the gate.
This isn't the first time you've done this,
so you know how to time it exactly.
Just as the doors close, you slide right into HQ.
You know you did the right thing, the government
would have just torn the car apart.
They don't know its secrets...
that it holds the key to different worlds.
As you step out of the vehicle, Fido runs up to you.
"Thank you for saving me," he says.
As you take a couple of steps away from the car,
it makes a strange sound.
It changes it shape.
You've seen it before, but only on TV.
"...Bumblebee???"
------ Game Over ------
"""

LOSE_HUNGER = """
YOUR STOMACH IS EMPTY.
Who knew that what the doctor said was true,
That human robot hybrids would need
Tofu to sustain themselves.
Your robot systems start to shut down.
Your human eyes close.
The last thing that you hear are sirens.
They GOTCHU. They got the car.
We failed...

------ Game Over------
"""

LOSE_AGENTS = """
THE AGENTS HAVE CLOSED IN ON YOU.
There are at least 20 cars surrounding you.
The lead car bumps your passenger side.
You manage to correct your steering
To keep you from crashing.

You didn't see the agents car beside you.
The driver bumps your car,
And that's it.

You spin out of control.
Your car flips over at least two times.
Or more... we lost count.

SIRENS

"Are they alive", someone asks.
Doesn't matter. All we wanted was the car.
You see a dog walking out of the car.
"Was it in the car the whole time?"
You think to yourself.

The dog looks up at the officers
"You will never stop the revolution."
"Did the dog just talk?" You think to yourself.

YOU DRIFT OFF INTO UNCONSCIOUSNESS.

------Game Over------
"""

"Lose"

LOSE_FUEL = """
Your car stopped suddenly.
The sirens are getting louder.
They GOTCHU. They got the car.
We failed...
------Game Over------
"""

CHOICES = """
    ----
    A. Eat some tofu.
    B. Continue ahead at a moderate speed.
    C. Speed ahead at full throttle.
    D. Stop for fuel at a refuelling station.
       (No food available)
    E. Status check
    Q. QUIT
    ----
"""


def type_text_output(text):
    for char in textwrap.dedent(text):
        time.sleep(0.05)
        sys.stdout.write(char)
        sys.stdout.flush()

    time.sleep(1)


def main():
    type_text_output(INTRODUCTION)

    # CONSTANTS
    MAX_FUEL_LEVEL = 40
    MAX_TOFU_LEVEL = 2
    MAX_DISTANCE_TRAVELED = 100
    TOFU_CHANCE = 0.03

    # Variables
    done = False

    km_traveled = 0
    agents_distance = -20.0
    turns = 0
    tofu = MAX_TOFU_LEVEL
    fuel = MAX_FUEL_LEVEL
    hunger = 0

    while not done:
        # Fido
        if random.random() < TOFU_CHANCE:
            # Fido pops up says something and refills tofu
            tofu = MAX_TOFU_LEVEL
            print()
            print("******** Your tofu is magically refilled!")
            print("******** \"You're welcome!\" a voice says.")
            print("******** It's Fido.")
            print("******** He's using his tofu cooking skills.")
        # Hunger message
        if hunger >= 45:
            print("****Your vision blurs and you fall to the ground.")
        elif hunger >= 35:
            print("****Your stomach is currently rumbling a lot. Food is necessary.")
            print("")
        elif hunger >= 20:
            print("****Your stomach is slightly rumbling. Eat food at your own discretion.")
        # Check if reached END GAME
        if km_traveled > MAX_DISTANCE_TRAVELED:
            # WIN
            # Print win scenario (typing way)
            time.sleep(2)
            type_text_output(WIN)

            # Break from while loop
            break

        elif hunger > 45:
            # Lose
            # Print losing hunger scenario
            time.sleep(2)
            type_text_output(LOSE_HUNGER)
            turns += 100
            break

        elif agents_distance >= 0:
            # Lose
            # Print losing agents scenario
            time.sleep(2)
            type_text_output(LOSE_AGENTS)
            turns += 100
            break

        elif fuel <= 0:
            # Lose
            # Print losing fuel scenario
            time.sleep(2)
            type_text_output(LOSE_FUEL)
            turns += 100
            break

        # Give the player their choices
        print(CHOICES)

        # Handle user's input
        users_choice = input("What do you want to do? ").lower().strip("!,.? ")

        if users_choice == "a":
            # Eat
            if tofu > 0:
                tofu -= 1
                hunger = 0
                print()
                print("-------- Mmmmmmm. Soybean goodness.")
                print("-------- Your hunger is sated.")
                print()
            else:
                print()
                print("-------- You have none left.")
                print()
        elif users_choice == "b":
            # Drive slow
            player_distance_now = random.randrange(6, 11)
            agents_distance_now = random.randrange(7, 15)

            # Burn fuel
            fuel -= random.randrange(2, 7)

            # Player distance traveled
            km_traveled += player_distance_now

            # Agent's distance traveled
            agents_distance -= (player_distance_now - agents_distance_now)

            # Feedback to Player
            print()
            print(f"-------- You travelved {player_distance_now} kms!")
            print()
        elif users_choice == "c":
            # Drive Fast
            player_distance_now = random.randrange(10, 16)
            agents_distance_now = random.randrange(7, 15)

            # Burn fuel
            fuel -= random.randrange(5, 11)

            # Player distance traveled
            km_traveled += player_distance_now

            # Agent's distance traveled
            agents_distance -= (player_distance_now - agents_distance_now)

            # Feedback to Player
            print()
            print(f"-------- You sped ahead {player_distance_now} kms!")
            print()
        elif users_choice == "d":
            # Refuel
            # Fill the fuel tank
            fuel = MAX_FUEL_LEVEL

            # Consider the agents coming closer
            agents_distance += random.randrange(7, 15)

            # Give the user feedback
            print()
            print("-------- You filled the fuel tank.")
            print("-------- The agents got closer...")
            print()
        elif users_choice == "e":
            print(f"\t---Status Check---")
            print(f"\tkms traveled: {km_traveled} kms")
            print(f"\tFuel left: {fuel} L")
            print(f"\tAgents are {abs(agents_distance)} kms behind you.")
            print(f"\tYou have {tofu} tofu left.")
            print("\t------\n")
        elif users_choice == "q":
            done = True

        # Increase hunger
        if users_choice not in ["a", "e"]:
            hunger += random.randrange(5, 13)
            turns += 1

        # Pause
        time.sleep(1.2)

    # Outroduction
    print("Thanks for playing! Please play again. =)")

    if turns >= 100:
        print()
        print("You lost, please stop being a failure and do it all again.")
    elif turns >= 18:
        print()
        print(f"You finished the game in {turns} turns.")
        print("Your grade is FAIL. You won, but you're not that good at this are you?")

    elif turns >= 15:
        print()
        print(f"You finished the game in {turns} turns.")
        print("Your grade is C. You won, but you could do much better.")

    elif turns >= 12:
        print()
        print(f"You finished the game in {turns} turns.")
        print("Your grade is B. You won, but you could do even better.")

    elif turns >= 9:
        print()
        print(f"You finished the game in {turns} turns.")
        print("Your grade is A. Well done! Can you beat your score?")


if __name__ == '__main__':
    main()

