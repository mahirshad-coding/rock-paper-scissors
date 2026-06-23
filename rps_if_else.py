import random
choices = ["rock", "paper", "scissors"]
player = input("Player, please enter your choice: rock, paper, or scissors").lower()
computer = random.choice(choices)
print("Computer chose", computer)

if player == computer:
    print("It's a tie")
elif player == "rock" and computer == "paper":
    print("You Lose")
elif player == "paper" and computer == "scissors":
    print("You Lose")
elif player == "scissors" and computer == "rock":
    print("You Lose")
elif player in choices:
    print("You Win")
else:
    print("Invalid Input")
