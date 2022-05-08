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
    print(player.cards)

def game(playerList):
    for i in playerList:
        turns(i)