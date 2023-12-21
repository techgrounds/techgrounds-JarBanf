# Key-value pairs
Dictionaries are used to store data values in key:value pairs. A dictionary is a collection which is ordered, changeable and do not allow duplicates. Dictionaries are written with curly brackets, and have keys and values.

## Key-terms

## Assignment

<ins>Exercise 1</ins>

- Create a new script.
- Create a dictionary with the following keys and values:
    | Key | Value |
    |---|---|
    | First name | Casper |
    | Last name | Velzen |
    | Job title | Learning coach |
    | Company | Techgrounds |

- Loop over the dictionary and print every key-value pair in the terminal.

<ins>Exercise 2</ins>

- Create a new script.
- Use user input to ask for their information (first name, last name, job title, company). Store the information in a dictionary.
- Write the information to a csv file (comma-separated values). The data should not be overwritten when you run the script multiple times.

### Used sources
- [Python Dictionaries](https://www.w3schools.com/python/python_dictionaries.asp)

### Encountered problems
None

### Result

**<ins>Exercise 1</ins>**

Script --> [exercise1.py](/09_Python/includes/08_exercise1.py)

```py
# create dictionary with key:values
dict = {
    "First name": "Casper",
    "Last name": "Velzen",
    "Job title": "Learning coach",
    "Company": "Techgrounds"
}

# loop through both keys and values
for x, y in dict.items():
    print(x + ": " + y)
```

![exercise1.py](/09_Python/includes/08_keyvalue-pairs1.png)<br><br>

**<ins>Exercise 2</ins>**

Script --> [exercise2.py](/09_Python/includes/08_exercise2.py)

```py

```

![exercise2.py](/09_Python/includes/08_keyvalue-pairs2.png)<br><br>