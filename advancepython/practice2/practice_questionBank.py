## Q1 Write a decorator that measures the execution time of any function and prints it.
# import time
# def measures_time(func):
#     def wrapper(*args, **kwargs):
#         start = time.time()
#         result = func(*args, **kwargs)
#         print(f"{func.__name__} took {time.time()-start:.4f}s")
#         return result
#     return wrapper

# @measures_time
# def slow_func():
#     time.sleep(1)
    
# @measures_time
# def medium_func(n):
#     if n % 2 ==0:
#         print("even")
#     else:
#         print("odd")
    
#     time.sleep(5)
    
# print(slow_func())
# print(medium_func(24))

## Q2 Write a decorator factory @retry(n) that retries a function up to n times if it raises an exception.
# def retry(n):
#     def decorator(func):
#         def wrapper(*args, **kwargs):
#             for i in range(n):
#                 try:
#                     return func(*args, **kwargs)
#                 except Exception as ec:
#                     if i == n - 1 : raise
#             return None
#         return wrapper
#     return decorator

# @retry(3)
# def show():
#     raise ValueError("oops")
    
# show()

## Q3 Write a generator that yields Fibonacci numbers infinitely.
# def fib():
#     a, b = 0, 1
#     while True:
#         yield a
#         a, b = b, a+b
# f= fib()

# print([next(f) for _ in range(8)])
    
## Q4 What is the difference between yield and yield from? Show with an example.
# def inner():
#     yield 1
#     yield 2
# def with_yield():
#     yield inner
# def with_yield_from():
#     yield from inner
    
# with_yield_from()

# # print(next(inner()))
# print(next(with_yield_from()))

