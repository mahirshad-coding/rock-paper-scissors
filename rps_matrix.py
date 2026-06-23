import random
choices = ["rock", "paper", "scissors"]
result = {
    ("rock", "rock"):"Tie",
    ("rock", "paper"):"You Lose",
    ("rock", "scissors"):"You Win",
    
    ("paper", "paper"):"Tie",
    ("paper", "rock"):"You Win",
    ("paper", "scissors"):"You Lose",
    
    ("scissors", "scissors"):"Tie",
    ("scissors", "rock"):"You Lose",
    ("scissors", "paper"):"You Win"
}
player = input("Enter rock, paper, or scissors: ").lower()
if player not in choices:
    print("Invalid Input")
else:
    computer = random.choice(choices)
    print("Computer chose :", computer)
    print(result[(player, computer)])
