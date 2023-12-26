# import random module
import random

# function to determine how many rounds to be played
def detRounds():
    rounds = int(input("How many rounds do you want to play? Choose uneven number."))
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
    print("Round winner determined")
    return roundWinner

# function to play round
def playRound(playRounds, curRound):
    print("Round " + str(curRound + 1) + " out of " + str(playRounds))
    print("FIGHT!")
    plH = playHand()
    coH = compHand()
    roundWinner = whoWinsRound(coH, plH)
    print("Winner round " + str(curRound + 1) + " is: " + roundWinner)
    return roundWinner

# function to keep score
def keepScore(scores, roundWinner):
    if roundWinner == "com":
        print("comScore + 1")
        scores[1] +=1
    elif roundWinner == "player":
        print("playScore + 1")
        scores[0] += 1
    elif roundWinner == "draw":
        print("It's a draw, no point for anyone")
    print("Player : " + str(scores[0]))
    print("Computer : " + str(scores[1]))
    return scores

def whoWinsGame(scores):
    gameWinner = ""
    if scores[0] < scores[1]:
        gameWinner = "Computer wins the game!"
    elif scores[0] > scores[1]:
        gameWinner = "Player wins the game!"
    else:
        gameWinner = "The game ended in a draw!"

    return gameWinner

# function to initialise game    
def playGame():
    playRounds = detRounds()
    scores = [0,0] # [player, computer]
    curRound = 0
    while playRounds != curRound:
        roundWinner = playRound(playRounds, curRound)
        scores = keepScore(scores, roundWinner)
        curRound += 1
        print("Round " + str(curRound) + " ended.")
    gameWinner = whoWinsGame(scores)
    print(gameWinner)

playGame()