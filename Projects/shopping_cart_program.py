# # Shopping cart program

# foods = []
# prices = []
# total = 0

# while True:
#     food = input("Enter a food to buy(q to quit): ")
#     if food.lower() == "q":
#         break
#     else:
#         price = float(input(f"Enter the price of a {food}: $"))
#         foods.append(food)
#         prices.append(price)

# print("----- YOUR CART -----")
# for food in foods:
#     print(food,end=" ")

# for price in prices:
#     total = total + price
# print()
# print(f"Your total is ${total}")


foods = []
prices = []
total = 0 

# while True:
#     food = input("Enter the name of the food item(Q to quit): ")
#     foods.append(food)
#     if food == 'q'.upper():
#         break
#     else:
#         price = input(f"Enter the price of {food}:$ ")
#         prices.append(price)

# print("-------------Your Cart-------------")
# for item in foods:
#     for am in prices:
#         print(f"{item}:{am}")

# while True:
#     price = input("Enter the price of food: $")
#     prices.append(price)
#     if price == 'q'.upper():
#         break

# for amount in prices:
#     total = amount+total
# print(f"Your total:{total}")

while True:
    food = input("Enter the name of the food(Q to quit): ")
    if food == 'q'.upper():
        break
    else:
        price = input(f"Enter the price of {food}: $ ")
        prices.append(price)

print("-------Your Cart-------")
print(foods)
for amount in prices:
    total = total + amount
print(f"Your Total: {total}")
    




