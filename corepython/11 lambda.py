'''
====================================
PYTHON LAMBDA FUNCTION – ALL IN ONE
====================================

What is a Lambda Function?
-------------------------
A lambda function is a small anonymous function.
Anonymous means the function has no name.

• Lambda functions are used for short and simple operations
• They can take any number of arguments
• They can have ONLY ONE expression
• The result of that expression is automatically returned

------------------------------------
KEY POINTS
------------------------------------
• Lambda functions do NOT use the 'def' keyword
• They do NOT have a function name
• They do NOT use the return keyword
• Mostly used for quick calculations
'''

# ------------------------------------
# LAMBDA SYNTAX
# ------------------------------------
'''
Syntax:
lambda arguments : expression

Where:
• lambda     → keyword to define anonymous function
• arguments  → input values
• expression → single line operation whose result is returned
'''

# ------------------------------------
# BASIC LAMBDA EXAMPLES
# ------------------------------------

# add = lambda a, b: a + b
# print(add(10, 20))

# greet = lambda: "Good Vibes Only"
# print(greet())

# multiply = lambda a, b, c: a * b * c
# print(multiply(10, 5, 2))

# ------------------------------------
# SINGLE ARGUMENT LAMBDA
# ------------------------------------

# add_ten = lambda x: x + 10
# print(add_ten(5))

# ------------------------------------
# MULTIPLE ARGUMENT LAMBDA
# ------------------------------------

# total = lambda a, b, c: a + b + c
# print(total(10, 15, 20))

# ------------------------------------
# IMMEDIATE EXECUTION (IIFE STYLE)
# ------------------------------------

# print((lambda x, y, z: x + y + z)(3, 8, 1))

# ------------------------------------
# STRING OPERATIONS WITH LAMBDA
# ------------------------------------

# full_name = lambda first, last: f"{first.title()} {last.title()}"
# print(full_name("guido", "van rossum"))

# text = "procedural"
# reverse_upper = lambda s: s.upper()[::-1]
# print(reverse_upper(text))

# ------------------------------------
# LAMBDA WITH VARIABLE LENGTH ARGUMENTS
# ------------------------------------

# sum_values = lambda *x: x[0] + x[1] + x[2] + x[3]
# print(sum_values(5, 10, 15, 20))

# ------------------------------------
# LAMBDA VS NORMAL FUNCTION
# ------------------------------------
'''
Normal Function:
----------------
• Uses def keyword
• Can contain multiple statements
• Uses return keyword
• Can have docstring

Lambda Function:
----------------
• Uses lambda keyword
• Only ONE expression
• No return keyword
• No docstring
'''

# def cube(y):
#     return y * y * y

# cube_lambda = lambda y: y * y * y

# print("Using def:", cube(5))
# print("Using lambda:", cube_lambda(5))

# ------------------------------------
# LAMBDA WITH LIST COMPREHENSION
# ------------------------------------

# functions = [lambda x=i: x * 10 for i in range(1, 5)]
# print(functions)

# for func in functions:
#     print(func())

# ------------------------------------
# LAMBDA WITH IF-ELSE (EXPRESSION)
# ------------------------------------
'''
Note:
Lambda supports if-else expression
But NOT if-elif-else statements
'''

# maximum = lambda a, b: a if a > b else b
# print(maximum(5, 2))

# check = lambda x: x if x > 10 else 22
# print(check(1))



# ------------------------------------
# WHERE LAMBDA IS MOSTLY USED
# ------------------------------------
'''
• map()
• filter()
• reduce()
• Sorting
• Short one-line logic
'''

# ------------------------------------
# PROS OF LAMBDA FUNCTION
# ------------------------------------
'''
1. Short and concise syntax
2. Ideal for one-time use
3. Can be passed as argument to other functions
4. Improves readability for simple logic
'''

# ------------------------------------
# CONS OF LAMBDA FUNCTION
# ------------------------------------
'''
1. Only one expression allowed
2. No multiple statements
3. No docstring support
4. Hard to debug if logic becomes complex
'''

'''
====================================
END OF PYTHON LAMBDA FUNCTION
====================================
'''
