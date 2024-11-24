import random;

#declare variables to be used
words = ['rock', 'paper', 'scissors']

#generate a random choice between 1, 2, and 3
randomChoice = random.choice(words)
print("Make your choice:")
choice = input()

def rpsgame():
    print(randomChoice)
    if(choice == randomChoice):
        print("It's a tie!")
    elif(choice == "rock" and randomChoice == "scissors"):
        print("You win!")
    elif(choice == "paper" and randomChoice == "rock"):
        print("You win!")
    elif(choice == "scissors" and randomChoice == "paper"):
        print("You win!")
    elif(choice == "rock" and randomChoice == "paper"):
        print("You lose!")
    elif(choice == "paper" and randomChoice == "scissors"):
        print("You lose!")
    elif(choice == "scissors" and randomChoice == "rock"):
        print("You lose!")

#function to play the game
def play():
    if (choice == "rock" or choice == "paper" or choice == "scissors"):
        rpsgame()
    else:
        print("Invalid choice! Please choose 'rock', 'paper', or'scissors'.")

play()