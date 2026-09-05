#input() = A function that prompts the user to enter data and it returns the entered data as a strinf

# name = input("What is your name")
# print(f"Hello {name}")

# age = int(input("How old are you?"))#user inputs are always a string
# age = age +1
# print(f"Your age is {age}") 

# Area of rectangle

# length = float(input("Enter the length of the rectangle "))
# breadth = float(input("Enter the breadth of the rectangle "))
# print(f"The area of the rectangle is {length*breadth} sq. units")

# Shopping Cart Program

item = input("What item would you like to buy?: ")
price = float(input("What is the price?: "))
quantity = int(input("How many would you like?: "))
total = price*quantity

print(f"You have bought {item} x {quantity}/s")
print(f"Your total is ${total}")