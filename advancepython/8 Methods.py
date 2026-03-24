"""
========================================
METHODS IN PYTHON (OOP)
========================================

Definition:
-----------
A method is a function that is defined inside a class.
It is used to perform operations using the data (variables)
of that class.

Methods define the behavior of objects.
"""

# ==================================================
# TYPES OF METHODS IN PYTHON
# ==================================================

"""
Python mainly supports the following types of methods:

1. Instance Methods
2. Class Methods
3. Static Methods
4. Magic (Special / Dunder) Methods
"""

# ==================================================
# 1. INSTANCE METHOD
# ==================================================

"""
Instance Method:
----------------
An instance method works with instance variables.
It must have 'self' as the first parameter.

Used when method needs object-specific data.
"""

# class Student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks

#     def display(self):        # Instance method
#         print("Name:", self.name)
#         print("Marks:", self.marks)

# s = Student("Rohit", 85)
# s.display()

# ==================================================
# 2. CLASS METHOD
# ==================================================

"""
Class Method:
-------------
A class method works with class variables.
It uses @classmethod decorator.
First parameter is 'cls' (class reference).
"""

# class Company:
#     company_name = "TCS"   # Class variable

#     @classmethod
#     def show_company(cls):
#         print("Company Name:", cls.company_name)

# Company.show_company()

# ==================================================
# DIFFERENCE: INSTANCE vs CLASS METHOD
# ==================================================

"""
Instance Method:
✔ Uses self
✔ Access instance variables
✔ Object-specific

Class Method:
✔ Uses cls
✔ Access class variables
✔ Class-specific
"""

# ==================================================
# 3. STATIC METHOD
# ==================================================

"""
Static Method:
--------------
A static method does not use self or cls.
It behaves like a normal function but
belongs to a class.

Uses @staticmethod decorator.
"""

# class MathUtils:
#     @staticmethod
#     def add(a, b):
#         return a + b

# print(MathUtils.add(10, 20))

# ==================================================
# WHEN TO USE STATIC METHOD
# ==================================================

"""
✔ Logic related to class
✔ No need for object or class data
✔ Utility/helper functions
"""

# ==================================================
# 4. MAGIC (SPECIAL / DUNDER) METHODS
# ==================================================

"""
Magic Methods:
--------------
Special methods that start and end with
double underscores (__).

They control object behavior.
"""

# ==================================================
# COMMON MAGIC METHODS
# ==================================================

"""
__init__  → Constructor
__str__   → String representation
__len__   → Length
__add__   → +
__eq__    → ==
"""

# ==================================================
# __init__ METHOD
# ==================================================

# class Person:
#    def __init__(self, name):
#       self.name = name
#       print(self.name)
# p = Person("Navanath")


# ==================================================
# __str__ METHOD
# ==================================================

# class Book:
#     def __init__(self, title):
#         self.title = title

#     def __str__(self):
#         return f"Book Title: {self.title}"

# b = Book("Python")
# print(b)

# ==================================================
# __len__ METHOD
# ==================================================

# class Team:
#     def __init__(self, players):
#         self.players = players

#     def __len__(self):
#         return len(self.players)

# t = Team(["A", "B", "C"])
# print(len(t))

# ==================================================
# METHOD CALLING STYLES
# ==================================================

"""
1. Object Method Call
   obj.method()

2. Class Method Call
   ClassName.method()

3. Static Method Call
   ClassName.method()
"""

# ==================================================
# IMPORTANT POINTS
# ==================================================

"""
✔ Methods define object behavior
✔ Instance methods use self
✔ Class methods use cls
✔ Static methods use neither self nor cls
✔ Magic methods customize object behavior
"""

# ==================================================
# QUICK SUMMARY (EXAM READY)
# ==================================================

"""
Methods:
--------
Functions inside a class

Types:
1. Instance Method
2. Class Method
3. Static Method
4. Magic Method
"""
