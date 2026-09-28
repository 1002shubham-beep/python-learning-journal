# Iterables = An object/collection that can return its elements one at a time,
#             allowing it to be iterated over in a loop

numbers = [1,2,3,4,5]

# for number in reversed(numbers):
#     print(number,end="\t")

# lists,tupples and sets are iterable
# sets are not reversible as they are unordered

name = "Bruce Wayne"

# for character in name:
#     print(character,end=" ")

my_fruits_bucket = {
    "A":"Apples",
    "B":"Oranges",
    "C":"Papayas",
    "D":"Mangoes"
}

for key, value in my_fruits_bucket.items():
    print(f"{key}: {value}")