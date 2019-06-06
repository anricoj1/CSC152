#BMI= (weight * 703)/(height * height)
# Find BMI and tell how person ranks 
height = int(input("Please enter your height in inches: "))
weight = int(input("Please enter your weight in pounds: "))
bmi = (weight * 703) / (height * height)
if bmi <= 18.5:
        print("Your BMI is", bmi, "which means you are underweight.")
else:
        if bmi > 18.5 and bmi < 25:
                print("Your BMI is", bmi, "which means you are normal.")
                if bmi > 25 and bmi < 30:
                        print("Your BMI is", bmi, "which means you are overweight.")
                        if bmi > 30:
                                print("Your BMI is", bmi, "which means you are obese.")
                                
                        
