'''
====================================
PYTHON reduce() FUNCTION – SHORT NOTES
====================================

What is reduce()?
-----------------
• reduce() is used to apply a function repeatedly on elements of an iterable
• It reduces the iterable to a single value
• reduce() is not built-in, so we must import it

Module:
-------
from functools import reduce

Syntax:
-------
reduce(function, iterable)  

function → takes TWO arguments
iterable → list, tuple, etc.
'''

from functools import reduce

# ------------------------------------
# BASIC EXAMPLE – MULTIPLICATION
# ------------------------------------

# numbers = [1, 2, 3, 4]

# def multiply(x, y):
#     return x * y

# result = reduce(multiply, numbers)
# print(result)        

'''
Working:
multiply(1, 2) → 2
multiply(2, 3) → 6
multiply(6, 4) → 24
'''

# ------------------------------------
# reduce() WITH LAMBDA – SUM
# ------------------------------------

# numbers = [10, 20, 30]
# result = reduce(lambda x, y: x + y, numbers)
# print(result)      

# ------------------------------------
# FIND MAX VALUE USING reduce()
# ------------------------------------

# numbers = [3, 8, 2, 10, 6]

# def find_max(x, y):
#     return x if x > y else y
  

# result = reduce(find_max, numbers)
# print(result) 


'''
Working:
find_max(3, 8) → 8
find_max(8, 2) → 8
find_max(8, 10) → 10
find_max(10, 6) → 10
'''

# ------------------------------------
# STRING CONCATENATION
# ------------------------------------

# words = ['Python', 'is', 'awesome']
# result = reduce(lambda x, y: x + " " + y, words)
# print(result)

# ------------------------------------

# ------------------------------------


