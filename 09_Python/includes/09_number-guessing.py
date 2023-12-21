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