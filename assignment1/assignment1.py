def hello():
    return "Hello!"

def greet(name):
    return f"Hello, {name}!"

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
            return a ** b

    except ZeroDivisionError:
        return "You can't divide by 0!"

    except TypeError:
        return "You can't multiply those values!"

def data_type_conversion(value, data_type):

    try:

        if data_type == "float":
            return float(value)

        elif data_type == "str":
            return str(value)

        elif data_type == "int":
            return int(value)

    except ValueError:
        return f"You can't convert {value} into a {data_type}."

def grade(*args):

    try:
        average = sum(args) / len(args)
        if average >= 90:
            return "A"

        elif 90 > average >= 80:
            return "B"

        elif 80 > average >= 70:
            return "C"

        elif 70 > average >= 60:
            return "D"

        else:
            return "F"

    except TypeError:
        return "Invalid data was provided."

def repeat(string, count):

    var = ""

    for i in range(count):
        var += string
    
    return var

def student_scores(command, **kwargs):
    
    if command == "mean":
        return sum(kwargs.values()) / len(kwargs.values())

    elif command == "best":

        best_score = 0
        best_student = ""

        for key, value in kwargs.items():

            if value > best_score:
                best_score = value
                best_student = key

        return best_student

def titleize(title):

    words = title.split()
    little_words = ["a", "on", "an", "the", "of", "and", "is", "in"]

    for i, word in enumerate(words):

        if i == 0:
            words[i] = word.capitalize()

        elif i == len(words) - 1:
            words[i] = word.capitalize()

        elif word in little_words:
            words[i] = word

        else:
            words[i] = word.capitalize()

    return " ".join(words)

def hangman(secret, guess):
    
    answer = ""

    for letter in secret:

        if letter in guess:
            answer = answer + letter

        else:
            answer = answer + "_"

    return answer

def pig_latin(sentence):

    vowels = "aeiou"
    words = sentence.split()
    translated_words = []

    for word in words:

        if word[0] in vowels:
            translated_words.append(word + "ay")

        else:
            consonants = ""
            rest_of_word = word

            while len(rest_of_word) > 0 and rest_of_word[0] not in vowels:

                if rest_of_word.startswith("qu"):
                    consonants = consonants + "qu"
                    rest_of_word = rest_of_word[2:]
                    break
                
                else:
                    consonants = consonants + rest_of_word[0]
                    rest_of_word = rest_of_word[1:]

            translated_words.append(rest_of_word + consonants + "ay")

    return " ".join(translated_words)



