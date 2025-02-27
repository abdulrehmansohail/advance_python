# Create a greeting decorator
def greet(func):
    def wrap(*args, **kwargs):
        name = func(*args, **kwargs)
        print(name)
        return f"Hello {name.title()}, welcome to our code space"
    return wrap

@greet
def greet_user(name:str):
    return name

print(greet_user("a rehman"))