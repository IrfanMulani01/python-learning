"""

# PYTHON OPERATORS (TEACHING NOTES)

Python operators are special symbols or keywords used to perform operations
on variables and values.

They are essential for:
• Performing calculations
• Making decisions (if-else)
• Manipulating data
• Writing logical conditions



"""

# ---------------------------------

# 1. ARITHMETIC OPERATORS

# ---------------------------------

"""
Arithmetic operators perform basic mathematical operations.

Operators:

* Addition

- Subtraction

* Multiplication
  /   Division (returns float)
  //  Floor Division
  %   Modulus (remainder)
  **  Exponentiation (power)
  """

# Example

# a = 10

# b = 3

# print(a + b)    # 13

# print(a - b)    # 7

# print(a * b)    # 30

# print(a / b)    # 3.33

# print(a // b)   # 3

# print(a % b)    # 1

# print(a ** b)   # 1000

# ---------------------------------

# 2. ASSIGNMENT OPERATORS

# ---------------------------------

"""
Assignment operators are used to assign and update values.

Operators:
=    Assign
+=   Add and assign
-=   Subtract and assign
*=   Multiply and assign
/=   Divide and assign
//=  Floor divide and assign
%=   Modulus and assign
**=  Power and assign
"""

# Example

# x = 10

# x += 5

# x *= 2

# print(x)

# ---------------------------------

# 3. COMPARISON OPERATORS

# ---------------------------------

"""
Comparison operators compare two values and return True or False.
Used mainly in conditions.

Operators:
==   Equal to
!=   Not equal to

 > Greater than
 <    Less than
 >=   Greater than or equal to
 <=   Less than or equal to
 """

# Example

# a = 10

# b = 5

# print(a == b)

# print(a > b)

# ---------------------------------

# 4. LOGICAL OPERATORS

# ---------------------------------

"""
Logical operators combine multiple conditions.

Operators:
and   True if both conditions are True
or    True if any condition is True
not   Reverse the condition
"""

# Example

# age = 20

# citizen = True

# print(age >= 18 and citizen)

# ---------------------------------

# 5. BITWISE OPERATORS

# ---------------------------------

"""
Bitwise operators work on binary values.
Mostly used in low-level programming.

Operators:
&   AND
|   OR
^   XOR
~   NOT
<<  Left shift

> > Right shift
> > """

# ---------------------------------

# 6. IDENTITY OPERATORS

# ---------------------------------

"""
Identity operators compare memory location, not values.

Operators:
is       Same object
is not   Different object
"""

# Example

# a = [1, 2, 3]

# b = [1, 2, 3]

# print(id(a))

# c = a
# print(id(c))
# print(id(b))

# print(a is c)

# print(a is b)
# 
# print(a == b)

# ---------------------------------

# 7. MEMBERSHIP OPERATORS

# ---------------------------------

"""
Membership operators check whether a value exists in a sequence.

Operators:
in       Value present
not in   Value not present
"""

# Example

# names = ["ram", "shyam", "geeta"]

# print("ram" in names)

# print("hari" not in names)

# ---------------------------------

# END OF PYTHON OPERATORS

# ---------------------------------
