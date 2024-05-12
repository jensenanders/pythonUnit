
def calculate_bmi(height, weight):
    bmi = weight * (height ** 2)
    return bmi

def get_category(height, weight):
    bmi = weight / (height ** 2)

    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal weight"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obese"
 