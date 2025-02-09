
#  bare minimum for Decorator

# def debug(func):
#     def wrapper(*args, **kwargs):
#         result = func(*args, **kwargs)
       
#         return result
#     return wrapper





import time

def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Function {func.__name__} took {end_time - start_time} seconds to execute")
        return result
    return wrapper

@timer
def example_function(n):
    time.sleep(n)

example_function(2)