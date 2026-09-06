#Rock Paper Scissors game

import random
def play_round():
    options = ("rock","paper","scissors")
    player = None
    computer = random.choice(options)

    while player not in options:
        player = input("Choose a choice(rock,paper,scissors): ")
        print(f"Player:{player}")   
        print(f"Computer:{computer}") 
        if player == computer:
            print("It's a tie.")
        elif player == "paper" and computer == "rock" or player == "scissors" and computer =="paper" or player == "rock" and computer == "scissors":
            print("You Won!")
        else:
            print("You lost!")
        print()

while True:    
        play_round()
        again = input("Press Enter to play again (q to quit): ")
        if again.lower() == "q":
            print("Thanks for playing")
            break