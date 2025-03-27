
# Task 1: Hello
def hello():
    return "Hello!"  
print(hello())
# Task 2: Greeting
def greet(name):
    return f"Hello, {name}!" 
print(greet("Arthur"))

# Task 3:Creating Calculator
def calculator(a, b, operation="multiply"): # this operation will be overrided accordingly, this is just default parameter.
    try:
        operations = {
            "add": a + b,
            "subtract": a - b,
            "multiply": a * b,
            "divide": a / b,
            "modulo": a % b,
            "int_divide": a // b,
            "power": a ** b
        }
        if operation in operations:
            return operations[operation]
        else:
            return "Invalid operation"
    except ZeroDivisionError:
        return "You can't divide by 0!"
    except TypeError:
        return "You can't multiply those values!"
print(calculator(3, 5, "add"))       
print(calculator(10, 4, "subtract"))   
print(calculator(2, "abc", "multiply")) # testing TypeError from except
print(calculator(10, 0, "divide")) # testing  ZeroDivisionError from except



# Task 4: Data Type Conversion
def data_type_conversion(value, to_type):
    try:
        if to_type == "int":
            return int(value)
        elif to_type == "float":
            return float(value)
        elif to_type == "str":
            return str(value)
        else:
            return f"Unsupported type: {to_type}"
    except (ValueError, TypeError):
        return f"You can't convert {value} into a {to_type}."
print(data_type_conversion(123, "str"))         # 123
print(data_type_conversion(123, "float"))       # 123.0
print(data_type_conversion("hello", "int"))     # You can't convert hello into a int.
print(data_type_conversion("7.8", "int"))       # You can't convert 7.8 into a int.
print(data_type_conversion("true", "bool"))     # Unsupported type: bool


# Task 5: Grading System
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
    except:
        return "Invalid data was provided."
print(grade(75, 85, 95)) # B
print(grade("three", "blind", "mice")) # Invalid data was provided.

# Task 6: Repeat using for loop

def repeat(text, count):
    result = ""
    for _ in range(count):
        result += text
    return result
print(repeat("hello", 5)) # hellohellohellohellohello
print(repeat("up,", 0)) # empty string as it was requested to repeat 0 times.

# Task 7: Student Scores

def student_scores(stat, **kwargs):
    if stat == "best":
        return max(kwargs, key=kwargs.get) # .get is super handy to get the value of the key.
    elif stat == "avg":
        return sum(kwargs.values()) / len(kwargs)
    else:
        return "Invalid request"
print(student_scores("best", Alice=88, Bob=92, Charlie=79))  
print(student_scores("avg", Alice=88, Bob=92, Charlie=79))  
print(student_scores("mean", Alice=88, Bob=92, Charlie=79))

# Task 8: Titleizing a Sentence

def titleize(sentence):
    little_words = {"a", "on", "an", "the", "of", "and", "is", "in"}
    words = sentence.split() #.split() method is used to split the string into a list.
    result = []
    for i, word in enumerate(words): # enumerate adds a counter to an iterable object.
        if i == 0 or i == len(words) - 1 or word not in little_words:
            result.append(word.capitalize())
        else:
            result.append(word.lower())
    return " ".join(result)
print(titleize("war and peace")) # War and Peace
print(titleize("a separate peace")) # A Separate Peace

# Task 9: Hangman
def hangman(secret, guess):
    return "".join([char if char in guess else "_" for char in secret]) #using list comprehension here
print(hangman("difficulty", "ic")) # _i__ic____
print(hangman("difficulty", "icd")) # _ic_ic____

# Task 10: Pig Latin
def pig_latin(sentence):
    vowels = "aeiou"
    words = sentence.split()
    result = []
    for word in words:
        if word.startswith("qu"):
            result.append(word[2:] + "quay")
        elif word[0] in vowels:
            result.append(word + "ay")
        else:
            for i in range(len(word)):
                if word[i] in vowels:
                    result.append(word[i:] + word[:i] + "ay")
                    break
    return " ".join(result)
