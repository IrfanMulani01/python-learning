"""
==============================
PYTHON return STATEMENT
==============================

The return statement is used inside a function to:

1. End the execution of the function
2. Send a value back to the place where the function was called

Syntax:
def function_name():
    return value
"""

# --------------------------------------------------
# Basic Example
# --------------------------------------------------
# def square(num):
#     return num * num

# result = square(5)
# print(result)    # 25


# --------------------------------------------------
# Returning a Single Value
# --------------------------------------------------
# def add(a, b):
#     return a + b

# res = add(2, 3)
# print("Result:", res)    # 5


# --------------------------------------------------
# Returning Value Using Conditions
# --------------------------------------------------
# def calculate_cost(menu):
#     if menu == "Ham and Cheese":
#         return 25
#     elif menu == "Nutella Sandwich":
#         return 30
#     elif menu == "Chicken Sandwich":
#         return 40
#     elif menu == "Corn Cheese Sandwich":
#         return 25
#     elif menu == "Aloo Grilled Sandwich":
#         return 25
#     else:
#         return 20

# menu = input("Enter sandwich name: ")
# print("Cost:", calculate_cost(menu))


# --------------------------------------------------
# Returning Multiple Values (Tuple)
# --------------------------------------------------
"""
A tuple is a comma-separated collection of values.
Python automatically packs multiple return values into a tuple.
"""

# def fun():
#     name = "GeeksforGeeks"
#     age = 20
#     return name, age

# name, age = fun()
# print(name)
# print(age)


# --------------------------------------------------
# Returning a List
# --------------------------------------------------
"""
A list can store multiple values of different types.
"""

# def fun():
#     name = "GeeksforGeeks"
#     age = 20
#     return [name, age]

# data = fun()
# print(data)


# --------------------------------------------------
# Returning a Dictionary
# --------------------------------------------------
"""
A dictionary stores data in key-value pairs.
"""

# def fun():
#     return {
#         "name": "GeeksforGeeks",
#         "age": 20
#     }

# data = fun()
# print(data)


# --------------------------------------------------
# Returning a Function (Function as Object)
# --------------------------------------------------
"""
In Python, functions are objects.
So a function can return another function.
"""

# def outer(x):
#     return x * 10

# def my_func():
#     return outer

# res = my_func()
# print(res(10))    # 100


# --------------------------------------------------
# Important Notes
# --------------------------------------------------
"""
1. return immediately stops function execution.
2. Code written after return will NOT execute.
3. A function without return returns None.
"""

# def test():
#     print("Hello")

# print(test())    # None



