# variable scope - where a variable is visible and accessible
# scope resolution = (LEGB) Local -> Enclosed -> Global -> Built-in

# Local

# def func1():
#     a=2
#     print(a)

# def func2():
#     b=3
#     print(b)

# func1()
# func2()

# Enclosed

# def func1():
#     x = 2
#     print(x)

#     def func2():
#         x = 3
#         print(x)
#         func2()

# func1()

# Global
# x = 2
# def func1():
#     print(x)

# func1()

# Built-In

# from math import e
# e = 2.9
# print(e)