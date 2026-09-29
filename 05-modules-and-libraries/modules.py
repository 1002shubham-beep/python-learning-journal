# module = a file containing code you want to include in your program use 'import' to include a module (built-in or your own) useful to break up a large program reusable separate files

# print(help("math"))

# import math
# print(math.pi)

# import math as m
# print(m.pi)

# from math import pi
# print(pi)
# not preffered as there can be name conflicts

#example:
# from math import e
# a,b,c,d,e = 1,2,3,4,5
# print(e**a)
# print(e**b)
# print(e**c)
# print(e**d)

import example

result = example.pi
print(result)
square = example.sqaure(2)
print(square)
cube = example.cube(2)
print(cube)
circumference= example.circumference(2)
print(circumference)
area = example.area(2)
print(area)