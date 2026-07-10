"""
BMI Calculator (20 points)

Write a program that:

Asks for weight in kilograms
Asks for height in meters
Calculates BMI using formula: BMI = weight / (height²)
Displays BMI with 1 decimal place
Shows BMI category based on the ranges below

BMI Categories:

Below 18.5: Underweight
18.5 - 24.9: Normal weight
25.0 - 29.9: Overweight
30.0 and above: Obese

"""
print("=" * 50)
print("BMI Calculator Programe")
print("=" * 50)

waight = float(input("input your weight (kilograms) : "))
height = float(input("input your height (meters) : "))
bmi = waight / (height ** 2)         
print(f"your BMI is : {round(bmi ,1)}")
if bmi < 18.5:
    print("your have Underweight BMI")
elif bmi <= 24.9:
    print("your have Normal weight BMI")
elif bmi <= 29.9:
    print("your have Overweight BMI")
elif bmi > 30.0:
    print("your have Obese BMI")
else:
    print("error")

print("=" * 50)
print("End program Thank")
print("=" * 50)
print()

"""
Question 2: Currency Converter (20 points)

Write a program that converts between Thai Baht (THB) and US Dollars (USD).
Requirements:

Ask user to choose conversion direction (THB to USD or USD to THB)
Ask for the amount to convert
Use exchange rate: 1 USD = 35.5 THB
Display result with 2 decimal places
Show the calculation formula used
"""

print("=" * 50)
print("Currency Converter programe")
print("=" * 50)

print("if want THB to USD press 1")
print("if want USD to THB press 2")
ans = input("press you want :")

if ans == '1':
    print("You select THB to USD")
    num = float(input("press you amount to convert :"))
    result = num / 35.5
    print("you have :" ,round(result ,2),"USD")
    print(f"calculation formula used {num} / 35.5")

elif ans == '2':
    print("You select USD to THB")
    num = float(input("press you amount to convert :"))
    result = num * 35.5
    print("you have :" ,round(result ,2),"THB")
    print(f"calculation formula used {num} * 35.5")

else:
    print("error")

print("=" * 50)
print("End program Thank")
print("=" * 50)