# name = input("Enter your full name: ")
# phone_number = input("Enter your phone number: ")

# result = len(name)
# result =name.find("S")
# result = name.rfind("a")
# result = name.capitalize()
# result = name.upper()
# result = name.lower()
# result = name.isdigit()
# result = name.isalpha()
# result = phone_number.count("-")
# result = name.replace("Prasad","Wayne")
# print(result)

user_name = input("Enter your username: ")
if len(user_name)>12:
    print("Your username can't be more than 12 characters.")
elif not user_name.find(" ")==-1:
    print("Your username can't contain spaces.")
elif not user_name.isalpha():
    print("Your username can't contain numbers")
else:
    print(f"Welcome {user_name}")