import random 

guesses = 0
low = 1
high = 100
answer = random.randint(low,high) 
is_running = True

while is_running:
    guess = int(input(f"Guess a number between {low} and {high}: "))
    guesses +=1
    if guess<low or guess>high:
       print("Number out of range. Try Again!")
    elif guess < answer:
        print("Too low. Try Again!")
    elif guess > answer:
        print("Too high. Try Again!")
    else:
        print(f"Correct! The answer was {answer}")
        print(f"Total number of guesses {guesses}")
        break