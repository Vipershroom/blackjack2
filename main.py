from Person import Person
from game import game


def getPlayers():
    print("How many players?")
    amount = int(input())
    playerList = []
    
    for i in range(amount):
        print(f"What is player {i + 1}'s name")
        name = input()
        playerList.append(Person(name, []))
    
    if amount == 1:
        print("You will be facing the dealer")
    
    return playerList

if __name__ == "__main__":
    print("Welcome to Blackjack")
    game(getPlayers())
