# Task1
def hello():
    return "Hello!"


hello()  # Write your code here.


# Task2
def greet(name):
    return f"Hello, {name}!"


greet("Anna")


# Task3
def calc(a, b, operation="multiply"):
    try:
        if operation == "add":
            return a + b
        elif operation == "subtract":
            return a - b
        elif operation == "multiply":
            return a * b
        elif operation == "divide":
            return a / b
        elif operation == "modulo":
            return a % b
        elif operation == "int_divide":
            return a // b
        elif operation == "power":
            return a**b
        else:
            return "Unknown operation"
    except ZeroDivisionError:
        return "You can't divide by 0!"
    except TypeError as e:
        return "You can't multiply those values!"


print(calc("hello", "world", "multiply"))
print(calc(10, 5))
print(calc("5", "2", "add"))
print(calc(5, 2, "add"))
print(calc(10, 2, "int_divide"))
print(calc(2, 3, "power"))
print(calc(2, 0, "divide"))


# Task4
def data_type_conversion(value, type):
    try:
        if type == "int":
            return int(value)
        elif type == "float":
            return float(value)
        elif type == "str":
            return str(value)
        else:
            return f"Unknown data type: {type}"
    except (ValueError, TypeError):
        return f"You can't convert {value} into a {type}."


print(data_type_conversion("abc", "int"))
print(data_type_conversion("123.45", "float"))
print(data_type_conversion(123, "str"))


# Task5
def grade(*args):
    try:
        if not all(isinstance(score, (int, float)) for score in args):
            raise ValueError("Non-numeric input detected")

        average = sum(args) / len(args)
    except (ValueError, TypeError, ZeroDivisionError):
        return "Invalid data was provided."

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


print(grade())
print(grade(100, 95, 80))
print(grade(50, 70, "0"))


# Task6
def repeat(string, count):
    result = ""
    for _ in range(count):
        result += string
    return result


print(repeat("ho", 3))


# Task7
def student_scores(param, **kwargs):
    if not kwargs:
        return "No student scores provided."
    if param == "best":
        return max(kwargs, key=kwargs.get)
    elif param == "mean":
        average = sum(kwargs.values()) / len(kwargs)
        return average
    else:
        return "Invalid mode. Use 'best' or 'mean'."


print(student_scores("best", Anna=95, Maria=92, Viktoria=88))
print(student_scores("mean", Andrew=85, Brad=82, Dan=78))


# Task8
def titleize(str):
    little = {"a", "on", "an", "the", "of", "and", "is", "in"}
    words = str.lower().split()

    if not words:
        return ""

    result = []

    for i, word in enumerate(words):
        if i == 0 or i == len(words) - 1:
            result.append(word.capitalize())
        elif word in little:
            result.append(word)
        else:
            result.append(word.capitalize())

    return " ".join(result)


print(titleize("anna bazileeva"))
print(titleize("national aeronautics and space administration"))


# Task9
def hangman(secret, guess):
    secret_word = ""
    for letter in secret:
        if letter in guess:
            secret_word += letter
        else:
            secret_word += "_"
    return secret_word


print((hangman("hosanna", "oa")))
print(hangman("hosanna", "hn"))


# Task10
def pig_latin(text):
    vowels = "aeiou"

    def convert(word):
        if word[0] in vowels:
            return word + "ay"

        if word.startswith("qu"):
            return word[2:] + "quay"

        i = 0
        while i < len(word):
            if word[i] in vowels:
                break
            if word[i] == "q" and i + 1 < len(word) and word[i + 1] == "u":
                i += 2
                break
            i += 1

        return word[i:] + word[:i] + "ay"

    return " ".join(convert(w) for w in text.split())


print(pig_latin("hello"))
print(pig_latin("aqua"))
print(pig_latin("kumquat"))
