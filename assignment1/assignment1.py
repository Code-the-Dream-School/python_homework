# Task 1: Hello
def hello():
    return "Hello!"


# Task 2: Greet with a Formatted String
def greet(name):
    return f"Hello, {name}!"


# Task 3: Calculator
def calc(a, b, operation="multiply"):
    try:
        match operation:
            case "add":
                return a + b
            case "subtract":
                return a - b
            case "multiply":
                return a * b
            case "divide":
                return a / b
            case "modulo":
                return a % b
            case "int_divide":
                return a // b
            case "power":
                return a ** b
            case _:
                return "Invalid operation"
    except ZeroDivisionError:
        return "You can't divide by 0!"
    except TypeError:
        return "You can't multiply those values!"


# Task 4: Data Type Conversion
def data_type_conversion(value, data_type):
    try:
        match data_type:
            case "int":
                return int(value)
            case "float":
                return float(value)
            case "str":
                return str(value)
            case _:
                return "Invalid data type"
    except ValueError:
        return f"You can't convert {value} into a {data_type}."


# Task 5: Grading System, Using *args
def grade(*args):
    try:
        avg = sum(args) / len(args)
        if avg >= 90:
            return "A"
        elif avg >= 80:
            return "B"
        elif avg >= 70:
            return "C"
        elif avg >= 60:
            return "D"
        else:
            return "F"
    except (TypeError, ZeroDivisionError):
        return "Invalid data was provided."


# Task 6: Use a For Loop with a Range
def repeat(string, count):
    result = ""
    for _ in range(count):
        result += string
    return result


# Task 7: Student Scores, Using **kwargs
def student_scores(mode, **kwargs):
    if mode == "best":
        return max(kwargs, key=kwargs.get)
    elif mode == "mean":
        return sum(kwargs.values()) / len(kwargs)
    else:
        return "Invalid mode"


# Task 8: Titleize, with String and List Operations
def titleize(text):
    little_words = {"a", "on", "an", "the", "of", "and", "is", "in"}
    words = text.split()
    result = [words[0].capitalize()] + [
        word if word in little_words else word.capitalize() for word in words[1:-1]
    ] + [words[-1].capitalize()]
    return " ".join(result)


# Task 9: Hangman, with more String Operations
def hangman(secret, guess):
    return "".join([char if char in guess else "_" for char in secret])


# Task 10: Pig Latin, String Manipulation
def pig_latin(text):
    def convert_word(word):
        vowels = 'aeiou'
        if word[0] in vowels:
            return word + 'ay'
        elif word.startswith('qu'):
            return word[2:] + 'quay'
        else:
            # Check for "qu" following a consonant, like "squash"
            for i in range(len(word)):
                if word[i] in vowels:
                    if word[i] == 'u' and i > 0 and word[i-1] == 'q':
                        return word[i+1:] + word[:i+1] + 'ay'
                    return word[i:] + word[:i] + 'ay'
            return word + 'ay'  # fallback if no vowel

    words = text.split()
    pig_latin_words = [convert_word(word) for word in words]
    return ' '.join(pig_latin_words)

