# Creating a Python decorator to measure function execution time
import time


def time_track(func):
    def wrap(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        time.sleep(3)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"time taken : {execution_time:.4f}")
        return result
    return wrap
@time_track
def product_list(data_list:list):
    x = 1
    time.sleep(2)
    for data in data_list:
        x *= data
    return x

print(product_list([2,3,4,5,6,7,99]))