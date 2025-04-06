# Write your code here.

# Task 1: Hello
def hello(): 
    return "Hello!"

print(hello())


# Task 2: Greet with a Formatted String
def greet(name):
    return "Hello " +name + "!"

print(greet("Mike"))

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
                return "Invalid operation!"
    
    except ZeroDivisionError:
        return "You can't divide by 0!"
    except TypeError:
        return "You can't multiply those values!"
    except Exception as e:
        return f"An error occurred: {e}"
    
print(calc(1, 4, "power"))

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
                return f"Invalid data type: {data_type}"  
    except ValueError:
        return f"You can't convert {value} into a {data_type}."
    except TypeError:
        return f"Invalid type for conversion: {value} into {data_type}."
    except Exception as e:
        return f"An error occurred: {e}"
    
print(data_type_conversion("string", "str"))

# Task 5: Grading System, Using *args
def grade(*args):
    try:
        if not args:
            return "Invalid data was provided."
        
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
    except (TypeError, ValueError):
        return "Invalid data was provided."
    
print(grade(90,70,100,39, 100))

# Task 6: Use a For Loop with a Range
def repeat(string, count):
    try:
        result = ""
        for _ in range(count):
            result += string
        return result
    except TypeError:
        return "Invalid data was provided."
    
print(repeat('Hello CTD. ', 10))

# Task 7: Student Scores, Using **kwargs
def student_scores(metric, **kwargs):
    try:
        if not kwargs:
            return "No student scores provided."
        
        if metric == "best":
            return max(kwargs, key=kwargs.get)
        elif metric == "mean":
            return sum(kwargs.values()) / len(kwargs)
        else:
            return "Invalid metric. Use 'best' or 'mean'."
    except Exception as e:
        return f"An error occurred: {e}"
    
# Task 8: Titleize, with String and List Operations
def titleize(text):
    try:
        little_words = {"a", "on", "an", "the", "of", "and", "is", "in"}
        words = text.split()
        
        for i, word in enumerate(words):
            if i == 0 or i == len(words) - 1 or word.lower() not in little_words:
                words[i] = word.capitalize()
            else:
                words[i] = word.lower()
        
        return " ".join(words)
    except Exception as e:
        return f"An error occurred: {e}"
    
print(titleize("on the edge of glory"))  

# Task 9: Hangman, with more String Operations
def hangman(secret, guess):
    try:
        return "".join(letter if letter in guess else "_" for letter in secret)
    except Exception as e:
        return f"An error occurred: {e}"
    
print(hangman("programming", "prog"))

# Task 10: Pig Latin, Another String Manipulation Exercise
def pig_latin(text):
    try:
        vowels = {"a", "e", "i", "o", "u"}
        words = text.split()
        pig_latin_words = []

        for word in words:
            if word[0] in vowels:
                pig_latin_words.append(word + "ay")
            else:
                index = 0
                while index < len(word) and word[index] not in vowels:
                    # Special case: treat 'qu' as a unit
                    if word[index] == 'q' and index + 1 < len(word) and word[index + 1] == 'u':
                        index += 2
                        break
                    index += 1
                pig_latin_words.append(word[index:] + word[:index] + "ay")

        return " ".join(pig_latin_words)
    except Exception as e:
        return f"An error occurred: {e}"
