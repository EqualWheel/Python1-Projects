


# Challenge: Provide feedback to the use based on their BMI category (e.g., underweight, normal weight, overweight, obese).
# Input: Prompt the user to enter their weight in kilograms abd height in meters.
# Processing: Calculate the BMI using the formula: BMI = Weight / (Height^2).
# Output: Display the calculated BMI.



# Input
weight_input = input("Enter your weight in Kilograms: ")
height_input = input("Enter your height in meters: ")

# Convert Input
weight = float(weight_input)
height = float(height_input)

# Processing
bmi = weight / (height ** 2)

# Output
print("Your BMI is: ", bmi)