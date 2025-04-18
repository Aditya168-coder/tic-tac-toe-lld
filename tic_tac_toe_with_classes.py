class Player:
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol


class GameBoard:
    def __init__(self):
        self.board = [['-' for _ in range(3)] for _ in range(3)]

    def display(self):
        print("\nCurrent board:")
        for row in self.board:
            print(" | ".join(row))
            print("-" * 9)

    def make_move(self, row, col, symbol):
        if 0 <= row < 3 and 0 <= col < 3 and self.board[row][col] == '-':
            self.board[row][col] = symbol
            return True
        return False

    def is_full(self):
        return all(cell != '-' for row in self.board for cell in row)

    def check_winner(self, symbol):
        for i in range(3):
            if all(self.board[i][j] == symbol for j in range(3)) or \
               all(self.board[j][i] == symbol for j in range(3)):
                return True
        if all(self.board[i][i] == symbol for i in range(3)) or \
           all(self.board[i][2 - i] == symbol for i in range(3)):
            return True
        return False


class TicTacToe:
    def __init__(self):
        self.player1 = Player(input("Enter Player 1 name (X): "), 'X')
        self.player2 = Player(input("Enter Player 2 name (O): "), 'O')
        self.board = GameBoard()
        self.current_player = self.player1

    def switch_turn(self):
        self.current_player = self.player1 if self.current_player == self.player2 else self.player2

    def play(self):
        print("\nWelcome to Tic Tac Toe!")
        self.board.display()

        while True:
            print(f"\n{self.current_player.name}'s turn ({self.current_player.symbol}):")
            try:
                row = int(input("Enter row (0-2): "))
                col = int(input("Enter col (0-2): "))
            except ValueError:
                print("Invalid input. Please enter integers only.")
                continue

            if self.board.make_move(row, col, self.current_player.symbol):
                self.board.display()

                if self.board.check_winner(self.current_player.symbol):
                    print(f"\n{self.current_player.name} wins!")
                    break
                elif self.board.is_full():
                    print("\nIt's a draw!")
                    break

                self.switch_turn()
            else:
                print("Invalid move. Cell already taken or out of bounds.")


# Entry point
if __name__ == "__main__":
    game = TicTacToe()
    game.play()
