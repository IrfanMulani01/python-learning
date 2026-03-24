"""
========================================
POLYMORPHISM IN PYTHON (OOP)
========================================

Definition:
-----------
Polymorphism means "many forms".

In OOP, polymorphism allows the same method name
or operator to behave differently
based on the object or data it is working with.
"""

# ==================================================
# TYPES OF POLYMORPHISM IN PYTHON
# ==================================================

"""
1. Method Overloading (Python style)
2. Method Overriding
3. Operator Overloading
"""

# ==================================================
# METHOD OVERLOADING (PYTHON WAY)
# ==================================================

"""
Method Overloading:
-------------------
In Python, method overloading is achieved using
default arguments or variable-length arguments.

Python does NOT support traditional method overloading
like Java or C++.
"""

# Using default arguments

# class Calculator:
#     def add(self, a, b=10, c=2):
#         return a + b + c

# calc = Calculator()
# print(calc.add(5))
# print(calc.add(5, 10))
# print(calc.add(5, 10, 15))

# Using *args

# class Calculator:
#     def add(self, *args):
#         return sum(args)

# calc = Calculator()
# print(calc.add(1, 2))
# print(calc.add(1, 2, 3, 4))

# ==================================================
# METHOD OVERRIDING
# ==================================================

"""
Method Overriding:
-----------------
When a child class provides its own implementation
of a method that already exists in the parent class.
"""

# class Animal:
#     def sound(self):
#         print("Animal makes sound")

# class Dog(Animal):
#     def sound(self):
#         print("Dog barks")

# a = Animal()
# d = Dog()
# a.sound()
# d.sound()

# ==================================================
# METHOD OVERRIDING WITH super()
# ==================================================

# class Bird:
#     def sound(self):
#         print("Bird sound")

# class Sparrow(Bird):
#     def sound(self):
#         super().sound()
#         print("Sparrow chirps")

# s = Sparrow()
# s.sound()

# ==================================================
# OPERATOR OVERLOADING
# ==================================================

"""
Operator Overloading:
---------------------
Operator overloading allows operators like
+, -, *, / to work with user-defined objects.

This is done using magic (dunder) methods.
"""

# ==================================================
# COMMON OPERATOR OVERLOADING METHODS
# ==================================================

"""
+   → __add__
-   → __sub__
*   → __mul__
/   → __truediv__
==  → __eq__
"""

# ==================================================
# OPERATOR OVERLOADING EXAMPLE (+)
# ==================================================

# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def __add__(self, other):
#         return Point(self.x + other.x, self.y + other.y)

#     def __str__(self):
#         return f"({self.x}, {self.y})"

# p1 = Point(2, 3)
# p2 = Point(4, 5)
# print(p1 + p2)

# ==================================================
# OPERATOR OVERLOADING EXAMPLE (==)
# ==================================================

# class Student:
#     def __init__(self, marks):
#         self.marks = marks

#     def __eq__(self, other):
#         return self.marks == other.marks

# s1 = Student(80)
# s2 = Student(80)
# print(s1 == s2)

# ==================================================
# REAL-WORLD OPERATOR OVERLOADING
# ==================================================

# class Word:
#     def __init__(self, text):
#         self.text = text

#     def __add__(self, other):
#         return Word(self.text + " " + other.text)

#     def __str__(self):
#         return self.text

# w1 = Word("Hello")
# w2 = Word("Python")
# print(w1 + w2)

# ==================================================
# DUCK TYPING (POLYMORPHISM)
# ==================================================

"""
Duck Typing:
------------
If it walks like a duck and talks like a duck,
it is a duck.

Python cares about behavior, not type.
"""

# class Dog:
#     def speak(self):
#         print("Dog barks")

# class Cat:
#     def speak(self):
#         print("Cat meows")

# def make_sound(animal):
#     animal.speak()

# d = Dog()
# c = Cat()
# make_sound(d)
# make_sound(c)

# ==================================================
# IMPORTANT POINTS
# ==================================================

"""
✔ Same method name, different behavior
✔ Achieved via overriding & overloading
✔ Operator overloading uses magic methods
✔ Duck typing is runtime polymorphism
"""

# ==================================================
# QUICK SUMMARY (EXAM READY)
# ==================================================

"""
Polymorphism:
-------------
Many forms of the same method/operator

Types:
1. Method Overloading (Python way)
2. Method Overriding
3. Operator Overloading
4. Duck Typing
"""
