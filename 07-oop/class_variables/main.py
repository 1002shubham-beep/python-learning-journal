# class variables = Shared among all instances of a class
#                   Defined outside the constructor 
#                   Allow you to share data among all objects created from that class

class Students:

    class_year = 2024 
    num_students = 0

    def __init__(self,name,age):
        self.name = name # instance variable
        self.age = age
        Students.num_students +=1

student1 = Students("Jack",20)
student2 = Students("Steve",21)
student3 = Students("Olivia",19)

print(student1.name)
print(student1.age)
# print(student1.class_year)
print(Students.class_year)
print()
print(student2.name)
print(student2.age)
# print(student2.class_year)
print(Students.class_year)
print()
print(student3.name)
print(student3.age)
# print(student3.class_year)
print()
print(f"Class year of {student1.name},{student2.name} an {student3.name} is {Students.class_year}")
print(f"Number of students is {Students.num_students}")
