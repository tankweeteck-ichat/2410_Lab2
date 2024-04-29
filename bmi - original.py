def calculate_bmi(height, weight):
    print("Height = " + str(height))
    print("Weight = " + str(weight))
    bmi = weight/(height * height)
    print("BMI = ", round(bmi, 2)) # Round the BMI to 2 decimal points
    if bmi < 18.5:
        print("Under Weight")
    elif bmi > 25.0:
        print("Over Weight")
    else:
        print("Normal Weight")


calculate_bmi(weight=57, height=1.73)
