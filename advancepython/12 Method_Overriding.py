"""
========================================
METHOD OVERRIDING IN PYTHON (OOP)
========================================

Definition:
-----------
Method overriding occurs when a child class
provides its own implementation of a method
that is already defined in the parent class.

The method name and parameters must be the same.
"""

# ==================================================
# WHY METHOD OVERRIDING IS USED
# ==================================================

"""
✔ To change parent class behavior
✔ To provide specific implementation in child
✔ To achieve runtime polymorphism
"""

# ==================================================
# BASIC METHOD OVERRIDING (EXAMPLE)
# ==================================================

# class Animal:
#     def sound(self):
#         print("Animal makes sound")

# class Dog(Animal):
#     def sound(self):      # Overriding parent method
#         print("Dog barks")

# d = Dog()
# d.sound()   # Dog barks

# ==================================================
# PROGRAM LOGIC
# ==================================================

"""
1. Parent class has a method
2. Child class defines the same method
3. Child method overrides parent method
4. Child version is executed at runtime
"""

# ==================================================
# OVERRIDING WITH super()
# ==================================================

"""
super() allows calling parent method
inside overridden method.
"""

# class Person:
#     def show(self):
#         print("I am a Person")

# class Student(Person):
#     def show(self):
#         super().show()
#         print("I am a Student")

# s = Student()
# s.show()

# ==================================================
# METHOD OVERRIDING WITH __init__
# ==================================================

"""
Child class can override parent constructor.
super() is used to call parent __init__.
"""

# class Employee:
#     def __init__(self, name):
#         self.name = name
#
# class Manager(Employee):
#     def __init__(self, name, dept):
#         super().__init__(name)
#         self.dept = dept
#
#     def display(self):
#         print("Name:", self.name)
#         print("Department:", self.dept)
#
# m = Manager("Rohit", "IT")
# m.display()

# ==================================================
# METHOD OVERRIDING IN MULTIPLE INHERITANCE
# ==================================================

"""
Python follows MRO (Method Resolution Order)
to decide which method to call.
"""

# class A:
#     def show(self):
#         print("Class A")
#
# class B(A):
#     def show(self):
#         print("Class B")
#
# class C(B):
#     def show(self):
#         print("Class C")
#
# obj = C()
# obj.show()   # Class C

# ==================================================
# IMPORTANT RULES
# ==================================================

"""
✔ Method name must be same
✔ Parameters should match
✔ Child method executes first
✔ Parent method can be accessed using super()
"""

# ==================================================
# QUICK SUMMARY (EXAM READY)
# ==================================================

"""
Method Overriding:
-----------------
Child class redefines parent method
Used for runtime polymorphism
"""
