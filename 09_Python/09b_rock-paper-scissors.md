# Rock Paper Scissors
It's time to build something.

## Key-terms

## Assignment

- The player plays against a computer opponent typing either a letter (rps) or an entire word (rock paper scissors) to play their move.
- Create a function that checks whether the move is valid or not.
- Create another function to create a computer move.
- Create another function to check who wins the round.
- Finally, create a function that keeps track of the score.
- The game should be played in a predetermined number of rounds.

### Used sources
- [How to Check if the String is Integer in Python](https://favtutor.com/blogs/check-string-is-integer-python)

### Encountered problems
None

### Result

Script --> [rock-paper-scissors.py](/09_Python/includes/09b_rock-paper-scissors.py)

```py
# import random module
import random

# function to determine how many rounds to be played
def detRounds():
    print()
    rounds = input("How many rounds do you want to play? Choose uneven number. ")
    while rounds.isdigit() != True:
        # player did not input a number, ask again
        rounds = input("Please choose a NUMBER! ")
    print() # create empty line
    return int(rounds)

# function to get player hand
def playHand():
    result = ""
    plH = input("Choose your weapon. (R)ock, (P)aper or (S)cissors: ")
    if plH == "R" or plH == "r" or plH == "Rock" or plH == "rock":
        result = "rock"
    elif plH == "P" or plH == "p" or plH == "Paper" or plH == "paper":
        result = "paper"
    elif plH == "S" or plH == "s" or plH == "Scissors" or plH == "scissors":
        result = "scissors"
    else:
        # player didn't choose correctly
        print("Weapon does not exist. Your going in empty handed.")
        result = "to be stupid"
    print("Player chose: " + result)
    return result

# function to generate computer hand
def compHand():
    result = ""
    # generate random number
    # from 0 to 2
    ranNum = random.randrange(0,3)
    if ranNum == 0:
        result = "rock"
    elif ranNum == 1:
        result = "paper"
    else:
        result = "scissors"
    print("Computer chose: " + result)
    return result

# function to determine who wins round
def whoWinsRound(coH, plH):
    roundWinner = ""
    if coH == "rock":
        if plH == "rock":
            roundWinner = "draw"
        elif plH == "paper":
            roundWinner = "player"
        elif plH == "scissors":
            roundWinner = "com"
        else:
            # player didn't choose correctly
            roundWinner = "com"
    elif coH == "paper":
        if plH == "rock":
            roundWinner = "com"
        elif plH == "paper":
            roundWinner =  "draw"
        elif plH == "scissors":
            roundWinner = "player"
        else:
            # player didn't choose correctly
            roundWinner = "com"
    elif coH == "scissors":
        if plH == "rock":
            roundWinner =  "player"
        elif plH == "paper":
            roundWinner =  "com"
        elif plH == "scissors":
            roundWinner = "draw"
        else:
            # player didn't choose correctly
            roundWinner = "com"
    return roundWinner

# function to play round
def playRound(playRounds, curRound):
    print("Round " + str(curRound + 1) + " out of " + str(playRounds))
    print("FIGHT!")
    plH = playHand() # get player hand
    coH = compHand() # get computer hand
    roundWinner = whoWinsRound(coH, plH) # determine who wins the round
    print("Winner round " + str(curRound + 1) + " is: " + roundWinner)
    return roundWinner

# function to keep score
def keepScore(scores, roundWinner):
    if roundWinner == "com":
        scores[1] +=1
    elif roundWinner == "player":
        scores[0] += 1
    elif roundWinner == "draw":
        print("It's a draw, no point for anyone")
    print("Player: " + str(scores[0]))
    print("Computer: " + str(scores[1]))
    print() #create empty line
    return scores

# function to decide who wins game
def whoWinsGame(scores):
    gameWinner = ""
    if scores[0] < scores[1]:
        gameWinner = "Computer wins the game!"
    elif scores[0] > scores[1]:
        gameWinner = "Player wins the game!"
    else:
        gameWinner = "The game ended in a draw. You both lose!"
    return gameWinner

# function to initialise game    
def playGame():
    playRounds = detRounds() # get rounds to play from player
    scores = [0,0] # [player, computer]
    curRound = 0
    while curRound < playRounds:
        # play rounds until determined round is reached
        roundWinner = playRound(playRounds, curRound) # play round
        scores = keepScore(scores, roundWinner) # keep score
        curRound += 1 # mark round as played
    # all rounds are done
    gameWinner = whoWinsGame(scores) # who wins?
    print(gameWinner)

playGame()
```

Example of a played game.

![rock paper scissors](/09_Python/includes/09b_rock-paper-scissors1.png)<br><br>

Example of when player does not input a number as round.

![rock paper scissors](/09_Python/includes/09b_rock-paper-scissors2.png)<br><br>

Example of when player does not enter a valid form of "Rock", "Paper" or "Scissors".

![rock paper scissors](/09_Python/includes/09b_rock-paper-scissors3.png)<br><br>