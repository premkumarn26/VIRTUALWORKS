Rock Paper Scissors Game:

import random

# List of choices
choices = ["rock", "paper", "scissors"]

print("🎮 Welcome to Rock, Paper, Scissors!")
print("Type 'rock', 'paper', or 'scissors'.")

while True:
    # User input
    user_choice = input("\nEnter your choice: ").lower()

    # Validate input
    if user_choice not in choices:
        print("❌ Invalid choice! Please enter rock, paper, or scissors.")
        continue

    # Computer chooses randomly
    computer_choice = random.choice(choices)

    print(f"You chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")

    # Determine winner
    if user_choice == computer_choice:
        print("🤝 It's a Tie!")
    elif (
        (user_choice == "rock" and computer_choice == "scissors") or
        (user_choice == "paper" and computer_choice == "rock") or
        (user_choice == "scissors" and computer_choice == "paper")
    ):
        print("🎉 You Win!")
    else:
        print("💻 Computer Wins!")

    # Play again
    play_again = input("\nDo you want to play again? (yes/no): ").lower()

    if play_again != "yes":
        print("👋 Thanks for playing!")
        break
Output:

🎮 Welcome to Rock, Paper, Scissors!
Type 'rock', 'paper', or 'scissors'.

Enter your choice: rock
You chose: rock
Computer chose: scissors
🎉 You Win!

Do you want to play again? (yes/no): yes

Enter your choice: paper
You chose: paper
Computer chose: scissors
💻 Computer Wins!

Do you want to play again? (yes/no): no
👋 Thanks for playing!