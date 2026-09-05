# fruits = ["apple","orange","banana","coconut"]
# vegetables = ["celery","carrots","potatoes"]
# meats = ["chicken","fish","turkey"]

groceries = [["apple","orange","banana","coconut"],["celery","carrots","potatoes"],["chicken","fish","turkey"]]


# fruits[0]="pineapple"
# groceries[0][0]="pineapple"
# print(groceries)
# print(groceries[0][1],groceries[1][2],groceries[2][0])

# for grocery in groceries:
#     for food in grocery:
#         print(food,end=" ")
#     print()

keys = (("1","2","3"),("4","5","6"),("7","8","9"),("*","0","#"))
for key in keys:
    for button in key:
        print(button,end=" ")
    print()