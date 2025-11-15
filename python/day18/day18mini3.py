import time

def timer_decorator(func):
    def wrapper(*args, **kwargs):
        start = time.time()           
        result = func(*args, **kwargs)
        end = time.time()            
        print(f"Function '{func.__name__}' took {end - start:.5f} seconds")
        return result
    return wrapper


@timer_decorator
def calculate_sum(n):
    total = 0
    for i in range(n):
        total += i
    return total


@timer_decorator
def wait_function():
    time.sleep(2)


print(calculate_sum(1000000))
wait_function()

# def timer_decorator(func):
# start = time.time()

# end = time.time()
# print(f"Function '{func.__name__}' took {end - start:.5f} seconds")
