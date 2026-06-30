Tic Tac Toe Game:

# Tic Tac Toe Game

# Create the board
board = [" " for _ in range(9)]

# Function to display the board
def display_board():
    print()
    print(board[0], "|", board[1], "|", board[2])
    print("--+---+--")
    print(board[3], "|", board[4], "|", board[5])
    print("--+---+--")
    print(board[6], "|", board[7], "|", board[8])
    print()

# Function to check winner
def check_winner(player):
    win_conditions = [
        [0,1,2], [3,4,5], [6,7,8],   # Rows
        [0,3,6], [1,4,7], [2,5,8],   # Columns
        [0,4,8], [2,4,6]             # Diagonals
    ]

    for condition in win_conditions:
        if (board[condition[0]] == player and
            board[condition[1]] == player and
            board[condition[2]] == player):
            return True
    return False

# Function to check draw
def check_draw():
    return " " not in board

# Main Game
current_player = "X"

while True:
    display_board()

    try:
        move = int(input(f"Player {current_player}, enter position (1-9): ")) - 1

        if move < 0 or move > 8:
            print("Invalid position! Choose between 1 and 9.")
            continue

        if board[move] != " ":
            print("Position already taken! Try again.")
            continue

        board[move] = current_player

        if check_winner(current_player):
            display_board()
            print(f"🎉 Player {current_player} Wins!")
            break

        if check_draw():
            display_board()
            print("🤝 It's a Draw!")
            break

        # Switch player
        if current_player == "X":
            current_player = "O"
        else:
            current_player = "X"

    except ValueError:
        print("Please enter a valid number.")

print("Game Over!")

Output:

Player X, enter position (1-9): 1
Player O, enter position (1-9): 5
Player X, enter position (1-9): 2
Player O, enter position (1-9): 8
Player X, enter position (1-9): 3

🎉 Player X Wins!
Game Over!