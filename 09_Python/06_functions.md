# Functions
A function is a block of code which only runs when it is called. You can pass data, known as parameters, into a function. A function can return data as a result.

## Key-terms


## Assignment

<ins>Exercise 1</ins>

- Create a new script.
- Import the random package.
- Print 5 random integers with a value between 0 and 100.

<ins>Exercise 2</ins>

- Create a new script.
- Write a custom function myfunction() that prints “Hello, world!” to the terminal. Call myfunction.
- Rewrite your function so that it takes a string as an argument. Then, it should print “Hello, NAME!”.

<ins>Exercise 3</ins>

- Create a new script.

- Copy the code below into your script.

    ```py
    def avg():
    # write your code here
    # you are not allowed to edit any code below here

    x = 128
    y = 255
    z = avg(x,y)

    print("The average of",x,"and",y,"is",z)
    ```
- Write the custom function avg() so that it returns the average of the given parameters. You are not allowed to edit any code below the second comment.

### Used sources
- [Python Functions](https://www.w3schools.com/python/python_functions.asp)
- [Python Modules](https://www.w3schools.com/python/python_modules.asp)
- [Python Random Module](https://www.w3schools.com/python/module_random.asp)
- [Python Random randrange() Method](https://www.w3schools.com/python/ref_random_randrange.asp)

### Encountered problems
None

### Result

**<ins>Exercise 1</ins>**

<ins>Python Modules</ins>  
Consider a module to be the same as a code library. A file containing a set of functions you want to include in your application.

<ins>Random Module</ins>  
Python has a built-in module that you can use to make random numbers.

<ins>Python Random randrange() Method</ins>  
The `randrange()` method returns a randomly selected element from the specified range.

`random.randrange(start, stop, step)`
- `start`: Optional. An integer specifying at which position to start.
Default 0
- `stop`: Required. An integer specifying at which position to end.
- `step`: Optional. An integer specifying the incrementation.
Default 1

Script --> [exercise1.py](/09_Python/includes/06_exercise1.py)

```py
# import the random module
import random

# define variabel
i = 0

# print 5 random integers between 0 and 100
while i < 5:
    print(random.randrange(1,100))
    i += 1
```

![exercise1.py](/09_Python/includes/06_functions1.png)<br><br>

**<ins>Exercise 2</ins>**

Script --> [exercise2.py](/09_Python/includes/06_exercise2.py)

```py

```

**<ins>Exercise 3</ins>**

Script --> [exercise3.py](/09_Python/includes/06_exercise3.py)

```py

```