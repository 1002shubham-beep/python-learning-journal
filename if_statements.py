# if = Do some code only if some conditions is True
# Else do something else

# age = int(input("Enter your age: "))

# if(age>=100):
#     print("How come you are still alive.")
# elif age>=18:
#     print("You are eligible for a credit card")
# elif age<=0:
#     print("Are you kidding?")
# else:
#     print(f"Sorry, you have to wait for {18-age} for your credit card.")

# Food 

response = input("Would you like to have some food? (Y/N):")

if response == "Y":
    item = input("What would you like to have: 1.Burger 2.Fries 3.Pasta 4.Pizza 5.Sandwich ")
    if item == "Burger":
        quantity = input(f"How many {item} would you like to order ")
        confirm = input(f"Confirm {quantity} {item}? (Y/N): ")
        if confirm == "Y":
            print("Order Confirmed")
        else:
            print("Order Cancelled")
    elif item == "Fries":
        quantity = input(f"How many {item} would you like to order ")
        confirm = input(f"Confirm {quantity} {item}? (Y/N): ")
        if confirm == "Y":
            print("Order Confirmed")
        else:
            print("Order Cancelled")
    elif item == "Pasta":
        quantity = input(f"How many {item} would you like to order ")
        confirm = input(f"Confirm {quantity} {item}? (Y/N): ")
        if confirm == "Y":
            print("Order Confirmed")
        else:
            print("Order Cancelled")
    elif item == "Pizza":
        quantity = input(f"How many {item} would you like to order ")
        confirm = input(f"Confirm {quantity} {item}? (Y/N): ")
        if confirm == "Y":
            print("Order Confirmed")
        else:
            print("Order Cancelled")
    elif item == "Sandwich":
            quantity = input(f"How many {item} would you like to order ")
            confirm = input(f"Confirm {quantity} {item}? (Y/N): ")
            if confirm == "Y":
                print("Order Confirmed")
            else:
                print("Order Cancelled")
else: print("Sorry to see you go")