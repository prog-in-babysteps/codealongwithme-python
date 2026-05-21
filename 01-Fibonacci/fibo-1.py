import time
def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    fibo_n = fibonacci(n - 1) + fibonacci(n - 2)
    return fibo_n
start_time = time.perf_counter()
print(fibonacci(36))
end_time = time.perf_counter()
print("Recursive Fibonacci")
print(f"Time Taken : {end_time - start_time:.6f}")
