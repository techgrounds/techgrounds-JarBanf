# ask user to input name
name = input("Enter name:")

if name == "Jared" or name == "jared":
    # if input name is "Jared" or "jared", do this
    print("Welcome back Jared, I missed you!")
else:
    # input name not correct, do this
    print("Hi " + name + ", I don't recognize you. I can not allow you to enter.")