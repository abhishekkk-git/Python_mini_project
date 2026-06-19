import random

choices = ["Stone", "Paper", "Scissor"]
you, comp = 0, 0
round = 1

while round <= 5:
    u = input(f"Round {round} - Enter Stone/Paper/Scissor: ")
    if u not in choices:
        print("Invalid value Please Try again.")
        continue

    c = random.choice(choices)
    print(f"Computer: {c}")

    if u == c:
        print("Tie!")
    elif (u=="Stone" and c=="Scissor") or (u=="Paper" and c=="Stone") or (u=="Scissor" and c=="Paper"):
        print("You Win!") ; you += 1
    else:
        print("Computer Wins!") ; comp += 1

    print(f"Score → You:{you} | Comp:{comp}\n")
    round += 1

print("FINAL:", "You Win!" if you > comp else "Computer Wins!" if comp > you else "Draw!")    