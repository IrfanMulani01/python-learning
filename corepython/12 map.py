'''
====================================
PYTHON map() FUNCTION – SHORT NOTES
====================================

What is map()?
--------------
• map() is a built-in function
• It applies a function to each item of an iterable
• Returns a new iterator (convert to list/tuple if needed)
• Used for transforming data

Syntax:
-------
map(function, iterable)
map(function, iterable1, iterable2)

function  → function or lambda applied on items
iterable  → list, tuple, etc.
'''

# ------------------------------------
# BASIC EXAMPLE
# ------------------------------------

# words = ["python", "is", "interpreted", "language"]
# lengths = list(map(len, words))
# print(lengths)       

# ------------------------------------
# map() WITH NORMAL FUNCTION
# ------------------------------------

# def cube(x):
#     return x ** 3

# items = [1, 2, 3, 4, 5]
# result = list(map(cube, items))
# print(result)

# ------------------------------------
# map() WITH LAMBDA FUNCTION
# ------------------------------------

# items = [1, 2, 3, 4, 5]
# result = list(map(lambda x: x ** 3, items))
# print(result)

# ------------------------------------
# map() WITH MULTIPLE ITERABLES
# ------------------------------------

# a = [1, 2, 3]
# b = [10, 20, 30]
# result = list(map(lambda x, y: x * y, a, b))
# print(result)

# ------------------------------------
# map() WITH STRING FUNCTIONS
# ------------------------------------

# s = ["hello", "nature", "python"]
# result = list(map(str.upper, s))
# print(result)

# ------------------------------------
# map() WITH TUPLE
# ------------------------------------

# values = (1, 2, 3, 4)
# result = tuple(map(lambda x: (x, x**2), values))
# print(result)

# ------------------------------------
# map() WITH DICTIONARY DATA
# ------------------------------------

# measurements = [
#     {"length": 2, "width": 3},
#     {"length": 4, "width": 5},
# ]

# areas = list(map(lambda x: x["length"] * x["width"], measurements))
# print(areas)

# ------------------------------------
# map() RETURN TYPE
# ------------------------------------

# result = map(len, ("apple", "banana", "cherry"))
# print(type(result))      # <class 'map'>
# print(result)
# print(list(result))      # convert to list

# ------------------------------------
# PRACTICE EXAMPLES
# ------------------------------------

# nums = [20, 40, 30, 15, 50]
# result = list(map(lambda x: x + x, nums))
# print(result)

# num1 = [20, 60]
# num2 = [50, 100]
# result = list(map(lambda a, b: a + b, num1, num2))
# print(result)

# a = ['Apple', 'Banana', 'Pear']
# result = list(map(lambda x: x[0] == 'B', a))
# print(result)

'''
------------------------------------
INTERVIEW POINTS
------------------------------------
• map() applies function to every element
• Faster and cleaner than loops
• Returns map object (iterator)
• Commonly used with lambda
• Used for transformation, not filtering
'''

'''
====================================
END OF map() FUNCTION
====================================
'''
