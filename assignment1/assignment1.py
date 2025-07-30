#Task 1
def hello():
    return "Hello, World!"
#Task 2
def greet(name):
    return f"Hello, {name}!"
#Task 3
def calc(x,y,operator):
   match operator:
       case 'add':
           return x + y
       case 'subtract':
            return x - y
       case 'multiply':
            return x * y
       case 'divide':
                return x / y
         
calc(10, 5, 'add')  # Example usage