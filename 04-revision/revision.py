# num = int(input("Enter a number: "))
# for i in range(1,11):
#     print(f"{num} x {i} = {num*i}")

# word = input("Enter a word: ")
# total = 0
# for i in range(0,len(word)):
#     if word[i] =="a":
#         total += 1
# print(f"a appears {total} times")

# i =1
# while i<=5:
#     print(i)
#     i += 1

# i = 10
# while i > 0 :
#     print(i)
#     i -= 1
# print("Blast off!")

# total = 0
# i =0
# while total <=100:
#     i += 1
#     total = total +i
# print(total)

# Password Checker
# passw = "python123"
# user_pass = input("Enter password: ")
# while not passw == user_pass:
#     print("Wrong password")
#     user_pass = input("Enter password: ")
# print("Corect password")

# Number Guessing
# secret = 7
# guess = int(input("Guess the number: "))

# while not secret == guess:
#     if guess > secret:
#         print("Too high!")
#         guess = int(input("Guess the number: "))
#     else:
#         print("Too low!")
#         guess = int(input("Guess the number: "))
# print("Correct!")

#Quiz Game

# questions = ("What is the capital of France?",

#              "Which gas do plants primarily use for photosynthesis?",

#              "How many sides does a hexagon have?",

#              "Who is known as the Father of Computers?",

#              "Which is the largest planet in our Solar System?")

# options = (("A. London", "B. Paris", "C. Rome", "D. Berlin"),

#            ("A. Oxygen", "B. Nitrogen", "C. Carbon Dioxide", "D. Hydrogen"),

#            ("A. Five", "B. Six", "C. Seven", "D. Eight"),

#            ("A. Isaac Newton", "B. Charles Babbage", "C. Albert Einstein", "D. Alan Turing"),

#            ("A. Earth", "B. Saturn", "C. Jupiter", "D. Neptune"))

# answers = ("B",

#            "C",

#            "B",

#            "B",

#            "C")

# correct_answers = ("Paris",

#                    "Carbon Dioxide",

#                    "Six",

#                    "Charles Babbage",

#                    "Jupiter")

# guesses = []

# question_num = 0

# score = 0

# for question in questions:
#     print("-------------------------------")
#     print(questions[question_num])
#     for option in options[question_num]:
#      print(option)
#     guess = input("Enter answer (A, B, C, D,): ").upper()
#     guesses.append(guess)
#     if guess == answers[question_num]:
#        print("Correct!")
#        score += 1
#     else:
#        print("Incorrect!")
#        print(f"{correct_answers[question_num]} is the correct answer")
#     question_num +=1

# fruit_colour = {
#     "Apple":"Red",
#     "Banana":"Yellow",
#     "Papaya":"Orange",
# }
# # print(fruit_colour["Apple"])
# print(dir(fruit_colour))
# print(fruit_colour.get("Banana"))
# print(fruit_colour.items())
# print(fruit_colour.items())

# s1  = 'hello.w'
# print(s1[1:7])

# def shubh():
#     print("I am Shubham")

# shubh()

# def sum(a,b):
#   print(a+b)

# sum(7,8)

# def addition(a,b):
#     return(a+b)

# result = addition(2,4) +1
# print(result)

# def display_invoice(name,amount,due_date):
#     print(f"Hello {name}")
#     print(f"You have ${amount:.2f} due on {due_date}")


# display_invoice("Steve",5000.86,"14/07/27")

# def username_maker(name,age,sign):
#     username = name.lower()+str(age)+sign[0:3].lower()
#     return username

# print(f"Your username is {username_maker("Shubham",20,"Gemini")}")
# print(f"Your username is {username_maker("John",22,"Taurus")}")
# print("Your username is:")
# print(username_maker("Shreya",21,"Pisces"))

# def fullname(first_name,last_name):
#     first_name = first_name.capitalize()
#     last_name = last_name.capitalize()
#     return first_name +" "+ last_name

# print(fullname("spongebob","squarepants"))

# def net_price(mrp,discount,tax=3):
#     return mrp * (1-discount) * (1+tax)

# print(f"{net_price(240,0.56):.2f}")

import time

def countdown(start,end):
    for x in range(start, end+1):
        print(x)
        time.sleep(1)
    print("Done")