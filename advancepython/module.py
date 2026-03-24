#  Modules in Python


## What is a Module?

# * A module in Python is simply a '.py' file containing Python code (functions, classes, variables).
# * It allows you to organize code into smaller, reusable parts.

#  Example:

## mymodule.py

# def greet(name):
#     return f"Hello, {name}!"


## main.py

# import mymodule
# print(mymodule.greet("Atharva"))



## Why use Modules?

# * Code Reusability → Write once, use multiple times.
# * Maintainability → Easier to manage large projects.
# * Readability → Code is well-organized and clear.
# * Avoids Duplication → Functions can be reused.

'''
## Key Elements of Modules

| Element             | Meaning                                                  |
| ------------------- | -------------------------------------------------------- |
| **Module**          | A `.py` file containing functions, classes, or variables |
| **import**          | Keyword to use another module in your program            |
| **from … import …** | Import only a specific function/class from a module      |
| **as**              | Gives an alias (short name) to a module                  |
| **dir()**           | Shows all available names inside a module                |

'''

## Importing Modules

## 1. Basic Import

# import math
# print(math.sqrt(16))


# ## 2. Import with Alias

# import math as m
# print(m.pi)


# ## 3. Import Specific Function

# from math import sqrt, pi
# print(sqrt(25))
# print(pi)


# ## 4. Import All (not recommended)

# from math import *
# print(sin(90))




## Built-in Modules

# Python provides many built-in modules:

# * 'math' → mathematical operations

# import math

# # Square root
# print("Square root of 16:", math.sqrt(16))

# # Power
# print("2 raised to 3:", math.pow(2, 3))

# # Factorial
# print("Factorial of 5:", math.factorial(5))

# # Ceiling and Floor
# print("Ceiling of 4.2:", math.ceil(4.2))   # rounds up
# print("Floor of 4.8:", math.floor(4.8))   # rounds down

# # Pi and Euler's number
# print("Value of pi:", math.pi)
# print("Value of e:", math.e)

# # Trigonometric functions
# print("sin(90°):", math.sin(math.radians(90)))
# print("cos(0°):", math.cos(math.radians(0)))

# # Logarithm
# print("Log base e of 10:", math.log(10))
# print("Log base 10 of 1000:", math.log10(1000))




# * 'os' → interact with the operating system

import os

# Get current working directory
# print("Current Directory:", os.getcwd())

# # List files in current directory
# print("Files:", os.listdir())

# # Create a new folder
# os.mkdir("test_folder")
# print("Folder 'test_folder' created")

# # Rename folder
# os.rename("test_folder", "renamed_folder")
# print("Folder renamed to 'renamed_folder'")

# # Remove folder
# os.rmdir("renamed_folder")
# print("Folder removed")


# # * 'random' → random number generation

import random

# Random integer between 1 and 10
# print("Random int:", random.randint(1, 10))

# # Random floating number between 0 and 1
# print("Random float:", random.random())

# # # Random choice from a list
# fruits = ["apple", "banana", "cherry"]
# print("Random choice:", random.choice(fruits))

# Shuffle a list
# numbers = [1, 2, 3, 4, 5]
# random.shuffle(numbers)
# print("Shuffled list:", numbers)


# # * 'datetime' → date and time functions

# import datetime

# Get current date and time
# now = datetime.datetime.now()
# print("Current Date & Time:", now)

# Get only date
# print("Today's Date:", now.date())

# # Get only time
# print("Current Time:", now.time())

# # Create a specific date
# d = datetime.date(2025, 8, 19)
# print("Custom Date:", d)

# # Add 7 days to current date
# future = now + datetime.timedelta(days=7)
# print("Date after 7 days:", future)



# # * 'sys' → system-specific parameters and functions

import sys

# # Version of Python
# print("Python version:", sys.version)

# # List of command-line arguments
# print("Command line args:", sys.argv)

# Exit the program (0 = successful)
# sys.exit(0)

# Max integer supported
# print("Max size of int:", sys.maxsize)

# # Path of all module search locations
# print("Python Module Search Paths:")
# for path in sys.path:
#     print(path)




##Example:


# import random
# print(random.randint(1,10))  # Random number between 1 and 10




## User-Defined Modules

##  *You can create your own module (".py" file) and import it into another.

## Example:

## calculator.py

# def add(a,b):
#     return a+b
# def sub(a,b):
#     return a-b

##  main.py

# import calculator
# print(calculator.add(5,3))
# print(calculator.sub(10,4))


## Packages (Collection of Modules)

# * A package is a folder that contains multiple modules.
# * It must include an '__init__.py' file to be recognized as a package.

'''
## Example structure:


mypackage/
 -   __init__.py
 -   module1.py
 -   module2.py

'''

# from mypackage import module1



## Theory Summary

## * A Module = Python file ('.py') with functions, classes, variables.
## * Use 'import' to bring in modules.
## * Built-in modules → provided by Python ('math', 'random', 'os', 'datetime', 'sys').
## * User-defined modules → your own '.py' files.
## * Packages = collection of modules in a folder with '__init__.py'.


##In short: Modules in Python = break code into separate files → import them → reuse anywhere.