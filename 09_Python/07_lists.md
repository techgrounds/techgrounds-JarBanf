# Lists
Lists are used to store multiple items in a single variable.

Lists are one of 4 built-in data types in Python used to store collections of data, the other 3 are Tuple, Set, and Dictionary, all with different qualities and usage.

Lists are created using square brackets.

## Key-terms

## Assignment

<ins>Exercise 1</ins>

- Create a new script.
- Create a variable that contains a list of five names.
- Loop over the list using a for loop. Print every individual name in the list on a new line.

<ins>Exercise 2</ins>

- Create a new script.
- Create a list of five integers.
- Use a for loop to do the following for every item in the list:
    - Print the value of that item added to the value of the next item in the list.
    - If it is the last item, add it to the value of the first item instead (since there is no next item).

### Used sources
- [Python Lists](https://www.w3schools.com/python/python_lists.asp)
- [Python - Loop Lists](https://www.w3schools.com/python/python_lists_loop.asp)
- []()

### Encountered problems
None

### Result

**<ins>Exercise 1</ins>**

Script --> [exercise1.py](/09_Python/includes/07_exercise1.py)

<ins>Loop Through a List</ins>  
You can loop through the list items by using a `for` loop.

```py
# list with 5 names
names = ["Jared", "Deniz", "Ahlaam", "Zuhair", "Salma"]

# print every name in the list "names"
for name in names:
    print(name)
```

![exercise1.py](/09_Python/includes/07_lists1.png)<br><br>

**<ins>Exercise 2</ins>**

Script --> [exercise2.py](/09_Python/includes/07_exercise2.py)

<ins>Loop Through the Index Numbers</ins>  
You can also loop through the list items by referring to their index number.

Use the `range()` and `len()` functions to create a suitable iterable.

```py
# list of 5 integers
integers = [3, 6, 23, 43, 50]

# loop through the list items by their index number
# from [0] - [last index]
for i in range(len(integers)):
    # if index number is NOT the last, 
    # current index value + next index value
    if i != (len(integers) - 1):
        print(integers[i]+integers[i+1])
    # else we have reached the last index
    # in this case, add last index value + first index value
    else:
        print(integers[i]+integers[i-i])
```

![exercise2.py](/09_Python/includes/07_lists2.png)<br><br>