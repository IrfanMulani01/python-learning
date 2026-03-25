"""
========================================
GENERATORS IN PYTHON
========================================

Definition:
-----------
A generator is a special type of function
that returns values one by one
using the 'yield' keyword
instead of returning all values at once.

Generators are memory efficient.
"""

# ==================================================
# WHY GENERATORS ARE USED
# ==================================================

"""
✔ Save memory
✔ Work with large data
✔ Produce values on demand
"""

# ==================================================
# NORMAL FUNCTION vs GENERATOR
# ==================================================

# Normal function
# def numbers():
#     return [1, 2, 3, 4]
# print(numbers())

# Generator function
# def numbers_gen():
#     yield 1
#     yield 2
#     yield 3
#     yield 4
# g=numbers_gen()

# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
"""
PROGRAM LOGIC:
--------------
Normal function:
1. Creates full list in memory
2. Returns all values at once

Generator:
1. Does NOT store all values
2. Returns values one by one
3. Uses yield instead of return
"""

# ==================================================
# BASIC GENERATOR FUNCTION
# ==================================================

# def simple_generator():
#     yield "A"
#     yield "B"
#     yield "C"

# g = simple_generator()
# print(next(g))
# print(next(g))
# print(next(g))

"""
PROGRAM LOGIC:
--------------
1. Function execution pauses at yield
2. Value is returned
3. State is saved
4. next() resumes execution
"""

# ==================================================
# GENERATOR USING LOOP
# ==================================================

# def count_numbers(n):
#     for i in range(n):
#         yield i

# g = count_numbers(5)
# for num in g:
#     print(num)

"""
PROGRAM LOGIC:
--------------
1. Loop runs step-by-step
2. Each iteration yields one value
3. Loop resumes where it stopped
"""

# ==================================================
# GENERATOR EXPRESSION
# ==================================================

# gen = (x * x for x in range(5))
# for value in gen:
#     print(value)

"""
PROGRAM LOGIC:
--------------
1. Similar to list comprehension
2. Values generated lazily
3. Memory efficient
"""

# ==================================================
# GENERATOR WITH CONDITION
# ==================================================

# def even_numbers(n):
#     for i in range(n):
#         if i % 2 == 0:
#             yield i

# for num in even_numbers(10):
#     print(num)

"""
PROGRAM LOGIC:
--------------
1. Condition is checked
2. Only valid values are yielded
"""

# ==================================================
# yield vs return
# ==================================================

"""
yield:
------
✔ Pauses function
✔ Saves state
✔ Returns multiple values

return:
-------
✔ Ends function
✔ Returns single value
"""

# ==================================================
# MULTIPLE yield STATEMENTS
# ==================================================

# def mixed_generator():
#     yield 10
#     yield 20
#     yield 30

# for value in mixed_generator():
#     print(value)

"""
PROGRAM LOGIC:
--------------
1. Each yield sends one value
2. Function continues until completion
"""

# ==================================================
# GENERATOR WITH next()
# ==================================================

# def demo():
#     yield 1
#     yield 2

# d = demo()
# print(next(d))
# print(next(d))
# print(d)

"""
PROGRAM LOGIC:
--------------
1. next() requests next value
2. Raises StopIteration after end
"""

# ==================================================
# REAL-WORLD EXAMPLE (READ LARGE DATA)
# ==================================================

# def read_numbers():
#     for i in range(1, 1000000):
#         yield i
#     print(i)
# g=read_numbers()
# print(next(g))  
# print(next(g)) 
# print(next(g))  
"""
PROGRAM LOGIC:
--------------
1. Large data not stored in memory
2. Values generated when needed
"""

# ==================================================
# GENERATORS IN INTERVIEW
# ==================================================

"""
✔ Memory optimization
✔ Lazy evaluation
✔ Used in data streaming
"""

# ==================================================
# IMPORTANT POINTS
# ==================================================

"""
✔ Generator uses yield
✔ next() fetches value
✔ Stops automatically
"""

# ==================================================
# QUICK SUMMARY (EXAM READY)
# ==================================================

"""
Generators:
-----------
Functions that produce values
one at a time using yield

Benefits:
✔ Memory efficient
✔ Faster for large data
"""
