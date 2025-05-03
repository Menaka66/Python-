def calculate_bmi(weight_kg, height_cm):
    height_m = height_cm / 100  # Convert cm to meters
    bmi = weight_kg / (height_m ** 2)
    return round(bmi, 2)

def bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi <= 24.9:
        return "Normal weight"
    elif 25 <= bmi <= 29.9:
        return "Overweight"
    elif 30 <= bmi <= 34.9:
        return "Obesity Class I (Moderate)"
    elif 35 <= bmi <= 39.9:
        return "Obesity Class II (Severe)"
    else:
        return "Obesity Class III (Very severe or morbid)"

print("🧮 BMI Calculator (Metric Units)")


age = int(input("Enter your age (2–120): "))
if not 2 <= age <= 120:
    print("Age out of acceptable range.")

gender = input("Enter your gender (Male/Female/Other): ").strip().capitalize()
height_cm = float(input("Enter your height in centimeters (e.g., 153): "))
weight_kg = float(input("Enter your weight in kilograms (e.g., 99): "))

if height_cm <= 0 or weight_kg <= 0:
    print("Height and weight must be positive.")

bmi = calculate_bmi(weight_kg, height_cm)
category = bmi_category(bmi)

print(f"\nAge: {age}")
print(f"Gender: {gender}")
print(f"Your BMI is: {bmi}")
print(f"Health Status: {category}")
