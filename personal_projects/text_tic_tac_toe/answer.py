def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board, player):
    for row in board:
        if all([cell == player for cell in row]):
            return True
    for col in range(3):
        if all([board[row][col] == player for row in range(3)]):
            return True
    if all([board[i][i] == player for i in range(3)]) or all([board[i][2 - i] == player for i in range(3)]):
        return True
    return False

def is_full(board):
    return all([cell != " " for row in board for cell in row])

def main():
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ["X", "O"]

    print_board(board)
    while True:
        for player in players:
            while True:
                try:
                    row, col = map(int, input(f"Player {player}, enter your move (row, col): ").split())
                    if board[row - 1][col - 1] == " ":
                        board[row - 1][col - 1] = player
                        break
                    else:
                        print("The cell is already taken. Try again.")
                except (ValueError, IndexError):
                    print("Invalid input. Enter numbers between 1 and 3, separated by a space.")

            print_board(board)
            if check_winner(board, player):
                print(f"Player {player} wins!")
                return
            if is_full(board):
                print("It's a draw!")
                return

if __name__ == "__main__":
    main()
