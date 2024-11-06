def calculate_bmi(height, weight):
    print("Height = " + str(height))
    print("Weight = " + str(weight))
    BMI = weight/(height **2)
    print("BMI = ", round(BMI, 2))
    print("Weight Classification: ", end="")
    if BMI < 18.5:
        print("Under Weight")
        return -1
    elif BMI > 25.0:
        print("Over Weight")
        return 1
    else:
        print("Normal Weight")
        return 0

result = calculate_bmi(weight=57, height=1.73)
print("Result = ",result)
result = calculate_bmi(weight=97, height=1.73)
print("Result = ",result)
result = calculate_bmi(weight=37, height=1.73)
print("Result = ",result)
calculate_bmi(weight=97, height=1.73)
print("================")
calculate_bmi(weight=37, height=1.73)
print("================")




