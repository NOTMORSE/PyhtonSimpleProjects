import random


def main():

    print("Welcome to Dice Simulator")
    num_dice = int(input("Please enter the number of dice: "))
    num_roll = int(input("Enter the number of sides for each die: "))

    rolls = []
    for _ in range(num_dice):
        roll = random.randint(1, num_roll)
        rolls.append(roll)

    print(f"Rolls: {rolls}")


main()
