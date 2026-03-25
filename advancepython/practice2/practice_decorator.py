# Q1. Write a simple decorator greet that prints "Good Morning!" 
# before calling any function. Apply it to a function say_hello() that prints "Hello!".
# def greet(func):
#     def wrapper():
#         print("Good Morning")
#         func()
#     return wrapper
    
    
# @greet
# def say_hello():
#     print("Hello!")
    
# say_hello()

# Q2. Write a decorator separator that prints "====================" 
# before and after any function's output. Apply it to a function that prints your name.

# def greet(func):
#     def wrapper():
#         print("====================")
#         func()
#         print("====================")
#     return wrapper

# @greet
# def pr():
#     print("Hello")

# pr()

# Q3. Write a decorator shout that takes the return 
# value of a function and converts it to uppercase. Apply it to a function get_name() that returns "python".
# def shout(func):
#     def wrapper(*args, **kwargs):
#         result = func(*args, **kwargs)  
#         return result.upper()
#     return wrapper

# @shout
# def get_name():
#    return ("python")

# print(get_name())

# ## Q5. Write a decorator logger that prints:
# Calling function: <function_name>
# Function finished: <function_name>
# before and after calling any function.

# def logger(func):
#     def wrapper():
#         print(f"calling function: {func()}")
#         # func()
#         print(f"Function finished: {func()}")
#     return wrapper

# @logger
# def show():
#     return "show function"
# # show()
# # print(show())

## Q6. Write a decorator validate_positive that checks if all arguments passed to a function are positive numbers. 
# If not, print "Invalid input!" and don't call the function. Apply it to an add(a, b) function.
# def validate_positive(func):
#     def wrapper(*args, **kwargs):
#         result = func(*args, **kwargs)
#         if result < 0:
#             print(f"{result} number is negative")
#         else:
#             print(f"{result} number is positive")
#     return wrapper

# @validate_positive
# def show(a):
#     return a
# show(-1)

# Q7. Write a decorator repeat(n) — a decorator with argument — that calls the decorated function n times.
# def repeat(n):
#     def decorator(func):
#         def wrapper(*args, **kwargs):
#             result = func(*args, **kwargs)
#             res = result * n
#             return res
#         return wrapper
#     return decorator

# @repeat(3)
# def show():
#     return "hii "

# print(show())

## **Q8.** Write a decorator `cache` that stores the results of a function call. If the same arguments are passed again, 
# return the **cached result** instead of recalculating. Apply it to a slow Fibonacci function.
# def cache(func):
#     stored = {}
#     def wrapper(*args):
#         if args in stored:
#             print(f"cache result for {args}")
#             return stored[args]
        
#         result = func(*args)
#         stored[args] = result
#         return result
#     return wrapper

# @cache
# def fib(n):
#     if n <= 1:
#         return n
#     return fib(n-1)+fib(n-2)
# print(fib(6))

## **Q9.** Write a decorator `require_login` that checks if a variable `is_logged_in = True`. 
# If not, print `"Access Denied!"` and block the function. Apply it to a `view_dashboard()` function.
# def require_login(func):
#     is_logged_in = False
#     def wrapper():
#         if is_logged_in == True:
#             print("Access Grantted")
#             func()
#         else:
#             print("Access Denied")
#     return wrapper

# @require_login
# def view_dashboard():
#     print("Wellcome to dashboard")
# view_dashboard()

# ## Q12. In a class Employee, use:
# @classmethod to track total employees
# @staticmethod to validate salary (must be > 0)
# A regular instance method show() to display employee details

# class Employee:
#     total_emp =0
    
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary
#         Employee.total_emp += 1
    
#     @classmethod
#     def show_total(cls):
#         print(f"total employees are {cls.total_emp}")
        
#     @staticmethod
#     def validate_salary(salary):
#         if salary > 0:
#             print(f"salary is {salary}")
#         else:
#             print("Enter valid salary")

# emp = Employee("irfan", 0)
# emp.show_total()
# emp.validate_salary(2000)


# ## Q14. Build a mini access control system using decorators:
# @timer — logs execution time
# @logger — logs function name
# @require_login — blocks unauthorized access
# Apply all three on a function download_file() and test with both is_logged_in = True and False.

# import datetime as dt
# class accessControl:
    
#     def __init__(self, name, is_logged_in = True):
#         self.name = name
#         self.is_logged_in = is_logged_in
        
#     def timer(func):
#         def wrapper(self):
#             print(f"Time: {dt.datetime.now().hour}")
#             func(self)       
#         return wrapper
    
#     def logger(func):
#         def wrapper(self):
#             print(f"logger name is {self.name}")
#             func(self)
#         return wrapper
    
#     def require_login(func):
#         def wrapper(self):
#             if self.is_logged_in:
#                 print("Access Granted")
#                 func(self)
#             else:
#                 print("Access Denied")
#         return wrapper
    
#     @timer
#     @logger
#     @require_login
#     def download_file(self):
#         print("Downloadding file")
        
# ac = accessControl("irfan")
# ac.download_file()

