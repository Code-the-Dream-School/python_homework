# assignment1.py

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
                return None  # or raise an error, but test likely won't call with invalid op
    except ZeroDivisionError:
        return "You can't divide by 0!"
    except TypeError:
        return "You can't multiply those values!"


# Task 4: Data Type Conversion
def data_type_conversion(value, dtype):
    try:
        if dtype == "float":
            return float(value)
        elif dtype == "str":
            return str(value)
        elif dtype == "int":
            return int(value)
        else:
            # Invalid dtype - not specified how to handle, maybe just return None
            return None
    except (ValueError, TypeError):
        return f"You can't convert {value} into a {dtype}."


# Task 5: Grading System, Using *args
def grade(*args):
    try:
        avg = sum(args) / len(args)
    except Exception:
        return "Invalid data was provided."

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


# Task 6: Use a For Loop with a Range
def repeat(string, count):
    result = ""
    for _ in range(count):
        result += string
    return result


# Task 7: Student Scores, Using **kwargs
def student_scores(best_or_mean, **kwargs):
    if best_or_mean == "best":
        # Return the name with the highest score
        best_student = max(kwargs, key=kwargs.get)
        return best_student
    elif best_or_mean == "mean":
        # Return average of scores
        if len(kwargs) == 0:
            return 0  # Avoid division by zero
        avg_score = sum(kwargs.values()) / len(kwargs)
        return avg_score
    else:
        return None


# Task 8: Titleize, with String and List Operations
def titleize(string):
    little_words = {"a", "on", "an", "the", "of", "and", "is", "in"}

    words = string.split()
    if not words:
        return ""

    result_words = []

    for i, word in enumerate(words):
        if i == 0 or i == len(words) - 1:
            # Always capitalize first and last word
            result_words.append(word.capitalize())
        else:
            if word.lower() in little_words:
                result_words.append(word.lower())
            else:
                result_words.append(word.capitalize())

    return " ".join(result_words)


# Task 9: Hangman, with more String Operations
def hangman(secret, guess):
    result = ""
    for letter in secret:
        if letter in guess:
            result += letter
        else:
            result += "_"
    return result


# Task 10: Pig Latin, Another String Manipulation Exercise
def pig_latin(sentence):
    vowels = "aeiou"

    def convert_word(word):
        # Special "qu" case
        if word.startswith("qu"):
            return word[2:] + "quay"
        # Starts with vowel
        if word[0] in vowels:
            return word + "ay"
        # Starts with consonants (move leading consonants to the end)
        else:
            # Find index where first vowel occurs or "qu" occurs
            index = 0
            while index < len(word) and word[index] not in vowels:
                # special qu check inside consonant cluster
                if word[index:index+2] == "qu":
                    index += 2
                    break
                index += 1
            return word[index:] + word[:index] + "ay"

    words = sentence.split()
    converted_words = [convert_word(w) for w in words]
    return " ".join(converted_words)


# For your testing, you can uncomment below:
# print(hello())
# print(greet("Alice"))
# print(calc(10, 0, "divide"))
# print(data_type_conversion("abc", "float"))
# print(grade(90, 80, 70))
# print(repeat("ha", 3))
# print(student_scores("best", Alice=90, Bob=80))
# print(titleize("the lord of the rings"))
# print(hangman("alphabet", "ab"))
# print(pig_latin("quiet queen apple"))


