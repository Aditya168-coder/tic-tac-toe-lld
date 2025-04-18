def create_board():
    return [['-' for _ in range(3)] for _ in range(3)]

def display_board(board):
    print("\nCurrent board:")
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def make_move(board, row, col, symbol):
    if 0 <= row < 3 and 0 <= col < 3 and board[row][col] == '-':
        board[row][col] = symbol
        return True
    return False

def check_winner(board, symbol):
    
    for i in range(3):
        if all(board[i][j] == symbol for j in range(3)) or \
           all(board[j][i] == symbol for j in range(3)):
            return True
    
    if all(board[i][i] == symbol for i in range(3)) or \
       all(board[i][2 - i] == symbol for i in range(3)):
        return True
    return False

def is_board_full(board):
    return all(cell != '-' for row in board for cell in row)

def switch_turn(current_symbol):
    return 'O' if current_symbol == 'X' else 'X'

def get_player_name(symbol, player1, player2):
    return player1 if symbol == 'X' else player2

def play_game():
    player1 = input("Enter Player 1 name (X): ")
    player2 = input("Enter Player 2 name (O): ")
    board = create_board()
    current_symbol = 'X'

    print("\nWelcome to Tic Tac Toe!")
    display_board(board)

    while True:
        player = get_player_name(current_symbol, player1, player2)
        print(f"\n{player}'s turn ({current_symbol}):")
        try:
            row = int(input("Enter row (0-2): "))
            col = int(input("Enter col (0-2): "))
        except ValueError:
            print("Invalid input. Please enter integers only.")
            continue

        if make_move(board, row, col, current_symbol):
            display_board(board)

            if check_winner(board, current_symbol):
                print(f"\n{player} wins!")
                break
            elif is_board_full(board):
                print("\nIt's a draw!")
                break

            current_symbol = switch_turn(current_symbol)
        else:
            print("Invalid move. Cell already taken or out of bounds.")

# Run the game
if __name__ == "__main__":
    play_game()
