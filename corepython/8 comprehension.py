'''
====================================
PYTHON COMPREHENSIONS – COMPLETE
====================================

What is Comprehension?
---------------------
Comprehension is a short and clean way to create:
• List
• Tuple (via generator)
• Set
• Dictionary

Instead of writing multiple lines of code using loops,
we can write everything in ONE line.

General Syntax
--------------
new_collection = [expression for item in iterable if condition]
'''

# ------------------------------------
# WHY USE COMPREHENSIONS?
# ------------------------------------
'''
Advantages:
- Code becomes shorter
- Easy to read
- Faster execution

'''

# ------------------------------------
# LIST COMPREHENSION
# ------------------------------------
'''
List comprehension creates a new list using a single line of code.
'''

# Normal way
# squares = []
# for i in range(1, 6):
#     squares.append(i * i)
# print(squares)

# Using List Comprehension
# squares = [i * i for i in range(1, 6)]
# print(squares)

'''
Explanation:
- i * i → expression
- for i in range(1, 6) → loop
'''

# ------------------------------------
# LIST COMPREHENSION WITH CONDITION
# ------------------------------------
'''
Create a list of even numbers.
'''

# evens = [i for i in range(1, 11) if i % 2 == 0]
# print(evens)

'''
Explanation:
- if condition filters values
'''

# ------------------------------------
# LIST COMPREHENSION WITH IF-ELSE
# ------------------------------------
'''
Replace even numbers with "Even" and odd with "Odd".
'''

# result = ["Even" if i % 2 == 0 else "Odd" for i in range(1, 6)]
# print(result)




# ------------------------------------
# TUPLE COMPREHENSION (GENERATOR)
# ------------------------------------
'''
Python does NOT support direct tuple comprehension.
Instead, it creates a generator object.
'''

# gen = (i * i for i in range(1, 6))
# print(gen)          # generator object
# print(tuple(gen))   # convert to tuple

'''
Explanation:
- () creates generator
- tuple() converts it into tuple
'''

# ------------------------------------
# SET COMPREHENSION
# ------------------------------------
'''
Set comprehension creates a set.
Duplicates are automatically removed.
'''

# nums = [1, 2, 2, 3, 4, 4, 5]
# unique = {i for i in nums}
# print(unique)

# ------------------------------------
# SET COMPREHENSION WITH CONDITION
# ------------------------------------
'''
Create a set of even numbers.
'''

# evens = {i for i in range(1, 11) if i % 2 == 0}
# print(evens)

# ------------------------------------
# DICTIONARY COMPREHENSION
# ------------------------------------
'''
Dictionary comprehension creates key-value pairs.
'''

# squares = {i: i * i for i in range(1, 6)}
# print(squares)

'''
Explanation:
- i → key
- i * i → value
'''

# ------------------------------------
# DICTIONARY COMPREHENSION WITH CONDITION
# ------------------------------------
'''
Store only even numbers and their squares.
'''

# even_squares = {i: i * i for i in range(1, 11) if i % 2 == 0}
# print(even_squares)

# ------------------------------------
# CONVERT LIST TO DICTIONARY
# ------------------------------------
'''
Convert list of numbers into number: square dictionary.
'''

# nums = [1, 2, 3, 4]
# result = {i: i * i for i in nums}
# print(result)

# ------------------------------------
# STRING COMPREHENSION (CHAR LIST)
# ------------------------------------
'''
Convert string into list of characters.
'''

# word = "Python"
# chars = [ch for ch in word]
# print(chars)

# ------------------------------------
# COMPREHENSION WITH FUNCTION
# ------------------------------------
'''
Apply function inside comprehension.
'''

# def square(x):
#     return x * x

# result = [square(i) for i in range(1, 6)]
# print(result)

# ------------------------------------
# INTERVIEW IMPORTANT POINTS
# ------------------------------------
'''
1. List comprehension returns a list
2. Tuple comprehension returns a generator
3. Set comprehension removes duplicates
4. Dictionary comprehension uses key:value
5. if-else position matters
6. More readable but avoid very complex logic
'''

'''
====================================
END OF COMPREHENSIONS
====================================
'''
