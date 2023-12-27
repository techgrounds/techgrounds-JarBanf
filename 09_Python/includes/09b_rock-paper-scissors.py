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