import random
import os


def drawCard():
    return random.randint(1,21)

def turns(player):
    print(f"Hello, {player.name}")
    if player.cards == []:
        player.cards.append(drawCard())
        player.cards.append(drawCard())
    print(player.cards)

def game(playerList):
    for i in playerList:
        turns(i)