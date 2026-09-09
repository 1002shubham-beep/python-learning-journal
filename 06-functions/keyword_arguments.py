# keyword arguments = an argument preceded by an identifier
#                     helps with readability
#                     order of arguments doesn't matter

def hello(greetings,title,first,last):
    print(f"{greetings} {title}{first} {last}")

# hello("Hello",first="Spongebob",title="Mr.",last="Sqaurepants")
#positional argument should be written first then keyword argument

# hello("Good Evening",title="Dr.",last="Doakes",first="James")

#------------------example------------------
# for x in range(1,11):
#     print(x,end=" ")

# print()

# print("1","2","3","4","5",sep="-")

#------------------exercise-----------------
def get_phone_number(country,area,first,last):
    return f"{country}-{area}-{first}-{last}"

phone_num = get_phone_number(country=1,area=123,first=456,last=789)

print(phone_num)