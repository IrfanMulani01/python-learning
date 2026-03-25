"""
============================================================
ADVANCED PYTHON CONCEPTS (FILES 19–23 COMBINED)
============================================================

Includes:
19. Context Managers
20. Memory Management
21. Shallow vs Deep Copy
22. Mutable vs Immutable
23. Namespaces & Scope
"""

# ==========================================================
# 19. CONTEXT MANAGERS
# ==========================================================

"""
Context Manager:
----------------
A context manager is used to manage resources properly.
It automatically handles setup and cleanup actions.

Used with: `with` keyword
"""

# WITHOUT context manager (manual handling)
# file = open("data.txt", "w")
# file.write("Hello")
# file.close()

# WITH context manager (recommended)
# with open("data.txt", "w") as file:
#     file.write("Hello World")
# File closes automatically


# Custom Context Manager using class

# class MyContext:
#     def __enter__(self):
#         print("Resource acquired")
#         return self  # return something to use inside 'with' if needed

#     def __exit__(self, exc_type, exc_value, traceback):
#         print("Resource released")
#         # returning False lets any exception propagate
#         return False

# with MyContext():
#     print("Inside context")



# ==========================================================
# 20. MEMORY MANAGEMENT
# ==========================================================

"""
Memory Management:
------------------
Python automatically manages memory using:
1. Reference Counting
2. Garbage Collection
"""

# Reference Counting example
a = 10
b = a
c = a

# # Garbage Collection example
import gc

class Demo:
    pass

d1 = Demo()
d2 = d1

del d1
del d2

gc.collect()  # Forces garbage collection


# ==========================================================
# 21. SHALLOW COPY vs DEEP COPY
# ==========================================================

"""
Copying Objects:
----------------
Shallow Copy  → copies outer object only
Deep Copy     → copies entire object recursively
"""

# import copy

# original = [[1, 2], [3, 4]]

# shallow = copy.copy(original)
# deep = copy.deepcopy(original)

# original[0][0] = 99

# print("Original:", original)
# print("Shallow :", shallow)
# print("Deep    :", deep)


# ==========================================================
# 22. MUTABLE vs IMMUTABLE
# ==========================================================

"""
Mutable Objects:
----------------
Objects that can be changed after creation.

Examples: list, dict, set

Immutable Objects:
------------------
Objects that cannot be changed.

Examples: int, float, string, tuple
"""

# # Immutable example
# x = 10
# print("Before:", id(x))
# x = x + 5
# print("After :", id(x))  # New object

# # Mutable example
# lst = [1, 2, 3]
# print("Before:", id(lst))
# lst.append(4)
# print("After :", id(lst))  # Same object


# ==========================================================
# 23. NAMESPACES & SCOPE
# ==========================================================

"""
Namespace:
----------
A namespace is a container that stores variable names.

Scope:
------
Scope defines where a variable is accessible.
"""

# # Global Namespace
# x = 100

# def outer():
#     y = 200  # Enclosing scope

#     def inner():
#         z = 300  # Local scope
#         print(z)

#     inner()
#     print(y)

# # outer()
# # print(x)


# """
# LEGB Rule:
# ----------
# Python looks for variables in this order:
# L → Local
# E → Enclosing
# G → Global
# B → Built-in
# """

# # global keyword example
# count = 0

# def increment():
#     global count
#     count += 1

# # increment()
# # print(count)


"""
============================================================
END OF ADVANCED PYTHON CONCEPTS
============================================================
"""
