def calculate_bmi(weight,height):
    bmi = weight/(height **2)
    return bmi

def get_bmi_class(bmi):
    if bmi < 19:
     return "underweight"
    elif bmi < 25:
     return "normal"
    elif bmi < 35:
     return "overweight"
    else:
     return "Obese"

def main():
    weight = float(input("Enter your weight in kg:"))
    height = float(input("Enter your height in metres:"))

    bmi = calculate_bmi(weight,height)
    bmi_class = get_bmi_class(bmi)

    print(f"Your BMI is:{bmi:.2f}")
    print(f"Your BMI class is:{bmi_class}")

if __name__=="__main__":
    main()
