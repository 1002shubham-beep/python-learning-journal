menu={
    "Popcorn":"$1.00",
    "Hot Dog":"$2.00",
    "Giant Pretzel":"$2.00",
    "Asst Candy":"$1.00",
    "Soda":"$1.00",
    "Bottled Water":"$1.00"
}
cart = []
total = 0
print("-------------MENU-------------")
for key, value in menu.items():
    print(f"{key:15}:{value}")
print("------------------------------")

while True:
    food = input("Select an item (q to quit): ").lower()
    print(f"Your cart: {cart}")
    if food  == "q":
        break
    elif menu.get(food) is not None:
        cart.append(food)

for food in cart:
    total += menu.get(food) 