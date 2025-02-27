# Implementing a Python decorator for function retry
import sqlite3
import time


# Level 1: Parameters Handler
def retry_on_failure(max_retries, delay=1):
    """
        retry_on_failure is a parameterized decorator (a decorator that takes arguments).
        1. Simple decorator has 2 levels
        2. Parameterized decorator has 3 levels
        3. Extra level is needed to handle the decorator parameters
    """ 
    # Level 2: Actual Decorator
    def decorator(func):
        # Level 3: Wrapper Function
        def wrap(*args, **kwargs):
            # This is where the magic happens
            for i in range(1, max_retries+1):
                try:
                    result = func(*args, **kwargs)
                    return result
                except Exception as e:
                    result = f"{i}/{max_retries} Failed, Attempting retry error {e}"
                    print(result)
                    time.sleep(delay)
            raise Exception("Max Retries Exceeded")
        return wrap
    return decorator


@retry_on_failure(max_retries=3, delay=2)
def connect_to_db():
    conn = sqlite3.connect("test_decorator.db")
    curser = conn.cursor()
    curser.execute("select * from student")
    result = curser.fetchall()
    curser.close()
    conn.close()
    return result

print(connect_to_db())