import random
import os


def drawCard():
    randnum = random.randint(1,11)
    if randnum == 11:
        print("You rolled an ace. Do you want it to act as 1 or 11?")
        ans = input()
        if ans == "11":
            return 11
        else:
            return 1
    return randnum

def turns(player):
    print(f"Hello, {player.name}")
    
    if player.cards == []:
        player.cards.append(drawCard())
        player.cards.append(drawCard())
        
    cardSum = sum(player.cards)
    
    print(f"Your cards are {player.cards}\nThe sum is {cardSum}")
    print("Would you like to {draw} or {hold?}")
    
    while True:
        ans = input()
        if ans == "draw":
            player.cards.append(drawCard())
            print(f"Your cards are {player.cards}\nThe sum is {cardSum}")
            print("Press enter to continue") 
            input()
        break
    os.system("cls")
    print("It is now time for the next players turn.\nOnce they have been seated you may press enter")
    input()
    os.system('cls')
    
def dealerTurn(player):
    pass

def game(playerList):
    while True:
        for i in playerList:
            if i.name == "Dealer":
                dealerTurn(i)
            else:
                turns(i)