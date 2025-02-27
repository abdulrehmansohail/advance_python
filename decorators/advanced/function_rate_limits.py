# Write a Python program that implements a decorator to enforce rate limits on a function.
import time


def rate_limit(max_calls, time_period):

    def decorator(func):
        num_calls = 0
        last_reset = time.time()
        def wrap(*args, **kwargs):
            nonlocal num_calls, last_reset
            time_elapsed = time.time() - last_reset
            if time_elapsed > time_period:
                num_calls = 0
                last_reset = time.time()
            if num_calls >= max_calls:
                raise Exception("Max Calls exceeded")
            num_calls += 1
            return func(*args, **kwargs)
        return wrap
    return decorator


@rate_limit(max_calls=5, time_period=0.1)
def api_call():
    print("API call executed successfully...")

# Test scenarios
def test_rate_limit():
    print("\nTest 1: Making 4 calls (should succeed)")
    for _ in range(4):
        api_call()
        time.sleep(0.1)  # Small delay to see outputs clearly
    
    print("\nTest 2: Making 6 calls (5th call should succeed, 6th should fail)")
    for _ in range(6):
        try:
            api_call()
            print(f"Call succeeded")
        except Exception as e:
            print(f"Call failed: {e}")
        time.sleep(0.1)
    
    print("\nTest 3: Waiting 5 seconds and trying again (should succeed)")
    time.sleep(5)
    api_call()

test_rate_limit()