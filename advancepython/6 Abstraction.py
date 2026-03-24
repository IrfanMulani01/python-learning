"""
========================================
ABSTRACTION IN PYTHON (OOP)
========================================

Definition:
-----------
Abstraction is an OOP concept that hides
the internal implementation details
and shows only the essential features
to the user.

It focuses on:
✔ What an object does
✔ Not how it does it
"""

# ==================================================
# WHY ABSTRACTION IS NEEDED
# ==================================================

"""
✔ Reduces complexity
✔ Improves code readability
✔ Enhances security
✔ Helps in large project design
"""

# ==================================================
# HOW ABSTRACTION IS ACHIEVED IN PYTHON
# ==================================================

"""
Python provides abstraction using:
1. Abstract Base Classes (ABC)
2. abstractmethod decorator

These are available in the abc module.
"""

from abc import ABC, abstractmethod

# ==================================================
# ABSTRACT CLASS (DEFINITION)
# ==================================================

"""
Abstract Class:
---------------
An abstract class is a class that cannot
be instantiated (object cannot be created).

It may contain:
✔ Abstract methods (without body)
✔ Normal methods (with body)
"""

# ==================================================
# ABSTRACT METHOD (DEFINITION)
# ==================================================

"""
Abstract Method:
----------------
A method that is declared but not implemented
in the abstract class.

Child class MUST implement it.
"""

# ==================================================
# BASIC ABSTRACTION EXAMPLE
# ==================================================

# class Shape(ABC):
#     @abstractmethod
#     def area(self):
#         pass

# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius

#     def area(self):
#         return 3.14 * self.radius * self.radius

# c = Circle(5)
# print(c.area())

# ==================================================
# ABSTRACT CLASS WITH MULTIPLE METHODS
# ==================================================

# class Vehicle(ABC):
#     @abstractmethod
#     def start(self):
#         pass

#     @abstractmethod
#     def stop(self):
#         pass

# class Bike(Vehicle):
#     def start(self):
#         print("Bike starts")

#     def stop(self):
#         print("Bike stops")

# b = Bike()
# b.start()
# b.stop()

# ==================================================
# ABSTRACT CLASS WITH NORMAL METHOD
# ==================================================

# class Bank(ABC):
#     def welcome(self):
#         print("Welcome to the bank")

#     @abstractmethod
#     def interest_rate(self):
#         pass

# class SBI(Bank):
#     def interest_rate(self):
#         print("SBI Interest Rate: 6%")

# s = SBI()
# s.welcome()
# s.interest_rate()

# ==================================================
# RULES OF ABSTRACTION
# ==================================================

"""
✔ Abstract class cannot be instantiated
✔ Child class must implement all abstract methods
✔ If not implemented → TypeError
"""

# ==================================================
# ERROR EXAMPLE (IMPORTANT)
# ==================================================

# class Test(ABC):
#     @abstractmethod
#     def show(self):
#         pass
# # #
# t = Test()   # ❌ Error: Cannot create object of abstract class

# ==================================================
# REAL-WORLD EXAMPLE
# ==================================================

# class Payment(ABC):
#     @abstractmethod
#     def pay(self, amount):
#         pass

# class UPI(Payment):
#     def pay(self, amount):
#         print(f"Paid {amount} using UPI")

# class Card(Payment):
#     def pay(self, amount):
#         print(f"Paid {amount} using Card")

# p1 = UPI()
# p2 = Card()
# p1.pay(500)
# p2.pay(1000)

# ==================================================
# DIFFERENCE: ABSTRACTION vs ENCAPSULATION
# ==================================================

"""
Abstraction:
------------
✔ Hides implementation
✔ Focuses on design
✔ Achieved using ABC

Encapsulation:
--------------
✔ Hides data
✔ Focuses on security
✔ Achieved using access modifiers
"""

# ==================================================
# IMPORTANT POINTS
# ==================================================

"""
✔ Use ABC module for abstraction
✔ abstractmethod forces implementation
✔ Helps in loose coupling
"""

# ==================================================
# QUICK SUMMARY (EXAM READY)
# ==================================================

"""
Abstraction:
------------
Hiding internal implementation
Showing essential features only

Implemented using:
✔ ABC
✔ @abstractmethod
"""
