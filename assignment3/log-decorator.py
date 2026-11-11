def logger_decorator(func):

    def wrapper(*args, **kwargs):
        
        result = func(*args, **kwargs)
        
        with open("./decorator.log", "a") as file:
            file.write(f"Function name: {func.__name__}\n")
            file.write(f"Positional arguments: {args if args else 'none'}\n")
            file.write(f"Keyword arguments: {kwargs if kwargs else 'none'}\n")
            file.write(f"Return value: {result}\n")
            file.write("-" * 40 + "\n")
        
        return result
        
    return wrapper

@logger_decorator
def function_one():
    print("Function One running")

@logger_decorator
def function_two(*args):
    print("Function Two running")
    return True

@logger_decorator
def function_three(**kwargs):
    print("Function Three running")
    return logger_decorator

function_one()
function_two(10, 20, 30)
function_three(name="Alex", age=21)