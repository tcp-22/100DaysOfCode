# Prompt user for values
print("Enter your height in meters: ") 
user_height = float(input())

print("Enter your weight in kilograms: ")
user_weight = int(input())

# Calculate BMI 
bmi = user_weight / user_height ** 2

# Simplify if/elif logic
if bmi < 18.5:
  print("Underweight")
elif 18.5 <= bmi < 25:
  print("Normal weight")  
elif 25 <= bmi < 30:
  print("Overweight")
else: 
  print("Obese")
