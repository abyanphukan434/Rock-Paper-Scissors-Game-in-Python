from quizGame import play_again
import random

while True:
    choices = ['rock', 'paper', 'scissors']

    player = None
    computer = random.choice(choices)

    while player not in choices:
        player = input("Rock, Paper or Scissors?: ").lower()

    if player == computer:
        print("Computer", computer)
        print("Player", player)
        print("TIE!")

    elif player == "rock":
        if computer == "paper":
            print("Computer", computer)
            print("Player", player)
            print("YOU LOSE!")
    
        if computer == "scissors":
            print("Computer", computer)
            print("Player", player)
            print("YOU WIN!")

    elif player == "scissors":
        if computer == "rock":
            print("Computer", computer)
            print("Player", player)
            print("YOU LOSE!")

        if computer == "paper":
            print("Computer", computer)
            print("Player", player)
            print("YOU WIN!")

    elif player == "paper":
        if computer == "scissors":
            print("Computer", computer)
            print("Player", player)
            print("YOU LOSE!")

        if computer == "rock":
            print("Computer", computer)
            print("Player", player)
            print("YOU WIN!")

    play_again = input("Play again? (yes/no): ").lower()

    if play_again != "yes":
        break
    print("Bye!")