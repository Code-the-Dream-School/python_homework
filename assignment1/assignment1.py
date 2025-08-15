# Write your code here.
#Task 1: Hello function
def hello():
    return "Hello, world!"

#Task 2: Greet function
def greet(name):
   return f"Hello, {name}!"

#print(greet("Ade"))

#Task 3: Calc function
def calc(a, b, operation):
    if operation == "add":
        return a + b
    elif operation == "subtract":
        return a - b
    elif operation == "multiply":
        return a * b
    elif operation == "divide":
        if b != 0:
            return a / b
        else:
            return "Error: Division by zero is not"
    else:
        return "Error: Unknown operation"
    
    #print(calc(10, 8, "add"))

#Task 4: Data Type Conversion Function
def data_type_conversion(value, dataType):
    try:
        if dataType == "float":
            return float(value)
        elif dataType == "string":
            return str(value)
        elif dataType == "int":
            return int(value)
        else:
            return "Error: Unknown data type"
    except ValueError:
        return f"Error: You can not convert {value} to {dataType}"
    
#Task 5: Grading System Using Arguments *args

def grade(*args):
    if not args:
        return "Error: No grades provided"  
 
    total = sum(args)
    count = len(args)
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

#Task 6: For Loop with a range

def repeat(string, count):
    if count > 0:
        for i in range(count):
            print(string)
        print (string * count)
    else:
        return "Error: Count must be a positive integer"
    
#Trying out task 6
#repeat("Hello", 3)

#Task 7: Student scores using **kwargs
"""def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Janet", role="Developer", age=25)"""
def student_scores(**kwargs):
   for key, value in kwargs.items():
       if key.startswith("score_") and isinstance(value, (int, float)):
           score.append(value)
       if value == max(score):
           return f"kwargs.get('name', 'Student') has the highest score: {key} with a score of {value}" 
       elif value == score/len(score):
           return f"average score is {sum(score)/len(score)}"
       
# Task 8: Titleize, with String and List Operations

def titleize(string):
    for i in string.split():
        if i.isupper():
            return "Error: String contains uppercase letters"
    return string.title()   
    if capitalize:
        return string.title()
    else:
        return string.lower()
    
#Task 9:Hangman, with more String Operations

def hangman(secret, guess):
    for char in guess:
        if char in secret:
            print(f"Good guess: {char} is in the word!")
        else:
            print(f"{char} is not in the word.")
    # Example of showing the current guessed state (optional):
    # print(''.join([c if c in guess else '_' for c in secret]))

    #Task 10: Pig Latin, Another String Manipulation Exercise

def pigLatin(word):
    # Simple Pig Latin implementation: move first letter to end and add 'ay'
    first = word[0]
    if first.lower() in 'aeiou':
        return word + "ay"
    else:
        return word[1:] + first + "ay"