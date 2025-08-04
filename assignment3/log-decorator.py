# assignment3/log-decorator.py
import logging
from functools import wraps

# Setup logging
logger = logging.getLogger(__name__ + "_parameter_log")
logger.setLevel(logging.INFO)
logger.addHandler(logging.FileHandler("./decorator.log", "a"))

def logger_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        logger.info(f"function: {func.__name__} "
                    f"positional parameters: {args if args else 'none'} "
                    f"keyword parameters: {kwargs if kwargs else 'none'} "
                    f"return: {result}")
        return result
    return wrapper

@logger_decorator
def say_hello():
    print("Hello, World!")

@logger_decorator
def accept_args(*args):
    return True

@logger_decorator
def accept_kwargs(**kwargs):
    return logger_decorator

if __name__ == "__main__":
    say_hello()
    accept_args(10, 20, 30)
    accept_kwargs(name="Gedan", age=25)
