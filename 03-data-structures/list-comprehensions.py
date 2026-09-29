#List comprehesion = A concise way to create lists in Python. Compact and easier to read than traditional loops[expression for value in iterable if condition]

# doubles = []
# for x in range(1,11):
#     doubles.append(x*2)

# print(doubles)

doubles = [x*2 for x in range(1,11)]
triples = [x*3 for x in range(1,11)]
squares = [x*x for x in range(1,11)]
# print(doubles)
# print(triples)
# print(squares)

#Making each of them uppercase
fruits = ["apple","banana","mango","orange"]
fruits = [fruit.upper() for fruit in fruits ]  #reassigning fruits
print(fruits)

#Making list with first letter of eeach of them
first_letter_fruit = [fruit[0] for fruit in fruits]
print(first_letter_fruit)

#Finding even and odd numbers
nums = [-56,64,-1,-75,23]
even = [num for num in nums if num%2 ==0]
odd = [num for num in nums if num%2 !=0]
print(even)
print(odd)

#Making list of positive numbers
nums = [num *-1 if num<0 else num for num in nums]
print(nums)
print()
#Passing students
# marks = [45,78,95,45,60]
# passing = [marks.index(mark)+1 for mark in marks if mark >= 60]
# print(f"Passing students: {passing}")

#Passing students(advanced)
marks = {
    "Steve":45,
    "John":78,
    "Sam":95,
    "Jenna":45,
    "Harry":60
}

passing = [name for name,score in marks.items() if score>=60]
print(f"Passing students are: {passing}")
