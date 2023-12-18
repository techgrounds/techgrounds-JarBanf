# Loops

Python has two primitive loop commands:

<ins>`while` loops</ins>  
With the while loop we can execute a set of statements as long as a condition is true.

<ins>`for` loops</ins>  
A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).

With the for loop we can execute a set of statements, once for each item in a list, tuple, set etc.

## Key-terms


## Assignment

<ins>Exercise 1</ins>  

- Create a new script.
- Create a variable x and give it the value 0.
- Use a while loop to print the value of x in every iteration of the loop. After printing, the value of x should increase by 1. The loop should run as long as x is smaller than or equal to 10.

<ins>Exercise 2</ins>

- Create a new script.
- Copy the code below into your script.

    ```py
    for i in range(10):
    # do something here
    ```

- Print the value of i in the for loop. You did not manually assign a value to i. Figure out how its value is determined.
- Add a variable x with value 5 at the top of your script.
- Using the for loop, print the value of x multiplied by the value of i, for up to 50 iterations.

<ins>Exercise 3</ins>

- Create a new script.
- Copy the array below into your script.

    ```py
    arr = ["Shikha", "Casper", "Bart", "Ruben", "Ulviye"]
    ```

- Use a for loop to loop over the array. Print every name individually.

### Used sources
- [Python While Loops](https://www.w3schools.com/python/python_while_loops.asp)
- [Python For Loops](https://www.w3schools.com/python/python_for_loops.asp)
- [Python range() Function](https://www.w3schools.com/python/ref_func_range.asp)

### Encountered problems
None

### Result

**<ins>Exercise 1</ins>**

Script --> [exercise1.py](/09_Python/includes/04_exercise1.py)

```py
# define variable
x = 0

#while x is smaller than or equal to 10, it will print the value of x.
while x <= 10:
    print(x)
    x += 1 # x + 1
```

![exercise1.py](/09_Python/includes/04_loops1.png)<br><br>

**<ins>Exercise 2</ins>**

Script --> [exercise2.py](/09_Python/includes/04_exercise2.py)


**- Print the value of i in the for loop. You did not manually assign a value to i. Figure out how its value is determined.**

```py
for i in range(10):
    print(i)
```

![exercise2-1.py](/09_Python/includes/04_loops2-1.png)<br>
 
The `range()` function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and stops before a specified number.

Syntax: `range(start, stop, step)`
- `start`: Optional. An integer number specifying at which position to start. Default is 0.
- `stop`: Required. An integer number specifying at which position to stop (not included).
- `step`: Optional. An integer number specifying the incrementation. Default is 1.

**- Add a variable x with value 5 at the top of your script. Using the for loop, print the value of x multiplied by the value of i, for up to 50 iterations.**

```py
# define variable
x = 5

# print x * i for 50 iterations (i = 0, i = 1, ..., i = 49)
for i in range(50):
    print(x*i)
```

![exercise2-2.py](/09_Python/includes/04_loops2-2.png)<br><br>

**<ins>Exercise 3</ins>**

Script --> [exercise3.py](/09_Python/includes/04_exercise3.py)

```py
# define list
arr = ["Shikha", "Casper", "Bart", "Ruben", "Ulviye"]

#print every name in list arr
for i in arr:
    print(i)
```

![exercise3.py](/09_Python/includes/04_loops3.png)<br><br>