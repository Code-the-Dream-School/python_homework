# Task 1
def hello():
    return "Hello!"

# Optional: test manually before pytest
print(hello())

# Task 2
def greet(name):
    return f"Hello, {name}!"

    print(greet("Zhana"))

# Task 3
def calc(a, b, op="multiply"):
    try:
        if op == "add":
            return a + b
        elif op == "subtract":
            return a - b
        elif op == "multiply":
            return a * b
        elif op == "divide":
            return a / b
        elif op == "modulo":
            return a % b
        elif op == "int_divide":
            return a // b
        elif op == "power":
            return a ** b
        else:
            return "Invalid operation"
    except ZeroDivisionError:
        return "You can't divide by 0!"
    except Exception:
        return "You can't multiply those values!"



#Task 4
def divide(x, y):
    return x / y

print(divide(10, 2))

# Task 5
def data_type_conversion(value, target_type):
    try:
        if target_type == "int":
            return int(value)
        elif target_type == "float":
            return float(value)
        elif target_type == "str":
            return str(value)
        elif target_type == "bool":
            return bool(value)
        else:
            return "Unsupported type"
    except Exception:
        return f"You can't convert {value} into a {target_type}."
# Task 6
def grade(a, b, c):
    try:
        average = (a + b + c) / 3
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
    except TypeError:
        return "Invalid data was provided."

#Task 7
def repeat(text, count):
    return text * count

#Task 8
def student_scores(method, **scores):
    if method == "mean":
        return sum(scores.values()) / len(scores)
    elif method == "best":
        return max(scores, key=scores.get)
    else:
        return "Unsupported method"
#Task 9
def titleize(text):
    small_words = {"and", "or", "of", "in", "on", "at", "a", "the"}
    words = text.split()
    result = []
    
    for i, word in enumerate(words):
        if i == 0 or i == len(words) - 1 or word not in small_words:
            result.append(word.capitalize())
        else:
            result.append(word.lower())
    
    return " ".join(result)

# Task 10
def hangman(secret, letters):
    result = ""
    for char in secret:
        if char.lower() in letters:
            result += char
        else:
            result += "_"
    return result
# Task 11
def pig_latin(text):
    vowels = "aeiou"

    def convert_word(word):
        # Word starts with vowel
        if word[0] in vowels:
            return word + "ay"
        # Word starts with "qu"
        elif word.startswith("qu"):
            return word[2:] + "quay"
        # Word has "qu" after first consonant, like "squ"
        elif "qu" in word:
            qu_index = word.find("qu")
            return word[qu_index + 2:] + word[:qu_index + 2] + "ay"
        else:
            # Move consonants before the first vowel to the end
            for i, char in enumerate(word):
                if char in vowels:
                    return word[i:] + word[:i] + "ay"
            return word + "ay"  # if no vowels found

    return ' '.join(convert_word(w) for w in text.split())
