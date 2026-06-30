Number Guessing Game :

import random


secret_number = random.randint(1, 100)

print(" Welcome to the Number Guessing Game!")
print("I have selected a number between 1 and 100.")
print("Try to guess it!")

attempts = 0

while True:
    try:
        guess = int(input("Enter your guess: "))
        attempts += 1

        if guess < secret_number:
            print("Too Low! Try again.")
        elif guess > secret_number:
            print("Too High! Try again.")
        else:
            print(f" Congratulations! You guessed the number in {attempts} attempts.")
            break

    except ValueError:
        print("Please enter a valid integer.")

Output:

🎮 Welcome to the Number Guessing Game!
I have selected a number between 1 and 100.
Try to guess it!

Enter your guess: 50
Too Low! Try again.

Enter your guess: 75
Too High! Try again.

Enter your guess: 63
Too Low! Try again.

Enter your guess: 68
🎉 Congratulations! You guessed the number in 4 attempts.
