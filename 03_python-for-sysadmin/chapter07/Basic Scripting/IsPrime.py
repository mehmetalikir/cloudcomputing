
#The number to be tested for primeness
def is_Prime(num):
    for i in range(2, num):
        #If remainder - value left after the division is not eqauls 0
        if (num % i == 0):
            return False
    return True


while True:
    num = int(input("Please enter an integer number > 1: "))
    if (is_Prime(num)):
            #Display the prime number
            print(num, "is a prime number.")
            break
    elif (not is_Prime(num)):
        print(num, "is not a prime number.")
    else:
        print("Error...")


