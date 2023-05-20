import random

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("_" * 9)
        
def check_for_winner(board, player):
    for row in board:
        if all(x == player for x in row):
            return True
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False
    
def check_for_draw(board):
    return all(cell != " " for row in board for cell in row)

def play_human():
       
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ["X", "0"]

    print_board(board)
    game_on = True
    while game_on:
        for player in players:
            while True:
                try:
                    row, col = map(int, input(f"Player {player}: Pick a place on the board. Enter the row and column separated by a space: ").split())
                    if board[row-1][col -1] == " ":
                        board[row - 1][col - 1] = player
                        break
                    elif board[row-1][col -1] != " ":
                        print("That space is taken. Try again.")
                except(ValueError, IndexError):
                    print("This is not a valid entry. Enter numbers between 1 and 3 separated by a space.")
                    
            print_board(board)
            if check_for_winner(board, player):
                print(f"Player {player} wins!!!")
                return
            if check_for_draw(board):
                print("It's a draw!")
                return

def play_computer():
       
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ["X", "O"]

    print_board(board)
    game_on = True
    while game_on:
        for player in players:
            while True:
                try:
                    if player == "X":
                        row, col = map(int, input(f"Player {player}: Pick a place on the board. Enter the row and column separated by a space: ").split())
                    else:
                        while True:
                            computer_choice = f"{random.randint(1, 3)} {random.randint(1, 3)}"
                            row, col = map(int, computer_choice.split())
                            if board[row-1][col -1] == " ":
                                break
                        print(f"The computer chooses {computer_choice}")    
                    if board[row-1][col -1] == " ":
                        board[row - 1][col - 1] = player
                        break
                    elif board[row-1][col -1] != " ":
                        print("That space is taken. Try again.")
                except(ValueError, IndexError):
                    print("This is not a valid entry. Enter numbers between 1 and 3 separated by a space.")
                    
            print_board(board)
            if check_for_winner(board, player):
                if player == "X":
                    print("You win!!!")
                elif player == "O":
                    print("The computer won :(")
                return
            if check_for_draw(board):
                print("It's a draw!")
                return

while True:
    game_choice = input("Would you like to play another human or play the computer? Type 'human' or 'computer': ").lower()
    if game_choice == "human":
        play_human()
        break
    elif game_choice == "computer":
        play_computer()
        break
    else:
        print("That is not a valid choice.")