import math

operator = input("Enter an operator (+,-,*,/): ")
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

if operator == "+":
    print(round(num1+num2),3)
elif operator == "-":
    print(round(num1-num2),3)
elif operator == "*":
    print(round(num1*num2),3)
elif operator == "/":
    if(num2 == 0):
        print("denominator cannot be 0")
    else:
        print(round(num1/num2),3)
else:
    print(f"{operator} is not a valid operator")