#Task 1 
def hello_world():
    return "Hello!"

print(hello_world())

#Task 2
def greet(name):
    return "Hello" +" " +name+ "!"

print(greet("Kavya"))

#Task 3
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
                return "Invalid operation"

    except ZeroDivisionError:
        return "You can't divide by 0!"

    except TypeError:
        return "You can't multiply those values!"
    
print(calc(2, 6,"add"))
print(calc(10, 0,"divide"))
print(calc("kavya", "Krishnamurthy", "multiply"))

#task 4
def data_type_convertor(value,data_type):
    try:
        match data_type:
            case "int":
                return int(value)
            case "float":
                return float(value)
            case "str":
                return str(value)
            case "bool":
                return bool(value)
            case _:
                return f"Invalid data type : {data_type}"
    except ValueError:
        return f"you cannot convert {value} to the specified {data_type}"
print(data_type_convertor("10", "int"))
print(data_type_convertor(100, "str"))
print(data_type_convertor("nonsense", "float"))

#task 5
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

    except TypeError:
        return "Invalid data was provided."
      
grade_1 = grade(60, 91, 83,56)
print(grade_1)
grade_2 = grade(100)
print(grade_2)
grade_3 = grade(100, 90, 80, 70, 60)
print(grade_3)
grade_4 = grade(100, 90, 80, 70, 60, "56")
print(grade_4)

#task 6
def repeat_string(string, n):
    result = "" #empty string to store the repeated string
    for i in range(n):
        result += string #concatenate the string to the result
    return result

print(repeat_string("Hello Kavya! ", 3))

#task 7
def student_scores(option, **kwargs):
    if option == "best":
        best_student = " "
        highest_score = -1
        for student, score in kwargs.items():
            if score > highest_score:
                highest_score = score
                best_student = student
        return best_student, highest_score
    elif option == "mean":
        total = 0
        for score in kwargs.values():
            total += score
        return total / len(kwargs)
    
print(student_scores("best", Hema=94, Jaya=85, sushma=97))
print(student_scores("mean", Hema=94, Jaya=85, sushma=97))

#task 8
def titleize(title):
    little_words = ["a", "on", "an", "the", "of", "and", "is", "in"]
    words = title.split()
    for i, word in enumerate(words):
        if i==0 or i==len(words)-1:
            words[i] = word.capitalize()
        elif word.lower() not in little_words:
            words[i] = word.lower()
        else:
            words[i] = word.capitalize()
    return " ".join(words)

print(titleize("the quick brown cat jumps over the lazy dog"))

# task 9
def hangman(secret, guess):
    result = " "
    for letter in secret:
        if letter in guess:
            result += letter
        else:
            result += "_"
    return result

print(hangman("alphabet", "ab"))

#task 10
def pig_latin(sentence):
    vowels = "aeiou"
    words = sentence.split()
    result = []
    for word in words:
        if word[0] in vowels:
            result.append(word + "ay")
        else:
            index = 0
            while index < len(word):
                if  word[index:index+2] == "qu":
                    index += 2
                elif word[index] not in vowels:
                    break
                else:
                    index += 1
            pig_word = word[index:] + word[:index] + "ay"
            result.append(pig_word)
    return " ".join(result)

print(pig_latin("alphabet"))
print(pig_latin("quick banana"))
