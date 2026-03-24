"""
==============================
PYTHON BUILT-IN FUNCTIONS
==============================

Built-in functions are functions that are already available in Python.
We do not need to import any module to use most of them.
"""

# --------------------------------------------------
# 1. abs()
# --------------------------------------------------
"""
abs() returns the absolute value of a number.
Absolute value means distance from zero (no sign).
Works with int, float, and complex numbers.
"""

# print(abs(-5))        # 5
# print(abs(-3.14))     # 3.14
# print(abs(3 + 4j))    # 5.0


# --------------------------------------------------
# 2. all()
# --------------------------------------------------
"""
all() returns True if all elements in an iterable are True.
If any element is False, it returns False.
Empty iterable → True
"""

# print(all([1, 2, 3]))          # True
# print(all([1, 0, 3]))          # False
# print(all([True, True]))       # True
# print(all([]))                 # True


# --------------------------------------------------
# 3. bin()
# --------------------------------------------------
"""
bin() converts an integer into a binary string.
Binary numbers start with '0b'.
"""

# print(bin(10))      # 0b1010
# print(bin(7))       # 0b111


# --------------------------------------------------
# 4. bool()
# --------------------------------------------------
"""
bool() converts a value to True or False.

False values:
0, 0.0, None, False, "", [], {}, (), set()

All other values → True
"""

# print(bool(0))          # 
# print(bool(""))         # 
# print(bool([]))         # 
# print(bool("Python"))   # 
# print(bool([0]))        # 


# --------------------------------------------------
# 5. callable()
# --------------------------------------------------
"""
callable() checks whether an object can be called like a function.
"""

# x = 10
# print(callable(x))      

# def fun():
#     pass

# print(callable(fun))    


# --------------------------------------------------
# 6. exec()
# --------------------------------------------------
"""
exec() executes Python code stored in a string.
Used for dynamic code execution.
"""

# exec("print('Hello from exec')")

# exec("""
# for i in range(3):
#     print(i)
# """)


# --------------------------------------------------
# 7. sum()
# --------------------------------------------------
"""
sum() returns the sum of elements in an iterable.
Optional second argument is the starting value.
"""

# print(sum([1, 2, 3]))          # 6
# print(sum([1, 2, 3], 10))      # 16


# --------------------------------------------------
# 8. any()
# --------------------------------------------------
"""
any() returns True if at least one element is True.
If all elements are False → returns False.
"""

# print(any([0, False, 5]))      
# print(any([0, False, 0]))      


# --------------------------------------------------
# 9. eval()
# --------------------------------------------------
"""
eval() evaluates a string as a Python expression and returns the result.
Use carefully (security risk).
"""

# x = 10
# print(eval("x * x"))           # 100
# print(eval("5 + 3 * 2"))       # 11


# --------------------------------------------------
# 10. enumerate()
# --------------------------------------------------
"""
# enumerate() adds index to iterable elements.
# Returns (index, value) pairs.
# """

# fruits = ["apple", "banana", "cherry"]

# for index, value in enumerate(fruits):
#     print(index, value)

# print(list(enumerate(fruits)))


# --------------------------------------------------
# 11. frozenset()
# --------------------------------------------------
"""
frozenset() creates an immutable set.
Elements cannot be added or removed.
Useful as dictionary keys.
"""

# fs = frozenset([1, 2, 3])
# print(fs)

# fs.add(4)   # Error (immutable)


# --------------------------------------------------
# 12. divmod()
# --------------------------------------------------
"""
divmod(a, b) returns (quotient, remainder)
"""

# print(divmod(10, 3))     # (3, 1)


# --------------------------------------------------
# 13. ord()
# --------------------------------------------------
"""
ord() returns Unicode code of a character.
"""

# print(ord('A'))    # 65
# print(ord('a'))    # 97
# print(ord('$'))    # 36


# --------------------------------------------------
# 14. oct(), hex(), pow()
# --------------------------------------------------
"""
oct() → octal representation
hex() → hexadecimal representation
pow(a, b) → a raised to power b
"""

# print(oct(10))      # 0o12
# print(hex(15))      # 0xf
# print(pow(2, 5))    # 32
