#Membership operators = used to test whether a value or variable is found in a sequence (string,list,tuple,set,or dictionary) 1.in 2.not in

word = "APPLE"

# letter = input("Guess a letter in the secret word: ")
# if letter in word:
#     print(f"There is a {letter} in the word")
# else:
#     print(f"{letter} was not found")

# if letter not in word:
#     print(f"{letter} was not found")
# else:
#     print(f"There is a {letter} in the word")


# fruits = {"Mango","Apple","Banana","Papaya","Watermelon","Litchi"}

# fruit = input("Guess a fruit: ")
# if fruit in fruits:
#     print(f"There is a {fruit} in fruits")
# else:
#     print(f"{fruit} was not found")

# email = input("Enter your email address: ")
#Example:
email = "brucewayne@wayneenterprises.com"

if "@" in email and "." in email:
    print(f"{email} is valid")
else:
    print(f"{email} is invalid")