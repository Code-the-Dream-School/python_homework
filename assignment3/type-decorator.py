def type_converter(type_of_output):

    def decorator(func):

        def wrapper():
            result = func()
            return type_of_output(result)
        return wrapper
    return decorator

@type_converter(str)
def return_int():
    return 5

@type_converter(int)
def return_string():
    return "not a number"

y = return_int()
print(type(y).__name__)

try:
    return_string()
except ValueError:
    print("can't convert that string to an integer!")