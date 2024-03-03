import random


def main():
    print("Welcome to the Number Guessing Game!")
    print("I've selected a number between 1 and 100. \nYou have 5 attempts to guess it.")

    number_chosen = random.randint(0, 101)

    max_attempts = 5

    while max_attempts > 0:

        guess = int(input("Guess a number: "))

        if max_attempts == 0:
            print("You've used all your attempts", f"\nThe hidden number was {number_chosen}")

        if guess < number_chosen:
            print("Try a little higher")
            max_attempts -= 1
            continue
        elif guess > number_chosen:
            print("Try a little lower")
            max_attempts -= 1
            continue
        else:
            print("Congratulations!! You've found the hidden number", f"The hidden number is {number_chosen}")
            break
    else:
        print("You've used all your attempts", f"\nThe hidden number was {number_chosen}")

    another_try = input("Do you want to try again?(y/n): ").lower()
    if another_try == 'y':
        main()
    else:
        print("Thank you for playing the game")


main()