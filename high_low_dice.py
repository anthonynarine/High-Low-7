# https://www.youtube.com/watch?v=yr_rbMoT7lU&list=PLmzkEJ1Zz_uYmscN0lBdS9rvRrQC-bdv_
"""
This game will roll two dice and you will place 1 of 3 bets.
High, low, or Seven until you decide to quit or you've lost all your money'"""

from random import randint

cash = 100
bet = 5

while True:
    print ("\n----------------------------------")
    print ("Place your bet or enter X to exit")
    print ("1) High roll bets of 8-12 pays out x 2")
    print ("2) Low  roll bets of 2-6  pays out x 2") 
    print ("3) 7    roll bets         pays out x 3")
    print (f"Cash on hand: {cash}")
    print ("----------------------------------")
    choice = input("Make your choice: ")

    #first time we do is check if the user wants to exit the game
    if choice == 'x' or choice == "X":
        print("Thanks for playing and hope to see you again")
        break
    #next we check the users bet
    elif choice == "1" or choice == "2" or choice == "3":
        roll = randint(1, 6) + randint (1, 6)
        print (f"You rolled a: {roll}")

        if roll > 7 and choice == "1":
            print("winner!")
            cash += bet
        elif roll < 7 and choice == "2":
            print("winner!")
            cash += (2 * bet) 
        elif roll == 7 and choice == "3":
            print("winner!")
            cash += bet
        else:
            print ("House wins")
            cash -= bet
    else:
        print ("Enter a valid choice!")
        continue

