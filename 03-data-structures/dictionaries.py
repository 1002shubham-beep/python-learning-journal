# dictionary = a collection of {key:value} pairs
#              ordered and changeable. No duplicates

capitals = {
    "India" : "New Delhi",
    "United States" : "Washington, D.C.",
    "China" : "Beijing",
    "Mexico" : "Mexico City",
    "Egypt" : "Cairo",
}

print(capitals.get("Egypt"))

# if capitals.get("Mexico"):
#     print("That capital exists")
# else:
#     print("That capital doesn't exists.")

capitals.update({"Germany":"Berlin"})

capitals.update({"India":"Jaipur"})
capitals.pop("China")
# print(capitals)
print()
keys = capitals.keys()
# print(keys)
capitals.popitem() # removes the latest key value pair
# capitals.clear()
# print(capitals)
# for key in capitals.keys():
#     print(key)
# print()
# for value in capitals.values():
#     print(value)

for key, value in capitals.items():
    print(f"{key}:{value}")