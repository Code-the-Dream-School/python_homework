class TictactoeException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


class Board:
    valid_moves = ["upper left", "upper center", "upper right",
                   "middle left", "center", "middle right",
                   "lower left", "lower center", "lower right"]

    def __init__(self):
        self.board_array = [[" " for _ in range(3)] for _ in range(3)]
        self.turn = "X"

    def __str__(self):
        lines = []
        lines.append(f" {self.board_array[0][0]} | {self.board_array[0][1]} | {self.board_array[0][2]} \n")
        lines.append("-----------\n")
        lines.append(f" {self.board_array[1][0]} | {self.board_array[1][1]} | {self.board_array[1][2]} \n")
        lines.append("-----------\n")
        lines.append(f" {self.board_array[2][0]} | {self.board_array[2][1]} | {self.board_array[2][2]} \n")
        return "".join(lines)

    def move(self, move_string):
        if not move_string in Board.valid_moves:
            raise TictactoeException("That's not a valid move.")
        move_index = Board.valid_moves.index(move_string)
        row = move_index // 3
        column = move_index % 3
        if self.board_array[row][column] != " ":
            raise TictactoeException("That spot is taken.")
        self.board_array[row][column] = self.turn
        if self.turn == "X":
            self.turn = "O"
        else:
            self.turn = "X"

    def whats_next(self):
        cat = True
        for i in range(3):
            for j in range(3):
                if self.board_array[i][j] == " ":
                    cat = False
                    break
            else:
                continue
            break

        if cat:
            return (True, "Cat's Game.")

        win = False
        for i in range(3):
            if self.board_array[i][0] != " ":
                if self.board_array[i][0] == self.board_array[i][1] and self.board_array[i][1] == self.board_array[i][2]:
                    win = True
                    break

        if not win:
            for i in range(3):
                if self.board_array[0][i] != " ":
                    if self.board_array[0][i] == self.board_array[1][i] and self.board_array[1][i] == self.board_array[2][i]:
                        win = True
                        break

        if not win:
            if self.board_array[1][1] != " ":
                if self.board_array[0][0] == self.board_array[1][1] and self.board_array[2][2] == self.board_array[1][1]:
                    win = True
                if self.board_array[0][2] == self.board_array[1][1] and self.board_array[2][0] == self.board_array[1][1]:
                    win = True

        if not win:
            if self.turn == "X":
                return (False, "X's turn.")
            else:
                return (False, "O's turn.")
        else:
            if self.turn == "O":
                return (True, "X wins!")
            else:
                return (True, "O wins!")


def play_game():
    board = Board()
    print("Welcome to Tic-Tac-Toe!")
    print("Valid moves are: " + ", ".join(Board.valid_moves))

    while True:
        print("\nCurrent board:")
        print(board)

        game_over, message = board.whats_next()
        if game_over:
            print(message)
            break

        print(message)
        move = input("Enter your move: ").strip().lower()

        try:
            board.move(move)
        except TictactoeException as e:
            print(f"Invalid move: {e}")


if __name__ == "__main__":
    play_game()