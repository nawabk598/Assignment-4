import random

choices = ["rock", "paper", "scissors"]

print("Rock, Paper, Scissors Game!")
print("Type rock, paper, or scissors.")

while True:
    player = input("Your choice: ").lower()

    if player not in choices:
        print("Please type rock, paper, or scissors.")
        continue

    computer = random.choice(choices)
    print("Computer chose:", computer)

    if player == computer:
        print("It's a tie!")
    elif (player == "rock" and computer == "scissors") or \
         (player == "paper" and computer == "rock") or \
         (player == "scissors" and computer == "paper"):
        print("You win!")
    else:
        print("You lose!")

    again = input("Play again? (yes/no): ")
    if again.lower() != "yes":
        print("Thanks for playing!")
        break
