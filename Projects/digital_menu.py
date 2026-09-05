print("Welcome to our Restaurant")
response = input("Would you like to order? (Y/N): ")
print("\n")
if response == "Y":
    print("1.Burger")
    print("2.French Fries")
    print("3.Pasta")
    print("4.Pizza")
    print("5.Sandwich")
    food = input("What would you like to order? ")
    if food =="Burger":
            print(f"Choose your {food}")
            food_type = input("\n1.Veg Burger $5.99\n 2.Chicken Burger $7.99\n 3.Egg Burger $6.99\n 4.Double Chicken Burger $10.99 \n")
            quantity = input(f"How many {food_type} would you like to order? ")
            confirmation = input(f"Confirm the order for {quantity} {food_type}? (Y/N): ")
            if confirmation =="Y":
                print(f"Order placed for {quantity} {food_type}")
            else:
                print("Order Cancelled")
    elif food =="French Fries":
            print(f"Choose your {food}")
            food_type = input("\n1.Classic Fries $3.49\n 2.Peri-Peri Fries $4.99\n 3.Cheese Fries $5.99 \n")
            quantity = input(f"How many {food_type} would you like? ")
            confirmation = input(f"Confirm the order for {quantity} {food_type}? (Y/N): ")
            if confirmation =="Y":
                print(f"Order placed for {quantity} {food_type}")
            else:
                print("Order Cancelled")
    elif food =="Pasta":
            print(f"Choose your {food}")
            food_type = input("\n1.White Sauce Pasta $9.49\n 2.Red Sauce Pasta $8.49\n 3.Chicken Pasta $11.49 \n")
            quantity = input(f"How many {food_type} would you like? ")
            confirmation = input(f"Confirm the order for {quantity} {food_type}? (Y/N): ")
            if confirmation =="Y":
                print(f"Order placed for {quantity} {food_type}")
            else:
                print("Order Cancelled")
    elif food =="Pizza":
            print(f"Choose your {food}")
            food_type = input("\n1.Margherita $8.99\n 2.Veggie Pizza $10.99\n 3.Chicken Pizza $12.99\n 4.Pepperoni Pizza $13.99 \n")
            quantity = input(f"How many {food_type} would you like? ")
            confirmation = input(f"Confirm the order for {quantity} {food_type}? (Y/N): ")
            if confirmation =="Y":
                print(f"Order placed for {quantity} {food_type}")
            else:
                print("Order Cancelled")
    elif food =="Sandwich":
            print(f"Choose your {food}")
            food_type = input("\n1.Veg Sandwich $5.99\n 2.Egg Sandwich $6.99\n 3.Chicken Sandwich $8.49\n 4.Cheese Sandwich $6.99 \n")
            quantity = input(f"How many {food_type} would you like? ")
            confirmation = input(f"Confirm the order for {quantity} {food_type}? (Y/N): ")
            if confirmation =="Y":
                print(f"Order placed for {quantity} {food_type}")
            else:
                print("Order Cancelled")
else:
    print("Sorry to see you go")