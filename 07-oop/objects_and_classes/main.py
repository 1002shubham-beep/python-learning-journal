import car

car1 = car.Car("Mustang",2024,"Red",False)
car2 = car.Car("Corvette",2025,"Blue",True)
car3 = car.Car("Charger",2026,"yellow",True)

#print(car1) --> Gives the memory address of the object something like 0x000001E2BAB76F90

# print(car1.model)
# print(car1.year)
# print(car1.color)
# print(car1.for_sale)

# print(car2.year)
# print(car2.model)
# print(car2.color)
# print(car2.for_sale)

# print(car3.year)
# print(car3.model)
# print(car3.color)
# print(car3.for_sale)

car1.drive()
car1.stop()
print()
car2.drive()
car2.stop()
print()
car3.drive()
car3.stop()
print()


