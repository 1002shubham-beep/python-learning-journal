import random

low = 1
high = 100

choices = ("Rock","Paper","Scissors")
cards = ["2","3","4","5","6","7","8","9","J","Q","K","A"]
# number = random.randint(low,high) #random integer from low to high
# number = random.random() #floating point number from 0 to 1
# choice = random.choice(choices)
random.shuffle(cards)
print(cards)