def hello():
    return "Hello!"

print (hello())

def greet(name):
    return (f"Hello, {name}!")

print(greet("James"))

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
            case "power":
                return a ** b
            case _:
                return "Unknown Operation. Please try again."
    
    
    except ZeroDivisionError:
        return "You can't divide by 0!"
    except TypeError:
        return "You can't multiply those values!"
                    


def data_type_conversion(value, data_type):
    try:
        if data_type == "int":
            return int(value)
        elif data_type == "float":
            return float(value)
        elif data_type == "str":
            return str(value)
        else:
            return "Unknown data type"
    
    except ValueError:
        return f"You can't convert {value} into a {data_type}."


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

    except (TypeError, ZeroDivisionError):
            return "Invalid data was provided."


def repeat(string, count):
    result = ""
    for i in range(count):
        result+= string
    return result
  
    

def student_scores(action, **kwargs):
    if action == "best":
        highest_score = 0
        best_student = ""

        for key, value in kwargs.items():
            if value > highest_score:
                highest_score = value
                best_student = key

        return best_student

    elif action == "mean":
        average = sum(kwargs.values()) / len(kwargs.values())
        return average
        


def titleize(string):
    words = string.split()

    little_words=['a','an', 'on', 'the', 'of', 'and', 'is', 'in']
    new_words =[]

    for i, word in enumerate(words):
        if i == 0 or i == len(words) -1:
            new_words.append(word.capitalize())
        else:
            if word not in little_words:
                new_words.append(word.capitalize()) 
            else:
                new_words.append(word)
    return " ".join(new_words)


def hangman(secret, guess):
    result = ""

    for letter in secret:
        if letter in guess:
            result = result + letter
        else:
            result = result + "_"
    
    return result


def pig_latin(sentence):
    words = sentence.split()
    vowels = "aeiou"
    new_words = []

    for word in words:
        if word[0] in vowels:
            new_words.append(word + "ay")
        
        elif word.startswith("qu"):
            new_words.append(word[2:] + "quay")

        else:
            while word[0] not in vowels:
                if word.startswith("qu"):
                    word = word[2:] + "qu"
                    break
        
                word = word[1:] + word[0]

            new_words.append(word + "ay")

    return " ".join(new_words)

            
