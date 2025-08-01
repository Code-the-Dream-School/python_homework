#Task 1
def hello():
    return "Hello, World!"
print(hello())  # Example usage
#Task 2
def greet(name):
    return f"Hello, {name}!"
#Task 3
def calc(x,y,operator):
    try:
        x = float(x)
        y = float(y)
        match operator:
            case 'add':
                return x + y
            case 'subtract':
                return x - y
            case 'multiply':
                return x * y
            case 'divide':
                if y == 0:
                    return "Error: Division by zero"
                return x / y
            case _:
                return "Error: Invalid operator"
    except ValueError:
        return "Error: Invalid input, please enter numbers"
    except Exception as e:
        return f"Error: {e}"
#Task 4
def data_type_conversion(value, data_type):
    try:
        match data_type:
            case 'int':
                return int(value)
            case 'float':
                return float(value)
            case 'str':
                return str(value)
            case _:
                return "Error: Invalid data type"
    except ValueError:
        return "You can't convert {value} to {data_type}"
    except Exception as e:
        return f"Error: {e}"    
data_type_conversion('fool', 'int')  # Example usage
#Task 5
def grade(*args):
    try:
        total = sum(args)
        count= len(args)
        average = total / count
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
    except ZeroDivisionError:
        return "Error: No grades provided"
    except TypeError:
        return "Invalid data was provided"
    except Exception as e:
        return f"Error: {e}"
#Task 6
def repeat (string, count):
    try:
        for i in range(count):
            print(string)
    except TypeError:
        return "Error: Count must be an integer"
#Task 7 
def student_scores (calculation, **kwargs):
    try:
        if calculation == 'average':
            total = sum(kwargs.values())
            count = len(kwargs)
            return total / count if count > 0 else 0
        elif calculation == 'max':
            return max(kwargs.values())
        else:
            return "Error: Invalid calculation type"
    except Exception as e:
        return f"Error: {e}"
#Task 8
def titleize(string):
    little_words =("a", "on","an", "the","of","and","is","in")
    words = string.split()
    for i, word in enumerate(words):
        if word.lower() not in little_words:
            words[i] = word.capitalize()
    return " ".join(words)
#Task 9
def hangman(secret, guess):
    result = []
    for i in secret:
        if i in guess:
            result.append(i)
        else:
            result.append('_')
    return " ".join(result)
#task 10
def pig_latin(word):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    words = word.split().lower()
    pig_latin_words = []
    for w in words:
        if w.startswith("qu"):
            pig_latin_words.append(w[2:] + "qu")
        elif w[0] in vowels:
            pig_latin_words.append(w + "ay")
        else:
            for i,char in enumerate(w):
                if char in vowels:
                    pig_latin_words.append(w[i:] + w[:i] + "ay")
                    break
    return" ".join(pig_latin_words)
