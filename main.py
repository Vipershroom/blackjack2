from Person import Person

def getPlayers():
    print("How many players?")
    amount = int(input())
    playerList = []
    
    for i in range(amount):
        print(f"What is player {i + 1}'s name")
        name = input()
        playerList.append(Person(name, []))
    return playerList

print("Welcome to Blackjack")

