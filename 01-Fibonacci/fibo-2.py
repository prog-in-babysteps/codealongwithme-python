import time
fib_dict = {0: 0, 1: 1}

def fibonacci(n):
    res = fib_dict.get(n)
    if res is not None:
        return res
    fibo_n = fibonacci(n - 1) + fibonacci(n - 2)
    fib_dict[n] = fibo_n
    return fibo_n

start_time = time.perf_counter()
print(fibonacci(36))
end_time = time.perf_counter()
print("Dynamic Programming Fibonacci Number with Memoization")
print(f"Time Taken : {end_time - start_time:.6f}")
