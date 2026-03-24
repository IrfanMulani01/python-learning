# Packages in Python

## Definition

# * A Package in Python is a way to organize related modules into a directory (folder).
# * It is essentially a folder containing multiple Python modules (.py files).
# * A package must contain a special file named `__init__.py`, which tells Python that the folder
# should be treated as a package.
# * Package = container of modules
# * Useful for code organization, modularity, and reusability in large projects.

'''
## Structure of a Package


my_package/                  ← Package (Folder)
  -  __init__.py              ← Initializes the package
  - module1.py               ← Module 1
  -  module2.py               ← Module 2
  -  sub_package/             ← Sub-package
      -  __init__.py
      - sub_module1.py

'''

'''

__init__.py

  * Required in older versions of Python (still used today).
  * Can be empty OR contain initialization code.
  * Makes the folder behave like a package.

'''


## Importing from a Package


# Import entire module
# import my_package.module1  

# # Import specific function/class
# from my_package.module1 import func1  

# # Import from sub-package
# from my_package.sub_package import sub_module1  


##  Example

'''

# Folder Structure:


math_operations/
  -  __init__.py
  - addition.py
  - subtraction.py

'''


# addition.py


# def add(a, b):
#     return a + b

# subtraction.py


# def sub(a, b):
#     return a - b


# main.py


# from math_operations.addition import add
# from math_operations.subtraction import sub

# print(add(5, 3))  # Output: 8
# print(sub(5, 3))  # Output: 2

'''

##  Summary Table

| Element           | Meaning                                            |
| ----------------- | -------------------------------------------------- |
| **Package**       | A folder that contains multiple Python modules     |
| **Module**        | A single Python file (.py)                         |
| **`__init__.py`** | Initializes the package, marks folder as a package |
| **Sub-package**   | A package inside another package                   |
| **Import**        | Used to access modules or functions from a package |

---

## 🔹 When to Use Packages?

| Reason                             | Benefit                                    |
| ---------------------------------- | ------------------------------------------ |
| To organize large codebases        | Keeps code clean and structured            |
| To manage big projects             | Makes code reusable and maintainable       |
| To reuse logic across applications | Allows sharing common functionality easily |

'''

