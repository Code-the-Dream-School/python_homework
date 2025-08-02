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
# Example usage of the functions
if __name__ == "__main__":
    print(hello())
    print(greet("Ade"))
    print(calc(10, 8, "add"))
    print(data_type_conversion("123", "int"))
    print(grade(85, 90, 78, 92))  # Example grades
    print(grade())  # No grades provided
    print(data_type_conversion("abc", "int"))  # Invalid conversion
    print(calc(10, 0, "divide"))  # Division by zero