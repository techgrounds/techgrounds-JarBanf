# import random module
import random

# function to generate computer hand
def compHand():
    ranNum = random.randrange(0,3)
    if ranNum == 0:
        return "rock"
    elif ranNum == 1:
        return "paper"
    else:
        return "scissors"

# function to get player hand
def playHand():
    plH = input("Choose (R)ock, (P)aper or (S)cissors: ")
    if plH == "R" or plH == "r" or plH == "Rock" or plH == "rock":
        return "rock"
    elif plH == "P" or plH == "p" or plH == "Paper" or plH == "paper":
        return "paper"
    elif plH == "S" or plH == "s" or plH == "Scissors" or plH == "scissors":
        return "scissors"
    else:
        return "invalid move"

# function to determine who wins
def whoWins(coH, plH):
    print("com chose: " + coH)
    print("player chose: " + plH)
    if coH == "rock":
        if plH == "rock":
            return "draw"
        elif plH == "paper":
            return "player"
        else:
            return "com"
    elif coH == "paper":
        if plH == "rock":
            return "com"
        elif plH == "paper":
            return "draw"
        else:
            return "player"
    elif coH == "scissors":
        if plH == "rock":
            return "player"
        elif plH == "paper":
            return "com"
        else:
            return "draw"
    else:
        print("error")

def play():
    coH = compHand()
    plH = playHand()
    winner = whoWins(coH, plH)
    print("Winner is: " + winner)

play()