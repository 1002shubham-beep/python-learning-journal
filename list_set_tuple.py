#  collection = single "variable" used to store multiple values
#  List  = [] ordered and mutable. Duplicates OK
#  Set   = {} unordered and immutable, but Add/Remove OK. NO Duplicates
#  Tuple = () ordered and immutable. Duplicates OK. FASTER

# fruits = ["mango","orange","banana","apple"] #list
# fruits = {"mango","orange","banana","apple"} #set
fruits = ("mango","orange","banana","apple") #tuple

# print(dir(fruits))
# print(help(dir(fruits)))

# print(fruits[0:3])
# print(fruits[::2])
# print(fruits[::-1])

# for fruit in fruits:
#     print(fruit,end=", ")

#   List

# print(len(fruits))
# print("apple" in fruits)
# print("pineapple" in fruits)
# fruits[1]="litchi"
# fruits.append("dragonfruit") # adds at the end
# fruits.remove("litchi") # removes the element
# fruits.insert(2,"berry") # inserts the element at the given index
# fruits.sort() 
# fruits.reverse()
# print(fruits.count("banana"))
# print(fruits.index("apple"))
# print(fruits)

#   Set

# print(dir(fruits))
# print(len(fruits))
#   no subscripting ie. [index] cause they aree unordered
# fruits.add("watermelon")
# fruits.remove("mango")
# fruits.pop() #reemoves the first element
#  fruits.clear()
# print(fruits)

#   Tuple
# print(dir(fruits))
print(fruits)
print(fruits.index("apple"))
print(fruits.count("apple"))