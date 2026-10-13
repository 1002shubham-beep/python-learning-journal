# super() = Function used in a child class to call methods from a parent class (Superclass).
#           Allows you to extend the functionality of the inherited methods.

class Shapes:
     def __init__(self,colour,is_filled):
        self.colour = colour
        self.is_filled = is_filled

     def describe(self):
         print(f"It is {self.colour} and {'filled' if self.is_filled else 'not filled'}")

class Circle(Shapes):
    def __init__(self,colour,is_filled,radius): # calling the constructor of the parent/super class
        super().__init__(colour,is_filled)
        self.radius = radius
    def describe(self):
        print(f"Area: {3.14*self.radius*self.radius}sq. units")
        super().describe()

class Sqaure(Shapes):
    def __init__(self,colour,is_filled,width):
        super().__init__(colour,is_filled)
        self.width = width

class Triangle(Shapes):
    def __init__(self,colour,is_filled,width,height):
        super().__init__(colour,is_filled)
        self.width = width
        self.height = height

circle = Circle("Yellow",True,30)
sqaure = Sqaure("Red",False,20)
triangle = Triangle("Blue",True,10,20)

print(circle.colour)
print(circle.is_filled)
print(circle.radius)
circle.describe()
print()
print(sqaure.colour)
print(sqaure.is_filled)
print(sqaure.width)
sqaure.describe()
print()
print(triangle.colour)
print(triangle.is_filled)
print(triangle.width)
print(triangle.height)
triangle.describe()

