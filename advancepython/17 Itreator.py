"""
========================================
ITERATORS IN PYTHON
========================================

Definition:
-----------
An iterator is an object that allows you to traverse
through all the elements of a collection (like list, tuple, etc.)
one element at a time.

In simple words:
Iterator = Object that remembers its position while looping
"""

# ==================================================
# BASIC EXAMPLE (ITERABLE vs ITERATOR)
# ==================================================

"""
Iterable:
---------
An object that can return an iterator.
Example: list, tuple, string
"""

# numbers = [10, 20, 30, 40]   # iterable

# iterator_obj = iter(numbers)   # iterator created

# print(next(iterator_obj))  # 10
# print(next(iterator_obj))  # 20
# print(next(iterator_obj))  # 30
# print(next(iterator_obj))  # 40
# print(next(iterator_obj))  # StopIteration error


# ==================================================
# WHAT IS next() ?
# ==================================================

"""
next():
-------
Returns the next value from the iterator.
When no elements are left, it raises StopIteration.
"""


# ==================================================
# FOR LOOP INTERNAL WORKING (IMPORTANT)
# ==================================================

"""
for loop internally does this:
------------------------------
1. Calls iter()
2. Calls next() repeatedly
3. Stops when StopIteration occurs
"""

# for num in numbers:
#     print(num)


# ==================================================
# CREATING CUSTOM ITERATOR (CORE CONCEPT)
# ==================================================

"""
To create your own iterator:
----------------------------
You must define:
1. __iter__()  → returns iterator object
2. __next__()  → returns next value
"""

# class MyNumbers:
#     def __init__(self, limit):
#         self.limit = limit
#         self.current = 1

#     def __iter__(self):
#         return self

#     def __next__(self):
#         if self.current <= self.limit:
#             value = self.current
#             self.current += 1
#             return value
#         else:
#             raise StopIteration


# obj = MyNumbers(5)

# for num in obj:
#     print(num)


# ==================================================
# ITERATOR vs ITERABLE (INTERVIEW)
# ==================================================

"""
Iterable:
---------
✔ Can return an iterator
✔ Uses iter()
✔ Example: list, tuple, set

Iterator:
---------
✔ Keeps track of state
✔ Uses __next__()
✔ Returns values one by one
"""


# ==================================================
# DIFFERENCE: ITERATOR vs GENERATOR
# ==================================================

"""
Iterator:
---------
✔ Uses class
✔ Uses __iter__ and __next__
✔ More control

Generator:
----------
✔ Uses function
✔ Uses yield
✔ Less code
"""


# ==================================================
# REAL-WORLD USE CASE
# ==================================================

"""
Iterators are useful when:
--------------------------
✔ Working with large data
✔ Reading files line by line
✔ Saving memory
"""


# ==================================================
# QUICK SUMMARY (EXAM READY)
# ==================================================

"""
✔ Iterator traverses elements one by one
✔ iter() creates iterator
✔ next() gives next element
✔ StopIteration ends iteration
✔ Custom iterator uses __iter__ and __next__
"""
