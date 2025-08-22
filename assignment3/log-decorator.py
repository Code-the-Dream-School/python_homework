#Task 1
#a.
import logging
logger = logging.getLogger(__name__  + "_parameter_log")
logger.setLevel(logging.INFO)
logger.addHandler(logging.FileHandler("./decorator.log","a"))

# To write a log record:
logger.log(logging.INFO, "this string would be logged")

#b. Writing and testing a decorator
def logger_decorator(func):
    def wrapper(*args, **kwargs):
        logger.info(f"Calling function '{func.__name__}' with args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        logger.info(f"Function '{func.__name__}' returned {result}")
        return result
    return wrapper

@logger_decorator
def func():
    print("This is a test function")

@logger_decorator
def est(a, *b):
    if sum (a, *b) > 0:
        return True
    
#e. decorate func(**kwargs) as well
@logger_decorator
def log_dec(**kwargs):
    for key, value in kwargs.items():
        return f"{key}: {value}"

#tack f. Test the decorated functions
log_dec(name="Rabiat", age=30, city="New York")


#Task2: Decorator that takes an argument