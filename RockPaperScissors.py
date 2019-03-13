#string.lower()变成小写
import random
choices=["rock","paper","scissors"]
your_choice = input("Please choose Rock/Paper/Scissors:  ")
your_choice= your_choice.lower()

while your_choice !="quit" :
    computer_choice = random.choice(choices)
    print("Your choice is :" + your_choice+" and the computer's choice is :" + computer_choice)
    if your_choice != computer_choice:
        if your_choice ==  'rock':
            if computer_choice == "paper":
                print("Computer Win")
            else:
                print("You win")
        if your_choice ==  'paper':
            if computer_choice == "rock":
                print("You Win")
            else:
                print("Computer win")
        if your_choice ==  'scissors':
            if computer_choice == "paper":
                print("You Win")
            else:
                print("Computer win")
    else:
        print("It's a tie")
    print()
    your_choice = input("Please choose Rock/Paper/Scissors:  ")
        
        
    
