# Task 1
def hello():
    return "Hello!"


# Task 2
def greet(name):
    return (f"Hello, {name}!")


# Task 3
def calc(a, b, operation="multiply"):

    if operation == "add":
        try:
            num1 = float(a)
            num2 = float(b)
            return num1 + num2
        except (ValueError, TypeError):
            return "You can't add those values!"
    elif operation == "subtract":
        try:
            num1 = float(a)
            num2 = float(b)
            return num1 - num2
        except (ValueError, TypeError):
            return "You can't subtract those values!"
    elif operation == "divide":
        try:
            num1 = float(a)
            num2 = float(b)
            return num1 / num2
        except (ValueError, TypeError):
            return "You can't divide those values!"
        except ZeroDivisionError:
            return "You can't divide by 0!"
    elif operation == "modulo":
        try:
            num1 = float(a)
            num2 = float(b)
            return num1 % num2
        except (ValueError, TypeError):
            return "You can't get the modulo of those values!"
    elif operation == "int_divide":
        try:
            num1 = float(a)
            num2 = float(b)
            return num1 // num2
        except (ValueError, TypeError):
            return "You can't perform integer division on those values!"
    elif operation == "power":
        try:
            num1 = float(a)
            num2 = float(b)
            return num1 ** num2
        except (ValueError, TypeError):
            return "You can't raise those values to a power!"
    elif operation == "multiply":
        try:
            num1 = float(a)
            num2 = float(b)
            return num1 * num2
        except (ValueError, TypeError):
            return "You can't multiply those values!"
        

# Task 4
def data_type_conversion(value, type):
    if type == "int":
        try:
            return int(value)
        except (ValueError, TypeError):
            return (f"You can't convert {value} into a {type}.")
    elif type == "float":
        try:
            return float(value)
        except (ValueError, TypeError):
            return (f"You can't convert {value} into a {type}.")
    elif type == "str":
        try:
            return str(value)
        except (ValueError, TypeError):
            return (f"You can't convert {value} into a {type}.")
    else:
        return (f"Invalid data type: {type}.")
    

# Task 5
def grade(*args):
    try:
        total = sum(args)
        count = len(args)
        average = total / count
    except (ValueError, TypeError):
        return "Invalid data was provided."

    if average >= 90:
        return "A"
    elif average >= 80 and average <= 89:
        return "B"
    elif average >= 70 and average <= 79:
        return "C"
    elif average >= 60 and average <= 69:
        return "D"
    elif average < 60:
        return "F"
    
# Task 6
def repeat(string, count):
    result = ""
    for i in range (count):
        result += string
    return result


# Task 7
def student_scores(action, **kwargs):
    if action == 'best':
        highest = max(kwargs.values())
        for name, score in kwargs.items():
            if score == highest:
                return name
    elif action == 'mean':
        total = sum(kwargs.values())
        count = len(kwargs)
        average = total / count
        return average


# Task 8
def titleize(string):
    words = string.split()
    capitalized_words = []

    short_words = ["a", "on", "an", "the", "of", "and", "is", "in"]

    for i, word in enumerate(words):
        if i == 0 or i == len(words) - 1:
            capitalized_words.append(word.capitalize())
        elif word in short_words:
            capitalized_words.append(word.lower())
        else:
            capitalized_words.append(word.capitalize())

    return " ".join(capitalized_words)


# Task 9
def hangman(secret, guess):
    guessed_letters = ""

    for letter in secret:
        if letter in guess:
            guessed_letters += letter
        else:
            guessed_letters += "_"
    return guessed_letters


# Task 10
def pig_latin(sentence):
    separated_words = sentence.split()
    pig_latin_words = []
    vowels = "aeiou"

    for word in separated_words:
        if word[0] in vowels:
            new_word = word + "ay"
            pig_latin_words.append(new_word)
        elif word.startswith("qu"):
            new_word = word[2:] + "quay"
            pig_latin_words.append(new_word)
        else:
            vowel_index = 0
            for i, letter in enumerate(word):
                if letter in vowels:
                    vowel_index = i
                    break
            consonants = word[:vowel_index]
            rest_of_word = word[vowel_index:]

            if rest_of_word.startswith("ua") or (vowel_index > 0 and word[vowel_index] == 'u' and word[vowel_index-1] == 'q'):
                vowel_index += 1
                consonants = word[:vowel_index]
                rest_of_word = word[vowel_index:]

            new_word = rest_of_word + consonants + "ay"
            pig_latin_words.append(new_word)

    return " ".join(pig_latin_words)