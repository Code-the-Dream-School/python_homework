import csv
import logging
import math

# ======================================================================
# Task 1: Writing and Testing a Decorator
# ======================================================================
# one time setup
logger = logging.getLogger(__name__ + "_parameter_log")
logger.setLevel(logging.INFO)
logger.addHandler(logging.FileHandler("./decorator.log", "a"))


def logger_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        logger.log(logging.INFO, f"function: {func.__name__}")
        logger.log(logging.INFO, f"positional parameters: {list(args) if args else 'none'}")
        logger.log(logging.INFO, f"keyword parameters: {kwargs if kwargs else 'none'}")
        logger.log(logging.INFO, f"return: {result}")
        logger.log(logging.INFO, "")
        return result
    return wrapper


@logger_decorator
def say_hello():
    print("Hello, World!")


@logger_decorator
def positional_args(*args):
    return True


@logger_decorator
def keyword_args(**kwargs):
    return logger_decorator


def run_task1():
    say_hello()
    positional_args(1, 2, "three")
    keyword_args(name="Ada", language="Python")
    print("Done. Check decorator.log for the results.")


# ======================================================================
# Task 2: A Decorator that Takes an Argument
# ======================================================================
def type_converter(type_of_output):
    def decorator(func):
        def wrapper(*args, **kwargs):
            x = func(*args, **kwargs)
            return type_of_output(x)
        return wrapper
    return decorator


@type_converter(str)
def return_int():
    return 5


@type_converter(int)
def return_string():
    return "not a number"


def run_task2():
    y = return_int()
    print(type(y).__name__)  # This should print "str"
    try:
        y = return_string()
        print("shouldn't get here!")
    except ValueError:
        print("can't convert that string to an integer!")  # This is what should happen


# ======================================================================
# Task 3: List Comprehensions Practice
# ======================================================================
def run_task3():
    with open("../csv/employees.csv", newline="") as f:
        reader = csv.reader(f)
        rows = [row for row in reader]

    header = rows[0]
    first_idx = header.index("first_name")
    last_idx = header.index("last_name")

    # Skip the heading row
    names = [row[first_idx] + " " + row[last_idx] for row in rows[1:]]
    print(names)

    # Only names containing the letter "e"
    names_with_e = [name for name in names if "e" in name]
    print(names_with_e)


# ======================================================================
# Task 4: Closure Practice
# ======================================================================
def make_hangman(secret_word):
    guesses = []

    def hangman_closure(letter):
        guesses.append(letter)
        display = "".join(ch if ch in guesses else "_" for ch in secret_word)
        print(display)
        return all(ch in guesses for ch in secret_word)

    return hangman_closure


def run_task4():
    secret = input("Enter the secret word: ").strip().lower()
    print("\n" * 50)  # scroll the secret off the screen
    game = make_hangman(secret)
    done = False
    while not done:
        guess = input("Guess a letter: ").strip().lower()
        if len(guess) != 1:
            print("Please enter exactly one letter.")
            continue
        done = game(guess)
    print("You got it!")


# ======================================================================
# Task 5: Extending a Class
# ======================================================================
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __str__(self):
        return f"Point({self.x}, {self.y})"

    def distance(self, other):
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)


class Vector(Point):
    def __str__(self):
        return f"Vector < {self.x}, {self.y} >"

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)


def run_task5():
    p1 = Point(1, 2)
    p2 = Point(4, 6)
    p3 = Point(1, 2)
    print(p1, p2)
    print("p1 == p2:", p1 == p2)
    print("p1 == p3:", p1 == p3)
    print("distance p1 to p2:", p1.distance(p2))

    v1 = Vector(1, 2)
    v2 = Vector(3, 4)
    print(v1, v2)
    print("v1 == v2:", v1 == v2)
    print("v1 + v2 =", v1 + v2)
    print("distance v1 to v2:", v1.distance(v2))


# ======================================================================
# Task 6: More on Classes (Tic-Tac-Toe)
# ======================================================================
class TictactoeException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(message)


class Board:
    valid_moves = ["upper left", "upper center", "upper right", "middle left", "center", "middle right", "lower left", "lower center", "lower right"]

    def __init__(self):
        self.board_array = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
        self.turn = "X"

    def __str__(self):
        lines=[]
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
        row = move_index // 3 # row
        column = move_index % 3 #column
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
                else:
                    continue
                break
            else:
                continue
            break
        if (cat):
            return (True, "Cat's Game.")
        win = False
        for i in range(3): # check rows
            if self.board_array[i][0] != " ":
                if self.board_array[i][0] == self.board_array[i][1] and self.board_array[i][1] == self.board_array[i][2]:
                    win = True
                    break
        if not win:
            for i in range(3): # check columns
                if self.board_array[0][i] != " ":
                    if self.board_array[0][i] == self.board_array[1][i] and self.board_array[1][i] == self.board_array[2][i]:
                        win = True
                        break
        if not win:
            if self.board_array[1][1] != " ": # check diagonals
                if self.board_array[0][0] ==  self.board_array[1][1] and self.board_array[2][2] == self.board_array[1][1]:
                    win = True
                if self.board_array[0][2] ==  self.board_array[1][1] and self.board_array[2][0] == self.board_array[1][1]:
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


def run_task6():
    board = Board()
    print(board)
    game_over = False
    while not game_over:
        print(f"{board.turn}'s turn. Valid moves: {', '.join(Board.valid_moves)}")
        move = input("Your move: ").strip().lower()
        try:
            board.move(move)
        except TictactoeException as e:
            print(e.message)
            continue
        print(board)
        game_over, message = board.whats_next()
        print(message)


# ======================================================================
# Mainline: choose which task to run
# ======================================================================
if __name__ == "__main__":
    tasks = {"1": run_task1, "2": run_task2, "3": run_task3,
             "4": run_task4, "5": run_task5, "6": run_task6}
    while True:
        choice = input("\nRun which task (1-6, or q to quit)? ").strip().lower()
        if choice == "q":
            break
        if choice in tasks:
            print(f"\n--- Task {choice} ---")
            tasks[choice]()
        else:
            print("Please enter a number from 1 to 6, or q.")
