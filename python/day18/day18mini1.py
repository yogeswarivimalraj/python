import time

def timer_decorator(func):
    def wrapper(*args, **kwargs):
        start = time.time()                
        result = func(*args, **kwargs)      
        end = time.time()                  
        elapsed = end - start

        print(f"Function '{func.__name__}' executed in {elapsed:.6f} seconds")
        return result
    return wrapper
@timer_decorator
def slow_function():
    time.sleep(2)   
    return "Done"

print(slow_function())

@timer_decorator
def add(a, b):
    return a + b

print(add(10, 20))
