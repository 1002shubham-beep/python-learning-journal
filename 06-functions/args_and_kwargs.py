# *args    = allows you to pass multiple non-key arguments
# **kwargs = allows you to pass multiple keyword-arguments
#            * unpacking operator 
#            1. positional 2. default 3. keyword 4. ARBITRARY

# def add(*args):
#     total = 0
#     for arg in args:
#         total += arg
    
#     return total

# print(add(1,2,3,4))

# def display_name(*names):
#     for name in names:
#         print(name,end=" ")

# display_name("Tony Stark","Steve Rogers","Bruce Banner","Thor Odinson")


def print_address(**kwargs): #kwargs = dictionary
    for key,value in kwargs.items():
        print(f"{key}: {value}")

# print_address(street="123 Fake St.",
#               city= "Detroit",
#               state="MI",
#               zip="54321")

# print_address(house_number="221",
#               sub_division="B",
#               street = "Baker Street",
#               city = "London",
#               postal_code = "NW1 6XE",
#               country = "UK",
#               )

def shipping_label(*args,**kwargs):
    for arg in args:
        print(arg,end=" ")
    print()
    for kwarg in kwargs.values():
        print(kwarg)

shipping_label("Detective","Sherlock","Holmes",
                house_number="221",
              sub_division="B",
              street = "Baker Street",
              city = "London",
              postal_code = "NW1 6XE",
              country = "UK",)