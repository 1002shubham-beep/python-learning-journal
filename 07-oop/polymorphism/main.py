# Polymorphism = Greek word that means to "have many forms or faces"
#                Poly = Many
#                Morphe = Form
#                TWO WAYS TO ACHIEVE POLYMORPHISM
#                1.Inheritance = An object could be treated of the same type as a parent class
#                2. "Duck Typing" = Objectmust have necessary attributes/methods

from abc import ABC, abstractclassmethod

class Shape(ABC):
    @abstractclassmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self,radius):
        self.radius= radius

    def area(self):
        return 3.14 * self.radius**2
    
class Sqaure(Shape):
    def __init__(self,side):
        self.side= side

    def area(self):
        return self.side**2
    
class Triangle(Shape):
    def __init__(self,base,height):
        self.base= base
        self.height = height

    def area(self):
        return self.base*self.height*0.5

class Pizza(Circle):
    def __init__(self, toppings,radius):
        self.toppings = toppings
        self.radius = radius

shapes = [Circle(5),Sqaure(4),Triangle(6,7),Pizza("BBQ",15)]

for shape in shapes:
    print(shape.area())