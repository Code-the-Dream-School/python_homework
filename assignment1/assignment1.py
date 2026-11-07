from turtle import title


def hello():
    return "Hello!"
def greet(name):
    return f"Hello, {name}!"

def calc(a, b, operation="multiply"):
    if operation == "add":
        return a + b
    elif operation == "subtract":
        return a - b
    elif operation == "multiply":
        try:
            return a * b
        except TypeError:
            return "You can't multiply those values!"
    elif operation == "divide":
        if b == 0:
            return "You can't divide by 0!"
        return a / b
    elif operation == "modulo":
        if b == 0:
            return "You can't divide by 0!"
        return a % b
    elif operation == "int_divide":
        if b == 0:
            return "You can't divide by 0!"
        return a // b
    elif operation == "power":
        return a ** b


def data_type_conversion(value, data_type):
    try:
        if data_type == "int":
            return int(value)
        elif data_type == "float":
            return float(value)
        elif data_type == "str":
            return str(value)
        elif data_type == "bool":
            return bool(value)
    except (ValueError, TypeError):
        return f"You can't convert {value} into a {data_type}."

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
    except (TypeError, ZeroDivisionError):
            return "Invalid data was provided."

def repeat(string, number):
    result = ""
    for i in range(number):
        result += string
    return result

def student_scores(mode, **kwargs):
    scores = list(kwargs.values())

    if not scores:
        return None

    if mode == "mean":
        return sum(scores) / len(scores)
    elif mode == "best":
        return max(kwargs, key=kwargs.get)


def titleize(title):
    small_words = {"a", "on", "an", "the", "of", "and", "is", "in"}
    words = title.split()

    for i, word in enumerate(words):
        if i != 0 and i != len(words) - 1 and word.lower() in small_words:
            words[i] = word.lower()
        else:
            words[i] = word.capitalize()

    return " ".join(words)

def hangman(secret, guess):
    result = ""

    for letter in secret:
        if letter in guess:
            result += letter
        else:
            result += "_"
    return result

def pig_latin(word):
    words = word.split()
    translated_words = []
    vowels = "aeiou"

    for current_word in words:
        lower_word = current_word.lower()

        if lower_word[0] in vowels:
            translated_words.append(current_word + "ay")
            continue

        if lower_word.startswith("squ"):
            translated_words.append(current_word[3:] + current_word[:3] + "ay")
            continue

        if lower_word.startswith("qu"):
            translated_words.append(current_word[2:] + current_word[:2] + "ay")
            continue

        if lower_word.startswith(("ch", "sh", "th", "wh", "ph")):
            translated_words.append(current_word[2:] + current_word[:2] + "ay")
            continue

        index = 0
        while index < len(current_word) and lower_word[index].lower() not in vowels:
            index += 1

        translated_words.append(current_word[index:] + current_word[:index] + "ay")
    return " ".join(translated_words)
        



    