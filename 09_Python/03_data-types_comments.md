# Data types and Comments

<ins>Data types</ins>  
In programming, data type is an important concept.

Variables can store data of different types, and different types can do different things.

Python has the following data types built-in by default, in these categories:
- Text Type:        `str`
- Numeric Types: 	`int`, `float`, `complex`
- Sequence Types: 	`list`, `tuple`, `range`
- Mapping Type: 	`dict`
- Set Types: 	    `set`, `frozenset`
- Boolean Type: 	`bool`
- Binary Types:     `bytes`, `bytearray`, `memoryview`
- None Type: 	    `NoneType`

<ins>Comments</ins>  
Comments can be used to:

- explain Python code.
- make the code more readable.
- prevent execution when testing code.

## Key-terms


## Assignment

<ins>Exercise 1</ins>

- Create a new script.
- Copy the code below into your script.

    ```py
    a = 'int'
    b = 7
    c = False
    d = "18.5"
    ```

- Determine the data types of all four variables ( a, b, c, d) using a built-in function.
- Make a new variable x and give it the value b + d. Print the value of x. This will raise an error. Fix it so that print(x) prints a float.
- Write a comment above every line of code that tells the reader what is going on in your script.

<ins>Exercise 2</ins>

- Create a new script.
- Use the input() function to get input from the user. Store that input in a variable.
- Find out what data type the output of input() is. See if it is different for different kinds of input (numbers, words, etc.).


### Used sources
- [Python Data Types](https://www.w3schools.com/python/python_datatypes.asp)
- [Python Comments](https://www.w3schools.com/python/python_comments.asp)
- [Python User Input](https://www.w3schools.com/python/python_user_input.asp)

### Encountered problems
None

### Result

**<ins>Exercise 1</ins>**

Script --> [exercise1.py](/09_Python/includes/03_exercise1.py)

**- Determine the data types of all four variables ( a, b, c, d) using a built-in function.**

```py
a = 'int'
b = 7
c = False
d = "18.5"

print("a =", type(a))
print("b =", type(b))
print("c =", type(c))
print("d =", type(d))
```

![exercise1.py](/09_Python/includes/03_data-types_comments1-1.png)<br><br>

**- Make a new variable x and give it the value b + d. Print the value of x. This will raise an error. Fix it so that print(x) prints a float.**

```py
a = 'int'
b = 7
c = False
d = 18.5

print("a =", type(a))
print("b =", type(b))
print("c =", type(c))
print("d =", type(d))

x = b+d

print("x =", x)
```

![exercise1.py](/09_Python/includes/03_data-types_comments1-2.png)<br><br>

**- Write a comment above every line of code that tells the reader what is going on in your script.**

```py
# define variables
a = 'int'
b = 7
c = False
d = 18.5

# print variable type
print("a =", type(a))
print("b =", type(b))
print("c =", type(c))
print("d =", type(d))

# combine the sum of b and d in a new x variable
x = b+d

# print x
print("x =", x)
```

**<ins>Exercise 2</ins>**

Script --> [exercise2.py](/09_Python/includes/03_exercise2.py)

```py
#get user input and store them in variables
name = input("Enter name: ")
age = input("Enter age: ")
cloud_practitioner = input("Are you a certified Cloud Practitioner: ")
score_divided = input("Enter your score divided by 10: ")

# print user input + data type
print("Name:", name)
print("Variabel type:", type(name))
print("Age:", age)
print("Variabel type:", type(age))
print("Certified Cloud Practitioner:", cloud_practitioner)
print("Variabel type:", type(cloud_practitioner))
print("Score divided by 10:", score_divided)
print("Variabel type:", type(score_divided))
```

![exercise2.py](/09_Python/includes/03_data-types_comments2-1.png)<br><br>