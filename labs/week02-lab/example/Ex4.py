print("4. BMI Calculator:")
print("   - Ask for weight (kg) and height (m)")
print("   - Calculate: BMI = weight / (height ** 2)")
print()

print("=" * 50)
print("BMI Calculator Programe")
print("=" * 50)

waight = float(input("input your weight (kilograms) : "))
height = float(input("input your height (meters) : "))
bmi = waight / (height ** 2)         
print(f"your BMI is : {bmi:.2f}")

print("=" * 50)
print("End program Thank")
print("=" * 50)
print()