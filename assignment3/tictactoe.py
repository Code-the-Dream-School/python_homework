class TictactoeException(Exception):

    def __init__(self, message):
        self.message = message
        super().__init__(message)

class Board: 
    valid_moves = [
        "upper left", "upper middle", "upper right",
        "middle left", "center", "middle right",
        "lower left", "lower middle", "lower right"
    ]

    def __init__(self):
        self.board = [
            [" ", " ", " "],
            [" ", " ", " "],
            [" ", " ", " "]
        ]

        self.turn = "X"

    def __str__(self):
        return (
            f"{self.board[0][0]} | {self.board[0][1]} | {self.board[0][2]}\n"
            f"---------\n"
            f"{self.board[1][0]} | {self.board[1][1]} | {self.board[1][2]}\n"
            f"---------\n"
            f"{self.board[2][0]} | {self.board[2][1]} | {self.board[2][2]}"
        )

    def move(self, location):
        if location not in self.valid_moves:
            raise TictactoeException("Invalid move: " + location)

        positions = {
            "upper left": (0, 0),
            "upper middle": (0, 1),
            "upper right": (0, 2),
            "middle left": (1, 0),
            "center": (1, 1),
            "middle right": (1, 2),
            "lower left": (2, 0),
            "lower middle": (2, 1),
            "lower right": (2, 2)
        }

        row, col = positions[location]

        if self.board[row][col] != " ":
            raise TictactoeException("Cell already occupied: " + location)

        self.board[row][col] = self.turn
        self.turn = "O" if self.turn == "X" else "X"

    def whats_next(self):
        lines = [
            self.board[0],  # Row 1
            self.board[1],  # Row 2
            self.board[2],  # Row 3
            [self.board[0][0], self.board[1][0], self.board[2][0]],  # Column 1
            [self.board[0][1], self.board[1][1], self.board[2][1]],  # Column 2
            [self.board[0][2], self.board[1][2], self.board[2][2]],  # Column 3
            [self.board[0][0], self.board[1][1], self.board[2][2]],  # Diagonal \
            [self.board[0][2], self.board[1][1], self.board[2][0]]   # Diagonal /
        ]

        for line in lines:
            if line[0] != " " and line[0] == line[1] == line[2]:
                return (True, f"{line[0]} wins!")
        
        if all(cell != " " for row in self.board for cell in row):
            return (True, "Cat's game!")
            
        return (False, f"{self.turn}'s turn")


if __name__ == "__main__":
    game = Board()


    while True:
        print(game)

        game_over, message = game.whats_next()
        print(message)

        if game_over:
            break

        location = input("Enter your move: ").strip().lower()

        try:
            game.move(location)
        except TictactoeException as error:
            print(error.message)