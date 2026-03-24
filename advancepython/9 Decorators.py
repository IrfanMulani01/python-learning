"""
========================================
DECORATORS IN PYTHON
========================================

Definition:
-----------
A decorator is a function that
adds extra functionality to another
function or method
WITHOUT modifying its original code.

Decorators use the '@' symbol.

A function that wraps another function
Adds extra code before and after it runs

"""

# ==================================================
# WHY DECORATORS ARE USED
# ==================================================

"""
✔ Add extra behavior (logging, auth, validation)
✔ Reuse code
✔ Keep original function clean
"""

# ==================================================
# BASIC FUNCTION (WITHOUT DECORATOR)
# ==================================================

# def say_hello():
#     print("Hello!")
# say_hello()

"""
PROGRAM LOGIC:
--------------
1. say_hello() is a normal function
2. It directly prints "Hello"
3. No extra behavior is added
"""

# ==================================================
# BASIC DECORATOR STRUCTURE
# ==================================================

# def my_decorator(func):
#     def wrapper():
#         print("Before function call")
#         func()
#         print("After function call")
#     return wrapper

# @my_decorator
# def say_hello():
#     print("Hello!")

# say_hello()


"""
PROGRAM LOGIC:
--------------
1. my_decorator receives a function as argument
2. wrapper() adds extra code
3. func() is called inside wrapper
4. wrapper is returned instead of original function
"""

# ==================================================
# USING DECORATOR WITHOUT '@'
# ==================================================



# def my_decorator(func):
#     def wrapper():
#         print("Before function call")
#         func()
#         print("After function call")
#     return wrapper

# def greet():
#     print("Hello")

# greet = my_decorator(greet)
# greet()

"""
PROGRAM LOGIC:
--------------
1. greet function is passed to my_decorator
2. my_decorator returns wrapper
3. greet now points to wrapper
4. wrapper executes:
   - before message
   - original greet()
   - after message
"""

# ==================================================
# USING DECORATOR WITH '@'
# ==================================================



# def my_decorator(func):
#     def wrapper():
#         print("Before function call")
#         func()
#         print("After function call")
#     return wrapper

# @my_decorator
# def greet():
#     print("Hello")

# greet()

"""
PROGRAM LOGIC:
--------------
1. @my_decorator automatically wraps greet()
2. greet becomes wrapper
3. Calling greet() actually calls wrapper()
"""

# ==================================================
# DECORATOR WITH ARGUMENTS
# ==================================================

# def my_decorator(func):
#     def wrapper(*args, **kwargs):
#         print("Before function call")
#         result = func(*args, **kwargs)
#         print("After function call")
#         return result
#     return wrapper

# @my_decorator
# def add(a, b):
#     return a + b

# print(add(5, 10))

"""
PROGRAM LOGIC:
--------------
1. add(5, 10) is passed to wrapper
2. *args receives (5, 10)
3. func(*args) executes add()
4. Result is returned safely
"""

# ==================================================
# MULTIPLE DECORATORS
# ==================================================

# def decorator1(func):
#     def wrapper():
#         print("Decorator 1")
#         func()
#     return wrapper

# def decorator2(func):
#     def wrapper():
#         print("Decorator 2")
#         func()
#     return wrapper

# @decorator1
# @decorator2
# def show():
#     print("Inside show")

# show()

"""
PROGRAM LOGIC:
--------------
Execution order (BOTTOM to TOP):
1. show → decorator2
2. result → decorator1
3. decorator1 runs first
4. decorator2 runs inside it
"""

# ==================================================
# CLASS METHOD DECORATOR
# ==================================================

# class Student:
#     school = "ABC School"

#     @classmethod
#     def show_school(cls):
#         print("School:", cls.school)

# Student.show_school()

"""
PROGRAM LOGIC:
--------------
1. @classmethod passes class as argument (cls)
2. No object creation needed
3. Used to access class-level data
"""

# ==================================================
# STATIC METHOD DECORATOR
# ==================================================

# class MathUtils:
#     @staticmethod
#     def add(a, b):
#         return a + b

# print(MathUtils.add(10, 20))

"""
PROGRAM LOGIC:
--------------
1. @staticmethod does NOT use self or cls
2. Acts like a normal function
3. Logically belongs to the class
"""

# ==================================================
# PROPERTY DECORATOR
# ==================================================

# class Person:
#     def __init__(self, name):
#         self._name = name

#     @property
#     def name(self):
#         return self._name

# p = Person("Navanath")
# print(p.name)

"""
PROGRAM LOGIC:
--------------
1. name() method behaves like an attribute
2. p.name internally calls name()
3. Used for data hiding and validation
"""

# ==================================================
# CLASS DECORATOR
# ==================================================

# def class_decorator(cls):
#     cls.category = "Decorated Class"
#     return cls

# @class_decorator
# class Demo:
#     pass

# d = Demo()
# print(d.category)

"""
PROGRAM LOGIC:
--------------
1. Class is passed to decorator
2. New property is added
3. Class is returned with changes
"""

# ==================================================
# REAL-WORLD EXAMPLE (LOGIN CHECK)
# ==================================================

# def login_required(func):
#     def wrapper(user):
#         if user == "admin":
#             return func(user)
#         else:
#             print("Access Denied")
#     return wrapper

# @login_required
# def dashboard(user):
#     print("Welcome:", user)

# dashboard("admin")
# dashboard("guest")

"""
PROGRAM LOGIC:
--------------
1. dashboard() is wrapped
2. wrapper checks condition
3. Only valid user can access function
"""

# ==================================================
# IMPORTANT POINTS
# ==================================================

"""
✔ Decorators wrap functions
✔ @ symbol simplifies syntax
✔ Used heavily in Django (login_required)
"""

# ==================================================
# QUICK SUMMARY (EXAM READY)
# ==================================================

"""
Decorators:
-----------
Functions that modify behavior
without changing original code

Types:
✔ Function Decorators
✔ Class Decorators
✔ Built-in Decorators
"""
