"""
=============================================
VARIABLES IN PYTHON OOP
=============================================

In Python OOP, variables are of three main types:
1. Instance Variables
2. Class Variables
3. Local Variables
"""

# =================================================
# 1. INSTANCE VARIABLES
# =================================================

"""
Instance variables belong to an object.
Each object has its own copy.
Defined using self inside __init__().
"""

# Example 1
# class Car:
#     def __init__(self, brand, model):
#         self.brand = brand      # Instance variable
#         self.model = model

#     def show(self):
#         print(self.brand, self.model)

# car1 = Car("Toyota", "Innova")
# car2 = Car("Honda", "City")

# car1.show()
# car2.show()

# # Example 2
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

# p1 = Person("Alice", 30)
# p2 = Person("Bob", 25)    

# print(p1.name, p1.age)
# print(p2.name, p2.age)

# p2.age = 26
# print(p2.age)    # Changed
# print(p1.age)    # Not affected

# =================================================
# 2. CLASS VARIABLES
# =================================================

"""
Class variables belong to the class.
Shared by all objects.
Defined outside methods.
"""

# class Circle:
#     pi = 3.14        # Class variable

#     def __init__(self, radius):
#         self.radius = radius   # Instance variable

#     def area(self):
#         return Circle.pi * self.radius ** 2

# c1 = Circle(5)
# c2 = Circle(10)

# print(c1.area())
# print(c2.area())
# print(Circle.pi)

# =================================================
# 3. LOCAL VARIABLES
# =================================================

"""
Local variables are created inside methods.
They exist only while the method runs.
"""

# class Calculator:
#     def add(self, x, y):
#         result = x + y      # Local variable
#         return result

#     def subtract(self, x, y):
#         result = x - y
#         return result

#     def multiply(self, x, y):
#         result = x * y
#         return result

#     def divide(self, x, y):
#         if y != 0:
#             result = x / y
#             return result
#         return "Cannot divide by zero"

# calc = Calculator()
# print(calc.add(5, 3))
# print(calc.subtract(10, 4))
# print(calc.multiply(2, 6))
# print(calc.divide(8, 2))
# print(calc.divide(8, 0)) 

# =================================================
# QUICK SUMMARY
# =================================================

"""
Instance Variable → Object level → uses self
Class Variable    → Class level → shared
Local Variable    → Method level → temporary
"""
