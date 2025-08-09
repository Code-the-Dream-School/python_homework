def logger_decorator(func):
    def wrapper(*args, **kwargs):
        pos_args = list(args) if args else "none"
        kw_args = kwargs if kwargs else "none"

        result = func(*args, **kwargs)


        log_message = (
            f"function: {func.__name__}\n"
            f"positional parameters: {pos_args}\n"
            f"keyword parameters: {kw_args}\n"
            f"return: {result}\n\n"
        )

        with open("decorator.log", "a") as log_file:
            log_file.write(log_message)

        return result
    return wrapper


@logger_decorator
def nothingfunction():
    print("Hello, World!")


@logger_decorator
def check_args(*args):
    return True

@logger_decorator
def get_decorator(**kwargs):
    return logger_decorator

nothingfunction()
check_args(1,2, 'true')
get_decorator(debug=True)