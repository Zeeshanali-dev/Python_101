

def debug(func):
    def wrapper(*args, **kwargs):
        arg_value = ", ".join(str(arg) for arg in args)
        kwarg_value = ", ".join(f"{k}={v}"  for k, v in kwargs.items())
        print(f"Calling {func.__name__} with arguments ({arg_value}, {kwarg_value})")
        result = func(*args, **kwargs)
        return result
    return wrapper







@debug
def greet(name, greeting="Hello"):
    print(f"{greeting} {name}")

greet("zeeshan",  greeting="Hi")