# ask user to input number
num = float(input("Enter a number: "))


if num < 100:
    # if input number is less then 100, do this
    print("Number is lower than 100")
elif num == 100:
    # if input number is 100, do this
    print("A perfect 100")
else:
    # if we are here, that means the number is more then 100, do this
    print("Number is higher than 100")