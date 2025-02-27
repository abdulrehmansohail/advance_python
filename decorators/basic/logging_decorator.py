# 1. Write a Python program to create a decorator that logs the arguments and return value of a function.
def track_record(func):
    print("decorator")
    def wrap(*args, **kwargs):
        print(f"Calling {func.__name__} with args {args} and kwargs {kwargs}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned {result}")
        return result
    return wrap

@track_record
def multiply_nums(x, y):
    print("main")
    return x * y

print(multiply_nums(4,5))

