import os
import random

def game():

    print "WELCOME TO BLACKJACK"
    Cards = [1,2,3,4,5,6,7,8,9,10,11,12,13,14]
    computerHand = deal()
    playerHand = deal()

    print "-------START GAME-------"
    print "Computer Hand: " + str(computerHand[0])
    print "Player Hand: " + str(playerHand)

    print "\n-------Current Score-----"
    if(computeScore(playerHand) == 21):
        print "21! You win!"
        message()
    elif(computeScore(computerHand) == 21):
        print "21! Computer Wins!"
        message()
    print computeScore(playerHand)
    cardHit = raw_input("Do you want to hit (Y/N): ")
    while(cardHit == "y" or cardHit == "Y" ):
        hit(playerHand)

        print "\n------NEW HAND SCORE------"
        print playerHand
        print computeScore(playerHand)

        if(len(playerHand) == 5 and computeScore(playerHand) < 21):
            print "Less than 5 and Under 21:  YOU WIN "
            message()
        elif(bust(playerHand) == 1):
            print "BUST. You lose"
            message()
        else:
            cardHit = raw_input("Do you want to hit (Y/N): ")

    print "\n-------Computer Turn------"
    if(computeStrategy(computerHand) == "Hit"):
        hit(computerHand)
        print computerHand
    else:
        print "I'm done."
        print computerHand

    print "\n--------DETERMINE WINNER------"
    print "COMPUTER: " + str(computeScore(computerHand))
    print "PLAYER  : " + str(computeScore(playerHand))

    if(winner(computerHand,playerHand) == "hand1" and bust(computerHand)==0):
       print "Computer won"

    elif(winner(computerHand,playerHand) == "hand2" and bust(playerHand) == 1):
       print "Computer won"

    elif(winner(computerHand,playerHand) == "hand1" and bust(computerHand) == 1):
       print "Player Won"

    elif(winner(computerHand,playerHand) == "hand2" and bust(playerHand) == 0):
       print "Player Won"

    message()


def message():
    again = raw_input("Do you want to play again? (Y/N) : ")
    if(again == "Y" or again == "y"):
        game()
    else:
        print "\n\n-------Thank you for playing!--------\n\n"
        exit()


'''
Seeing as though this is a simple 2 player game, the deck size wouldn't matter
and the chance of drawing the same card 3 or more times is low, I thought this
simple implementation would suffice.
'''
def deal():
    random1 = random.randint(1,14)
    random2 = random.randint(1,14)

    if (random1 == 11):random1 = "J"
    if (random1 == 12):random1 = "Q"
    if (random1 == 13):random1 = "K"
    if (random1 == 14):random1 = "A"

    if (random2 == 11):random2 = "J"
    if (random2 == 12):random2 = "Q"
    if (random2 == 13):random2 = "K"
    if (random2 == 14):random2 = "A"

    hand = [random1,random2]
    return hand


def computeScore(hand):
    total = 0
    for cards in hand:
        if cards == "J" or cards == "Q" or cards == "K":
            total+= 10
        elif cards == "A":
            if total == 11: total+= 1
            else:total+= 11
        else:
            total += cards

    return total

def hit(hand):
    newCard = random.randint(1,14)

    if (newCard == 11):newCard = "J"
    if (newCard == 12):newCard = "Q"
    if (newCard == 13):newCard = "K"
    if (newCard == 14):newCard = "A"

    hand.append(newCard)

    return hand

# A very conservative rule
def computeStrategy(hand):
    strategy = ""
    if (computeScore(hand) > 15): strategy = "Stay"
    if (computeScore(hand) <=15): strategy =  "Hit"

    return strategy

def winner(hand1,hand2):
    score1 = computeScore(hand1)
    score2 = computeScore(hand2)

    if score1 > 21: return "hand2"
    if score2 > 21: return "hand1"

    if(score1 > score2): return "hand1"
    else: return "hand2"

def bust(hand):
    if computeScore(hand) >= 21:
        return 1
    else:
        return 0

if __name__ == '__main__':
    game()
