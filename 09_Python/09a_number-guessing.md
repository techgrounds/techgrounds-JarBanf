# Number guessing
It's time to build something.

## Key-terms

## Assignment

- Generate a random number between 1 and 100 (or any other range).
- The player guesses a number. For every wrong answer the player receives a clue.
- When the player guesses the right number, display a score.

### Used sources
- [Python While Loops](https://www.w3schools.com/python/python_while_loops.asp)

### Encountered problems
None

### Result

Script --> [number-guessing.py](/09_Python/includes/09a_number-guessing.py)

```py
# import random module
import random

# generate random number from 1 to 100
randomNumber = random.randrange(1, 101)

# ask player to input number
playerNumber = int(input("Guess a number from 1 to 100: "))

# set player score to 0
playerScore = 0


while playerNumber != randomNumber:
    # player number not correct
    if playerNumber < randomNumber:
        # player number is lower than random number
        # give clue
        print("Nope, higher!")
    else:
        # player number is higher than random number
        # give clue
        print("Nope, lower!")
    # add 1 to score
    playerScore += 1
    # ask player to guess again
    playerNumber = int(input("Guess again: "))
else:
    # player has guessed correctly
    # add 1 to score
    playerScore += 1
    print("Congratulations, you got it!")
    print("Winning number was " + str(randomNumber))
    print("Your score is " + str(playerScore))
```

![number guessing](/09_Python/includes/09a_number-guessing1.png)<br>

![number guessing](/09_Python/includes/09a_number-guessing2.png)<br>

![number guessing](/09_Python/includes/09a_number-guessing3.png)<br>