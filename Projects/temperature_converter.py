unit = input("Is this temperature in Celsius or Farenheit (C/F): ")
temp = float(input("Enter Temperature: "))

if unit == "C":
    temp = ((temp*9)/5 +32)
    print(f"It's {round(temp,2)}°F")
elif unit == "F":
    temp = ((temp - 32)*5)/9
    print(f"It's {round(temp,2)}°C")
else:
    print(f"{unit} is an invalid unit of measurment")