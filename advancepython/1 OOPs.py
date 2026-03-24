"""
========================================
WHAT IS OOP? (OBJECT-ORIENTED PROGRAMMING)
========================================

OOP means writing programs using OBJECTS.

Instead of writing everything in one place,
we group related data and functions together.

This makes programs:
✔ easy to understand
✔ easy to maintain
✔ easy to reuse
"""

# ==================================================
# WHY OOP?
# ==================================================

"""
Without OOP:
- Code becomes long and confusing

With OOP:
- Code is well organized
- Real-world problems are easy to represent
"""

# ==================================================
# BASIC OOP TERMS
# ==================================================

"""
CLASS
-----
A class is a blueprint or design.
It tells what an object will have and what it can do.

OBJECT
------
An object is created from a class.
It is a real thing made using the blueprint.
"""

# ==================================================
# REAL LIFE EXAMPLE
# ==================================================

"""
Class  → Car (design)
Object → Toyota, Honda, BMW (real cars)
"""

# ==================================================
# SIMPLE CLASS & OBJECT EXAMPLE
# ==================================================

# class Car:
#     def __init__(self, brand, model):
#         self.brand = brand
#         self.model = model

#     def start(self):
#         print(self.brand, self.model, "is starting")

# # Creating objects
# car1 = Car("Toyota", "Innova")
# car2 = Car("Honda", "City")

# car1.start()
# car2.start()

# ==================================================
# WHAT IS __init__ ?
# ==================================================

"""
__init__ is called a CONSTRUCTOR.

It runs automatically when we create an object.

Its job:
- Receive data
- Store data inside the object
"""

# ==================================================
# WHAT IS self ?
# ==================================================

"""
self means:
👉 current object

self is used to:
- store data in the object
- access object data inside methods

IMPORTANT:
self is NOT a keyword.
It is just a common name used by Python developers.
"""

# ==================================================
# WHY self IS NEEDED?
# ==================================================

"""
Every object has different data.

Example:
car1 brand = Toyota
car2 brand = Honda

self tells Python:
"Use data of THIS object"
"""

# ==================================================
# EASY self EXAMPLE
# ==================================================

# class Student:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def show(self):
#         print("Name:", self.name)
#         print("Age:", self.age)

# s1 = Student("Rahul", 20)
# s2 = Student("Amit", 22)

# s1.show()
# s2.show()

# ==================================================
# FOUR PILLARS OF OOP (EASY WORDS)
# ==================================================

"""
1. Encapsulation
   - Keeping data and methods together in one class

2. Abstraction
   - Hiding internal details
   - Showing only what is needed

3. Inheritance
   - One class using another class's code

4. Polymorphism
   - Same function name
   - Different behavior
"""

# ==================================================
# ONE-LINE SUMMARY (VERY IMPORTANT)

# ==================================================

"""
✔ OOP → Programming using objects
✔ Class → Blueprint
✔ Object → Created from class
✔ self → Refers to current object
✔ __init__ → Runs when object is created
"""
