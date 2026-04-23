# Task 1: Hello
def hello():
    return "Hello!"

print(hello())  

#Task 2: Greet with a Formatted String
def greet(name):
    return (f"Hello, {name}!")

print(greet("Risqua"))

print("Go to the next Task-3")

#Task 3 : Calculator 
def calc(a, b, operation="multiply"):
    try:
        if operation == "add":
            return a + b
        elif operation == "subtract":
            return a - b
        elif operation == "multiply":
            return a * b
        elif operation == "modulo":
            return a % b
        elif operation == "divide":
            return a / b
        elif operation == "int_divide":
            return a // b
        elif operation == "power":
            return a ** b
        else:
            return "Invalid operation"
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed"
    except (TypeError, ValueError):
        return "You can't multiply those values!"
    
    
print(calc(10, 5, "subtract"))
print(calc(10, 5, "multiply"))
print(calc(10, 5, "divide"))
print(calc(10, 0, "divide"))
print(calc(10, 5, "power"))

print("Go to the next Task-4")
    
    # Task 4: Data Type Conversion
def convert_to_string(value, data_type):
    try:
        if data_type == "int":
            return int(value)
        elif data_type == "float":
            return float(value)
        elif data_type == 'str':
            return str(value)
        else:
            return (f"Invalid data type requested: {data_type}")
    except (ValueError, TypeError):
        return (f"You can't convert {value} into a {data_type}.")
print(convert_to_string(123, "int"))
print(convert_to_string(3.14, "float")) 
print(convert_to_string(123, "str"))
print(convert_to_string("abc", "int"))

#Task 5: Grading System, Using *args
def grade(*args):
    try:
        
        if len(args) == 0:
            return "Invalid data was provided."
        
        # average
        avg = sum(args) / len(args)

        
        if avg >= 90:
            return 'A'
        elif avg >= 80:
            return 'B'
        elif avg >= 70:
            return 'C'
        elif avg >= 60:
            return 'D'
        else:
            return 'F'

    except (TypeError, ValueError):
        return "Invalid data was provided."
    
print(grade(95, 85, 92))
print(grade(75, 80, 78))

#Task 6: Use a For Loop with a Range
def repeat(text, count):
    result = ""

    for i in range(count):
        result +=text

    return result

print(repeat("Hello", 5))
 
 #Task 7: Student Scores, Using **kwargs
def student_scores(mode, **kwargs): 
    if mode == "best":
        best_name = None
        best_score = float('-inf')

        for key_name, value_score in kwargs.items():
            if value_score > best_score:
                best_score = value_score
                best_name = key_name

        return best_name

    elif mode == "mean":
        if len(kwargs) == 0:
            return 0
    return sum(kwargs.values()) / len(kwargs)
    
print(student_scores("best", Alice=90, Bob=85, Charlie=95))

#Task 8: Titleize, with String and List Operations
def titleize(text):
    words = text.split()
    little_words = ["a", "on", "an", "the", "of", "and", "is", "in"]

    for i, word in enumerate(words):
        if i == 0 or i == len(words) - 1:
            words[i] = word.capitalize()
        elif word in little_words:
            words[i] = word.lower()
        else:
            words[i] = word.capitalize()

    return " ".join(words)
print(titleize("a capital city of maryland is annapolis"))

#Task 9: Hangman, with more String Operations
def hangman(secret, guess):
    result =""
    
    for letter in secret:
        if letter in guess:
            result += letter
        else:
            result += "_"
    return result

secret = "alphabet"
guess = "ab"

print((hangman(secret, guess)))

#Task 10: Pig Latin, Another String Manipulation Exercise
def pig_latin(text):
    vowels = "aeiou"
    words = text.split()
    result = []

    for word in words:
        # starts with vowel
        if word[0] in vowels:
            result.append(word + "ay")
        else:
            i = 0
            # handle "qu" as a unit
            while i < len(word):
                if word[i] in vowels:
                    break
                if word[i] == 'q' and i + 1 < len(word) and word[i + 1] == 'u':
                    i += 2
                else:
                    i += 1
            # move consonant cluster to end + "ay"
            result.append(word[i:] + word[:i] + "ay")

    return " ".join(result)

print(pig_latin("banana"))