#want to calculate bmi weight in int and height in float answer should be in int
Weight = int(input("Enter your weight: "))
Height = float(input("Enter your number"))
BMI = Weight/(Height**2)
print("BMI:",int(BMI))