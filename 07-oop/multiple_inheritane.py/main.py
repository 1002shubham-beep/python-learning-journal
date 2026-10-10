# multiple inheritance = inherit from more than one parent class
#                        C(A,B)

#multilevel inheritance = inherit from a parent which inherits from another parent
#                         A -> B(A) -> C(B)

class Mother:
    def __init__(self):
        pass

    face_shape= "Square"
    nose = "Sharp"

class Father:
    def __init__(self):
        pass

    eyes = "Almond"

class Child(Father,Mother):
    pass

# child = Child()
# print(child.face_shape)
# print(child.nose)
# print(child.eyes)

class Animal:
    def __init__(self,name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is sleeping")

class Prey(Animal):
    def flee(self):
        print(f"{self.name} is fleeing")

class Predator(Animal):
    def hunt(self):
        print(f"{self.name} is hunting")

class Rabbit(Prey):
    pass

class Hawk(Predator):
    pass

class Fish(Predator,Prey):
    pass

rabbit = Rabbit("Bugs")
hawk = Hawk("Tony")
fish = Fish("Nemo")

rabbit.flee()
rabbit.eat()
rabbit.sleep()
print()
hawk.hunt()
hawk.eat()
hawk.sleep()
print()
fish.hunt()
fish.flee()
fish.eat()
fish.sleep()