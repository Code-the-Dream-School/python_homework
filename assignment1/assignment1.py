# Task 1
def hello():
    return "Hello!"


# Task 2
def greet(name):
    return f"Hello, {name}!"


# Task 3
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
    except ZeroDivisionError:
        return "You can't divide by 0!"
    except TypeError:
        return "You can't multiply those values!"


# Task 4
def data_type_conversion(value, data_type):
    try:
        match data_type:
            case "float":
                return float(value)
            case "int":
                return int(value)
            case "str":
                return str(value)
    except ValueError:
        return f"You can't convert {value} into a {data_type}."


# Task 5
def grade(*args):
    try:
        average = sum(args) / len(args)

        if average >= 90:
            return "A"
        elif average >= 80:
            return "B"
        elif average >= 70:
            return "C"
        elif average >= 60:
            return "D"
        else:
            return "F"
    except Exception:
        return "Invalid data was provided."


# Task 6
def repeat(text, count):
    result = ""
    for _ in range(count):
        result += text
    return result


# Task 7
def student_scores(option, **kwargs):
    if option == "best":
        best_student = max(kwargs, key=kwargs.get)
        return best_student
    elif option == "mean":
        return sum(kwargs.values()) / len(kwargs.values())


# Task 8
def titleize(text):
    little_words = ["a", "on", "an", "the", "of", "and", "is", "in"]
    words = text.split()

    for i, word in enumerate(words):
        if i == 0 or i == len(words) - 1:
            words[i] = word.capitalize()
        elif word in little_words:
            words[i] = word.lower()
        else:
            words[i] = word.capitalize()

    return " ".join(words)


# Task 9
def hangman(secret, guess):
    result = ""

    for letter in secret:
        if letter in guess:
            result += letter
        else:
            result += "_"

    return result


# Task 10
def pig_latin(text):
    vowels = "aeiou"
    words = text.split()
    result = []

    for word in words:
        if word[0] in vowels:
            result.append(word + "ay")
        else:
            index = 0
            while index < len(word) and word[index] not in vowels:
                if word[index:index+2] == "qu":
                    index += 2
                    break
                index += 1
            result.append(word[index:] + word[:index] + "ay")

    return " ".join(result)
