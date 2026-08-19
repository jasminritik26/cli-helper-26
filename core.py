import time
from functools import wraps

# A simple cache to optimize repeated function calls
cache = {}  

def memoize(func):
    @wraps(func)
    def wrapper(*args):
        if args in cache:
            return cache[args]
        result = func(*args)
        cache[args] = result
        return result
    return wrapper

@memoize
def expensive_computation(x):
    time.sleep(2)  # Simulating a time-consuming computation
    return x * x

# Example usage of the expensive computation function
if __name__ == '__main__':
    print(expensive_computation(4))  # First call, will take time
    print(expensive_computation(4))  # Second call, will return instantly
    print(expensive_computation(5))  # New computation, will take time again
    print(expensive_computation(5))  # Return instantly again for 5