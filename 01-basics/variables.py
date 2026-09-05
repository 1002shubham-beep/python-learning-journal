# This is my first python program
print('I am Batman')

#Variable =  A container for a value (string, integer, float, boolean)
#            A variable behaves as if it was the value it contains

# Strings
first = 'My name is Shubham'
food = 'roasted chciken'
email = '1002shubham@gmail.com'

print(f"Hello, {first}")
print(f"You like {food}")
print(f"Your email is {email}")

# Integers (whole number)
age =20
quantity = 3
num_of_students = 98
print(f"You are {age} years old")
print(f"You are buying {quantity} items")
print(f"Your class has {num_of_students} students")

# Float 
price = 10.99
gpa = 9.8
distance = 10.86
print(f"The price is ${price}")
print(f"Your GPA is {gpa}")
print(f"You ran {distance}km")

# Boolean
is_student = True
is_graduate = False
for_sale = True
is_online = False

print(f"Are you a students?: {is_student}")

if for_sale:
    print(f"Car is for sale?: {for_sale}")
else: print(f"Car is not available")

if is_online:print("You are online")
else: print("You are offline")