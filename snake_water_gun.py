import random

# Computer chooses randomly
choices = ["snake", "water", "gun"]
computer = random.choice(choices)

# User input
user = input("Enter snake, water or gun: ").lower()

# Display computer choice
print("Computer chose:", computer)

# Decision making
if user == computer:
    print("Game Tie")

elif (user == "snake" and computer == "water") or \
     (user == "water" and computer == "gun") or \
     (user == "gun" and computer == "snake"):
    print("You Win")

else:
    print("You Lose")