# Conditions

Python supports the usual logical conditions from mathematics:

- Equals: `a == b`
- Not Equals: `a != b`
- Less than: `a < b`
- Less than or equal to: `a <= b`
- Greater than: `a > b`
- Greater than or equal to: `a >= b`

These conditions can be used in several ways, most commonly in "if statements" and loops.

An "if statement" is written by using the if keyword.

## Key-terms


## Assignment

<ins>Exercise 1</ins>

- Create a new script.
- Use the input() function to ask the user of your script for their name. If the name they input is your name, print a personalized welcome message. If not, print a different personalized message.

<ins>Exercise 2</ins>

- Create a new script.
- Ask the user of your script for a number. Give them a response based on whether the number is higher than, lower than, or equal to 100.
- Make the game repeat until the user inputs 100.

### Used sources
- [Python If ... Else](https://www.w3schools.com/python/python_conditions.asp)

### Encountered problems
None

### Result

**<ins>Exercise 1</ins>**

Script --> [exercise1.py](/09_Python/includes/05_exercise1.py)

```py
# ask user to input name
name = input("Enter name:")

if name == "Jared" or name == "jared":
    # if input name is "Jared" or "jared", do this
    print("Welcome back Jared, I missed you!")
else:
    # input name not correct, do this
    print("Hi " + name + ", I don't recognize you. I can not allow you to enter.")
```

![exercise1.py](/09_Python/includes/05_conditions1.png)<br><br>

**<ins>Exercise 2</ins>**

Script --> [exercise2.py](/09_Python/includes/05_exercise2.py)

```py
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
```

![exercise2.py](/09_Python/includes/05_conditions2.png)<br><br>