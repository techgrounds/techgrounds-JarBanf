# ask user to input number
num = float(input("Enter a number: "))

"""if num < 100:
    # if input number is less then 100, do this
    print("Number is lower than 100")
elif num == 100:
    # if input number is 100, do this
    print("A perfect 100")
else:
    # if we are here, that means the number is more then 100, do this
    print("Number is higher than 100")"""

while num != 100:
    # while input number is NOT 100 do this
    print("Entered number is NOT 100.")
    # ask user to input a number again
    num = float(input("Enter a number: "))
else:
    # input number is 100, do this
    print("100 is perfect!!")