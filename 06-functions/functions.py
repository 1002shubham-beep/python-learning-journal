# function = A block of reusable code
#            place () after the function name to invoke it

#def function_name(parameter)
def happy_birthday_song(name,age):
    print(f"Happy Birthday to {name}")
    print(f"You are {age} years old!")
    print(f"Happy Birthday to {name}")
    print()



# happy_birthday_song("Richard Roe",24)
# happy_birthday_song("Jane Doe",27)
# happy_birthday_song("John Doe",12)

#function_name(argument)

#Display Invoice function

def display_invoice(username,amount,due_date):
    print(f"Hello {username}")
    print(f"Your bill of ${amount:.2f} is due on {due_date}")

# display_invoice("Shubham",42.50,"01/01")

# return = statement used to end a function
#          and send a result back to the caller

def add(x,y):
    z = x+y
    return z

def substract(x,y):
    z = x-y
    return z

def multiply(x,y):
    z = x*y
    return z

def divide(x,y):
    z = x/y
    return z

# print(add(5,6)) #print(11), print(return value)
# print(substract(5,6))
# print(multiply(5,6))
# print(divide(5,6))

def create_name(first_name,last_name):
    first_name = first_name.capitalize()
    last_name = last_name.capitalize()
    return(first_name +" "+ last_name)

print(create_name("spongebob","squarepants"))