

def gather_info():
    height = float(input("Pls enter you height: "))
    weight = float(input("Pls enter you weight: "))
    system = input("M or I: ").lower()
    return (height,weight,system)

def calculate_bmi(weight, height, system="m"):
    if system == "m":
        bmi = (weight / (height ** 2))
    else:
        bmi = 703 * (weight / (height ** 2))
    return bmi

while True:
    height, weight, system = gather_info()
    if system.startswith("i"):
        bmi = calculate_bmi(weight, system=system, height = height)
        print(f"Your BMI is {bmi}")
        break
    elif system.startswith("m"):
        bmi = 10000 * calculate_bmi(weight, system=system, height = height)
        print(f"Your BMI is {bmi}")
        break
    else:
        print("Error")
