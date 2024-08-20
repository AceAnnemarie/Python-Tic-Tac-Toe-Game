def print_board(board):
    """Print the game board."""
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board, player):
    """Check if the given player has won."""
    # Check rows and columns
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or \
           all(board[j][i] == player for j in range(3)):
            return True

    # Check diagonals
    if all(board[i][i] == player for i in range(3)) or \
       all(board[i][2 - i] == player for i in range(3)):
        return True

    return False

def is_draw(board):
    """Check if the game is a draw."""
    return all(board[row][col] != ' ' for row in range(3) for col in range(3))

def tic_tac_toe():
    """Play the Tic-Tac-Toe game."""
    while True:
        board = [[' ' for _ in range(3)] for _ in range(3)]
        players = ['X', 'O']
        turn = 0

        for _ in range(9):
            print_board(board)
            print(f"Player {players[turn]}'s turn")

            try:
                row, col = map(int, input("Enter row and column (0-2): ").split())
                if not (0 <= row < 3 and 0 <= col < 3):
                    print("Indices out of range. Please enter values between 0 and 2.")
                    continue
            except ValueError:
                print("Invalid input. Please enter integers only.")
                continue

            if board[row][col] == ' ':
                board[row][col] = players[turn]
                if check_winner(board, players[turn]):
                    print_board(board)
                    print(f"Player {players[turn]} wins!")
                    break
                if is_draw(board):
                    print_board(board)
                    print("It's a draw!")
                    break
                turn = 1 - turn
            else:
                print("Cell already taken. Try again.")
        
        play_again = input("Do you want to play again? (yes/no): ").strip().lower()
        if play_again != 'yes':
            print("Thanks for playing! Goodbye.")
            break

if __name__ == "__main__":
    tic_tac_toe()
