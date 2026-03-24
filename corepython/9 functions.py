'''
====================================
FUNCTIONS IN PYTHON – COMPLETE
====================================

What is a Function?
-------------------
- A function is a block of reusable code.
- It runs only when it is called.
- Functions help reduce code duplication.
- Functions improve readability and maintenance.

Key Points:
-----------
- Data passed to a function is called a parameter.
- Data passed while calling a function is called an argument.
- A function can return a value using the return keyword.
'''

# ------------------------------------
# TYPES OF FUNCTIONS
# ------------------------------------
'''
1. User-defined Functions
2. Built-in Functions
'''

# ------------------------------------
# DEFINING A FUNCTION
# ------------------------------------
'''
Syntax:
def function_name(parameters):
    code block
    
function_name(argument)    
'''

# Example
# def fun():
    
#     print("Welcome to Function")

# fun()

# ------------------------------------
# FUNCTION WITH PARAMETERS
# ------------------------------------

# def names(fname, lname):
#     print(fname + " " + lname)

# names("Pratik")
# names('sushant','dongardive')

# ------------------------------------
# FUNCTION WITH LOGIC
# ------------------------------------

# def evenOdd(x):
#     if x % 2 == 0:
#         print("Even")
#     else:
#         print("Odd")

# evenOdd(4)
# evenOdd(5)

# ------------------------------------
# FUNCTION WITH MULTIPLE OPERATIONS
# ------------------------------------

# def calci(a, b):
#     print("Add =", a + b)
#     print("Sub =", a - b)
#     print("Mul =", a * b)
#     print("Div =", a / b)

# calci(10, 5)

# ------------------------------------
# DOCSTRINGS
# ------------------------------------
'''
Docstring:
----------
- A documentation string written inside a function.
- Used to explain what the function does.
- Written using triple quotes.
- Accessed using __doc__ or help().
'''

# # Single-line Docstring
# def vacation():
#     '''vacation functions greets.'''
#     print("Welcome")
    

# print(vacation.__doc__)
# vacation()

# Multi-line Docstring

# def any_fun(x):
#     """
#     This function explains docstrings.

#     Parameters:
#     x (int): input value

#     Returns:
#     int
#     """

# print(any_fun.__doc__)

# ------------------------------------
# TYPES OF FUNCTION ARGUMENTS
# ------------------------------------
'''
1. Positional Arguments
2. Keyword Arguments
3. Default Arguments
4. Variable Length Arguments
'''

# ------------------------------------
# 1. POSITIONAL ARGUMENTS
# ------------------------------------
'''
- Arguments are passed in order.
- Order must match the parameters.
'''

# def add(a, b):
#     print(a + b)

# add(10,20)

# def first(name, age):
#     print(name)
#     print(age)

# first(11,"Max")

# ------------------------------------
# 2. KEYWORD ARGUMENTS
# ------------------------------------
'''
- Arguments passed using parameter names.
- Order does not matter.
'''

def greet(name, age):
    print("Name:", name)
    print("Age:", age)

# greet(age=25, name="Navanath")

# Combination of positional + keyword
# greet("Navanath", age=25)
# greet(age=25,"Navanath")

# ------------------------------------
# 3. DEFAULT ARGUMENTS
# ------------------------------------
'''
- Default value is used if no argument is passed.
'''

# def my_function(country="India"):
#     print("I am from", country)

# my_function("Sweden")
# my_function()
# my_function("Brazil")

# def student(name, age, grade="Six", school="ABC"):
#     print(name, age, grade, school)

# student("Roshan", 12)
# student("Priyanka", 21, "Seven", "Sungrace")

# ------------------------------------
# 4. VARIABLE LENGTH ARGUMENTS
# ------------------------------------
'''
Used when number of arguments is unknown.

Types:
------
1. *args  → Tuple (positional)
2. **kwargs → Dictionary (keyword)
'''

# ------------------------------------
# *args (Arbitrary Positional Arguments)
# ------------------------------------

# def num(*num1):
#     print(num1)

# num(1, 2, 3, 4, 5)

# def percentage(*marks):
#     total = sum(marks)
#     avg = total / len(marks)
#     print("Average =", avg)

# percentage(56, 61, 73)

# ------------------------------------
# **kwargs (Arbitrary Keyword Arguments)
# ------------------------------------

# def details(**kwargs):
#     print(kwargs)

# details(name="Max", age=20, city="Pune")

# def display(**kwargs):
#     for k, v in kwargs.items():
#         print(k, ":", v)
# # #
# display(name="Raj", avg=98.9, rno=100)

# ------------------------------------
# *args AND **kwargs TOGETHER
# ------------------------------------

# def all_aboard(a, *args, **kwargs):
#     print(a)
#     print(args)
#     print(kwargs)
# #
# all_aboard(2, 56, 89, x=3, y=0)

# ------------------------------------
# PASSING LIST & RETURN VALUE
# ------------------------------------

# def maximum(a, b, c):
#     values = [a, b, c]
#     return max(values)

# print("Maximum =", maximum(10, 20, 30))

'''
====================================
END OF FUNCTIONS IN PYTHON
====================================
'''



# def even(n):
#     rem=n%2
#     if rem == 0:
#         return True
#     else:
#         return False
# print(even(5))   
 