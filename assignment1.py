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
                return "Unknown operation"
    except ZeroDivisionError:
        return "You can't divide by 0!"
    except Exception:
        return "You can't multiply those values!"

# Task 4: Data Type Conversion
def data_type_conversion(value, dtype):
    try:
        match dtype:
            case "int":
                return int(value)
            case "float":
                return float(value)
            case "str":
                return str(value)
            case _:
                return "Invalid type"
    except Exception:
        return f"You can't convert {value} into a {dtype}."

# Task 5: Grading System Using *args
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
    except Exception:
        return "Invalid data was provided."

# Task 6: Repeat with For Loop and Range
def repeat(string, count):
    result = ""
    for _ in range(count):
        result += string
    return result

# Task 7: Student Scores Using **kwargs
def student_scores(method, **kwargs):
    if not kwargs:
        return None

    if method == "best":
        return max(kwargs, key=kwargs.get)
    elif method == "mean":
        return sum(kwargs.values()) / len(kwargs)
    else:
        return None

# Task 8: Titleize
def titleize(text):
    little_words = {"a", "on", "an", "the", "of", "and", "is", "in"}
    words = text.split()
    title = []

    for i, word in enumerate(words):
        if i == 0 or i == len(words) - 1 or word not in little_words:
            title.append(word.capitalize())
        else:
            title.append(word)
    return " ".join(title)

# Task 9: Hangman
def hangman(secret, guess):
    result = ""
    for letter in secret:
        if letter in guess:
            result += letter
        else:
            result += "_"
    return result

# Task 10: Pig Latin
def pig_latin(text):
    words = text.split()
    result = []

    for word in words:
        if word.startswith("qu"):
            result.append(word[2:] + "quay")
        elif word[0] in "aeiou":
            result.append(word + "ay")
        else:
            for i, letter in enumerate(word):
                if letter in "aeiou":
                    result.append(word[i:] + word[:i] + "ay")
                    break
    return " ".join(result)


# OPTIONAL: Manual Testing (Can comment out later)
if __name__ == "__main__":
    print(hello())                               # Task 1
    print(greet("Gedam"))                        # Task 2
    print(calc(10, 5, "add"))                    # Task 3
    print(data_type_conversion("123", "int"))    # Task 4
    print(grade(90, 80, 70))                     # Task 5
    print(repeat("Go!", 3))                      # Task 6
    print(student_scores("best", Alice=88, Bob=92))  # Task 7
    print(titleize("a tale of two cities"))      # Task 8
    print(hangman("alphabet", "ab"))             # Task 9
    print(pig_latin("quiet apple banana"))       # Task 10
