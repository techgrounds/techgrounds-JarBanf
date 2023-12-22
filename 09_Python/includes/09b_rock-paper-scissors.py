# import random module
import random

# function to determine how many rounds to be played
def detRounds():
    rounds = int(input("How many rounds do you want to play? 3, 5 or 7? "))
    print("Rounds to play: " + str(rounds))
    return rounds

# function to get player hand
def playHand():
    result = ""
    plH = input("Choose (R)ock, (P)aper or (S)cissors: ")
    if plH == "R" or plH == "r" or plH == "Rock" or plH == "rock":
        result = "rock"
    elif plH == "P" or plH == "p" or plH == "Paper" or plH == "paper":
        result = "paper"
    elif plH == "S" or plH == "s" or plH == "Scissors" or plH == "scissors":
        result = "scissors"
    print("player chose: " + result)
    return result

# function to generate computer hand
def compHand():
    result = ""
    ranNum = random.randrange(0,3)
    if ranNum == 0:
        result = "rock"
    elif ranNum == 1:
        result = "paper"
    else:
        result = "scissors"
    print("com chose: " + result)
    return result

# function to determine who wins
def whoWinsRound(coH, plH):
    roundWinner = ""
    if coH == "rock":
        if plH == "rock":
            roundWinner = "draw"
        elif plH == "paper":
            roundWinner = "player"
        elif plH == "scissors":
            roundWinner = "com"
    elif coH == "paper":
        if plH == "rock":
            roundWinner = "com"
        elif plH == "paper":
            roundWinner =  "draw"
        elif plH == "scissors":
            roundWinner = "player"
    elif coH == "scissors":
        if plH == "rock":
            roundWinner =  "player"
        elif plH == "paper":
            roundWinner =  "com"
        elif plH == "scissors":
            roundWinner = "draw"
    print("Round winner is: " + roundWinner)
    return roundWinner

# function to play round
def playRound():
    plH = playHand()
    coH = compHand()
    roundWinner = whoWinsRound(coH, plH)
    print("Round played")
    return roundWinner

# function to keep score
def keepScore(playScore, comScore, roundWinner):
    scores = [playScore, comScore]
    if roundWinner == "com":
        comScore +=1
    elif roundWinner == "player":
        playScore += 1
    elif roundWinner == "draw":
        comScore += 0
        playScore += 0
    print("Score is: " + scores + "[player, com]")
    return scores

def whoWinsGame(rounds, scores):
    return

def announceWinner(gameWinner):
    print("Game winner is: " + gameWinner)


def playGame():
    rounds = detRounds()
    playScore = 0
    comScore = 0
    roundWinner = playRound()
    scores = keepScore(playScore, comScore, roundWinner)

    gameWinner = whoWinsGame(rounds, scores)
    announceWinner(gameWinner)

playRound()
##playGame()