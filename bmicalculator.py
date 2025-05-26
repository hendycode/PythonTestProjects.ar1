your_weight = float(input("Please input your Weight: "))
your_height = float(input("Please input your Height (M): "))

bmi = your_weight / (your_height ** 2)

if bmi > 30 :
    print(f"Your BMI is {bmi:.4}.\nYou are obese.")
elif bmi >= 25 and bmi <= 29.9:
    print(f"Your BMI is {bmi:.4}.\nYou are overweight.")
elif bmi >= 18.5 and bmi <= 24.9:
    print(f"Your BMI is {bmi:.4}.\nYour weight is healthy.")
else:
    print(f"Your BMI is {bmi:.4}.\nYou are underweight.")