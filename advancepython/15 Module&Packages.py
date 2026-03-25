"""
========================================
MODULES AND PACKAGES IN PYTHON
========================================

Definition:
-----------
Modules and packages help organize Python code
into reusable and manageable parts.
"""

# ==================================================
# MODULE (DEFINITION)
# ==================================================

"""
What is a Module?
-----------------
A module is a Python file (.py) that contains:
✔ variables
✔ functions
✔ classes

It allows code reuse and better organization.
"""

# ==================================================
# CREATING A MODULE
# ==================================================

"""
Create a file named: math_utils.py
"""

# math_utils.py
# ----------------
# def add(a, b):
#     return a + b
#
# def sub(a, b):
#     return a - b

# ==================================================
# IMPORTING A MODULE
# ==================================================

# import math_utils
# print(math_utils.add(10, 5))
# print(math_utils.sub(10, 5))

# ==================================================
# IMPORT SPECIFIC FUNCTIONS
# ==================================================

# from math_utils import add
# print(add(5, 3))

# ==================================================
# IMPORT WITH ALIAS
# ==================================================

# import math_utils as mu
# print(mu.add(2, 2))

# ==================================================
# BUILT-IN MODULE EXAMPLES
# ==================================================

"""
✔ math
✔ random
✔ datetime
✔ os
✔ sys
"""

# import math
# print(math.sqrt(16))

# ==================================================
# PACKAGE (DEFINITION)
# ==================================================

"""
What is a Package?
------------------
A package is a collection of modules
organized inside a directory.

It must contain __init__.py (for older versions).
"""

# ==================================================
# PACKAGE STRUCTURE
# ==================================================

"""
my_package/
│
├── __init__.py
├── operations.py
├── display.py
"""

# operations.py
# ----------------
# def multiply(a, b):
#     return a * b

# display.py
# -------------
# def show(msg):
#     print(msg)

# ==================================================
# USING A PACKAGE
# ==================================================

# from my_package import operations
# print(operations.multiply(4, 5))

# from my_package.display import show
# show("Hello Package")

# ==================================================
# PROGRAM LOGIC
# ==================================================

"""
1. Module → single .py file
2. Package → folder of modules
3. import keyword loads code
4. Code becomes reusable
"""

# ==================================================
# __name__ == "__main__"
# ==================================================

"""
Used to control code execution
when module is imported.
"""

# def main():
#     print("Main function executed")
#
# if __name__ == "__main__":
#     main()

# ==================================================
# IMPORTANT POINTS
# ==================================================

"""
✔ One file = module
✔ Folder of modules = package
✔ import makes code reusable
✔ Avoid duplicate code
"""

# ==================================================
# QUICK SUMMARY (EXAM READY)
# ==================================================

"""
Module:
-------
Single Python file

Package:
--------
Collection of modules
"""
