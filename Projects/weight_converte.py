weight = float(input("Enter your weight: "))
unit = input("Enter unit (Kg/Lbs)")

if unit == "Kg":
    weight *= 2.20462
    print(f"You weight {round(weight,3)} Lbs")
elif unit == "Lbs":
    weight /=2.20462
    print(f"You weight {round(weight,3)} Kg")