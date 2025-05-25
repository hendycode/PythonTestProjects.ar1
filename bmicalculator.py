your_weight = float(input("Hi there, how much do you weigh?: "))
print(f"Weight: {your_weight}kg")

your_height = float(input("What is your height? M: "))
print("Weight: " + str(your_weight) + "kg")
print("Height: " + str(your_height) + "m")

bmi = your_weight / your_height ** 2


if bmi >= 25 and bmi <= 29.9:
    print(f"Your BMI is: {bmi}. You are Overweight.")
elif bmi >= 18.5 and bmi <= 24.9:
    print(f"Your BMI is: {bmi}. Your weight is healthy")
elif bmi < 18.5:
    print(f"Your BMI is: {bmi}. You are underweight")
else:
    print(f"Your BMI is: {bmi}. You are Obese.")