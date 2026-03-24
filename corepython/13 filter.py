'''
====================================
PYTHON filter() FUNCTION – SHORT NOTES
====================================

What is filter()?
-----------------
• filter() is a built-in Python function
• It is used to select elements from an iterable
• The function must return True or False
• Only elements that return True are kept

Syntax:
-------
filter(function, iterable)

function → returns True or False
iterable → list, tuple, string, etc.
'''

# ------------------------------------
# BASIC EXAMPLE
# ------------------------------------

# numbers = [-2, -1, 0, 1, 2]
# positive = list(filter(lambda x: x > 0, numbers))
# print(positive)        # [1, 2]

# ------------------------------------
# filter() WITH NORMAL FUNCTION
# ------------------------------------

# def is_positive(n):
#     return n > 0

# numbers = [-2, -1, 0, 1, 2]
# result = list(filter(is_positive, numbers))
# print(result)

# ------------------------------------
# filter() WITH LAMBDA FUNCTION
# ------------------------------------

# nums = [1, 2, 3, 4, 5, 6]
# evens = list(filter(lambda x: x % 2 == 0, nums))
# print(evens)

# ------------------------------------
# filter() WITH STRINGS
# ------------------------------------

# letters = ['u', 'a', 'q', 'c', 'i', 'd', 'e']
# vowels = list(filter(lambda x: x in 'aeiou', letters))
# print(vowels)

# ------------------------------------
# filter() WITH RANGE
# ------------------------------------

# numbers = list(filter(lambda x: x % 2 == 0, range(1, 20)))
# print(numbers)

# ------------------------------------
# filter() WITH None
# ------------------------------------
'''
If function is None:
• filter() removes all falsy values
Falsy values:
0, False, None, "", [], {}, ()
'''


# values = [1, 0, False, True, "", "Python", [], {}, 5]
# result = list(filter(None, values))
# print(result)

# ------------------------------------
# filter() WITH MULTIPLE LISTS (INTERSECTION)
# ------------------------------------

# a = [1, 3, 4, 5, 7]
# b = [2, 3, 5, 6]

# common = list(filter(lambda x: x in a, b))
# print(common)

# ------------------------------------
# filter() WITH LIST OF DICTIONARIES
# ------------------------------------

# books = [
#     {"title": "Book A", "price": 500},
#     {"title": "Book B", "price": 730},
#     {"title": "Book C", "price": 400}
# ]

# expensive_books = list(filter(lambda x: x["price"] > 500, books))

# for book in expensive_books:
#     print(book["title"])

'''
------------------------------------
INTERVIEW POINTS
------------------------------------
• filter() selects elements (does NOT modify them)
• Function must return True or False
• Returns filter object (iterator)
• Commonly used with lambda
• Used for filtering, not transformation
'''

'''
====================================
END OF filter() FUNCTION
====================================
'''
