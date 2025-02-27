"""
    Decorator Structure
    def decorator(func: main_function):
        def wrap(*args, **kwargs):
            result = func(*args, **kwargs)
            return result
        return wrap # no parentheses there

    @decorator
    def main_function():
        return something
"""

def greet(func):
    def wrap(*args, **kwargs):
        return f"Hello {func(*args, **kwargs)}"
    return wrap

@greet
def greet_user(name:str):
    return name

print(greet_user("jhon doe"))