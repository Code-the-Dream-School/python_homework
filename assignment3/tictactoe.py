class TictactoeException(Exception):
    pass

class Board:
    def __init__(self):
        self.board_array = [[" "]*3 for _ in range(3)]
        self.turn = "X"
        self.moves_map = {
            "upper left": (0, 0), "upper center": (0, 1), "upper right": (0, 2),
            "middle left": (1, 0), "center": (1, 1), "middle right": (1, 2),
            "lower left": (2, 0), "lower center": (2, 1), "lower right": (2, 2),
        }

    def __str__(self):
        rows = []
        for row in self.board_array:
            rows.append(" " + " | ".join(row) + " ")
        return "\n-----------\n".join(rows)

    def move(self, position):
        if position not in self.moves_map:
            raise TictactoeException("That's not a valid move.")
        row, col = self.moves_map[position]
        if self.board_array[row][col] != " ":
            raise TictactoeException("That spot is taken.")
        self.board_array[row][col] = self.turn

    def switch_turn(self):
        self.turn = "O" if self.turn == "X" else "X"

    def check_winner(self):
        # Check rows and columns
        for i in range(3):
            if self.board_array[i][0] == self.board_array[i][1] == self.board_array[i][2] != " ":
                return True
            if self.board_array[0][i] == self.board_array[1][i] == self.board_array[2][i] != " ":
                return True
        # Check diagonals
        if self.board_array[0][0] == self.board_array[1][1] == self.board_array[2][2] != " ":
            return True
        if self.board_array[0][2] == self.board_array[1][1] == self.board_array[2][0] != " ":
            return True
        return False

    def board_full(self):
        return all(cell != " " for row in self.board_array for cell in row)

    def whats_next(self):
        if self.check_winner():
            return True, f"Player {self.turn} wins!"
        elif self.board_full():
            return True, "Cat's Game."
        else:
            self.switch_turn()
            return False, f"{self.turn}'s turn."

def main():
    print("Welcome to Tic Tac Toe!\n")
    board = Board()
    print(board)
    
    while True:
        move = input(f"{board.turn}'s move: ").strip().lower()
        try:
            board.move(move)
            print("\n" + str(board))
            game_over, message = board.whats_next()
            print(message)
            if game_over:
                break
        except TictactoeException as e:
            print("Error:", e)

    print("Thanks for playing!")

if __name__ == "__main__":
    main()
