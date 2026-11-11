class TictactoeException(Exception):

    def __init__(self, message):
        self.message = message
        super().__init__(message)

class Board: 
    valid_moves = [
        "top left", "top middle", "top right",
        "middle left", "middle middle", "middle right",
        "bottom left", "bottom middle", "bottom right"
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
            "top left": (0, 0),
            "top middle": (0, 1),
            "top right": (0, 2),
            "middle left": (1, 0),
            "middle middle": (1, 1),
            "middle right": (1, 2),
            "bottom left": (2, 0),
            "bottom middle": (2, 1),
            "bottom right": (2, 2)
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
                return f"{line[0]} wins!"
        
        if all(cell != " " for row in self.board for cell in row):
            return "Cat's game!"
            
        return f"{self.turn}'s turn"

game = Board()

while True:
    print(game)
    print(game.whats_next())

    if game.whats_next() in ["X wins!", "O wins!", "Cat's game!"]:
        break

    location = input("Enter your move: ").strip().lower()

    try:
        game.move(location)

    except TictactoeException as error:
        print(error.message)