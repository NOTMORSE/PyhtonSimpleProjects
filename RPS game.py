import time
import random


def bot():
    computer = ["rock", "paper", "scissors"]
    return random.choice(computer)


def vertical_loading_animation():
    countdown = 3
    while countdown > 0:
        print(countdown, ".....")
        time.sleep(1)
        countdown -= 1
    print("Go!!!")


def main():
    print("Welcome to Rock, Paper, Scissors Game")
    rounds = int(input("Please enter the number of rounds you want to play: "))
    print("Let's Start!!!!")

    score = 0
    com_score = 0
    while rounds > 0:
        bot_choice = bot()
        vertical_loading_animation()
        user_pick = input("Please choose from Rock \U0001F91B, Paper \U0001F91A, or Scissors \U00002702: ").lower()

        if user_pick == bot_choice:
            print(f"You chose {user_pick} \U0001F91B and computer chose {bot_choice} \U0001F91A")
            print("It's a tie")

        elif user_pick == "rock" and bot_choice == "paper":
            print(f"You chose {user_pick} \U0001F91B and computer chose {bot_choice} \U0001F91A")
            print("Computer wins")
            com_score += 1
        elif user_pick == "rock" and bot_choice == "scissors":
            print(f"You chose {user_pick} \U0001F91B and computer chose {bot_choice} \U00002702")
            print("You win")
            score += 1

        elif user_pick == "paper" and bot_choice == "rock":
            print(f"You chose {user_pick} \U0001F91A and computer chose {bot_choice} \U0001F91B")
            print("You win")
            score += 1
        elif user_pick == "paper" and bot_choice == "scissors":
            print(f"You chose {user_pick} \U0001F91A and computer chose {bot_choice} \U00002702")
            print("Computer wins")
            com_score += 1

        elif user_pick == "scissors" and bot_choice == "rock":
            print(f"You chose {user_pick} \U00002702 and computer chose {bot_choice} \U0001F91B")
            print("Computer wins")
            com_score += 1
        elif user_pick == "scissors" and bot_choice == "paper":
            print(f"You chose {user_pick} \U00002702 and computer chose {bot_choice} \U0001F91A")
            print("You win")
            score += 1

        rounds -= 1

    print("Game Over")
    print("Score:")
    print(f"You: {score}", f"\nComputer: {com_score}")
    if score > com_score:
        print("You win")
    elif score < com_score:
        print("You lose")

    repeat = input("Do you want to try again?(y/n): ")
    if repeat == 'y':
        main()
    else:
        print("Thank you for playing")


main()
