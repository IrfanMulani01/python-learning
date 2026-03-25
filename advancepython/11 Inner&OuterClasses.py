"""
========================================
OUTER CLASS & INNER CLASS IN PYTHON
========================================
"""

# ==================================================
# OUTER CLASS (DEFINITION)
# ==================================================

"""
What is an Outer Class?
----------------------
An outer class is a normal Python class.
It can contain:
✔ variables
✔ methods
✔ another class (called an inner class)
"""

# ==================================================
# INNER CLASS (DEFINITION)
# ==================================================

"""
What is an Inner Class?
----------------------
An inner class is a class defined inside another class.
It is used when the logic is closely related
to the outer class and is not useful on its own.
"""

# ==================================================
# BASIC EXAMPLE (OUTER + INNER)
# ==================================================

# class Outer:
#     def __init__(self):
#         self.name = "Outer Class"

#     class Inner:
#         def __init__(self):
#             self.name = "Inner Class"

#         def display(self):
#             return f"This is {self.name}"

# # Creating objects
# outer_obj = Outer()
# inner_obj = outer_obj.Inner()
# print(inner_obj.display())

# ==================================================
# PROGRAM LOGIC
# ==================================================

"""
1. Outer class is defined normally
2. Inner class is defined inside Outer
3. Inner class object is created using Outer().Inner()
4. Inner class method is called
"""

# ==================================================
# HOW ACCESS WORKS
# ==================================================

"""
Outer().Inner()

✔ First create Outer object
✔ Then access Inner class
✔ Then create Inner object
"""

# ==================================================
# DIFFERENCE: OUTER vs INNER CLASS
# ==================================================

"""
| Feature           | Outer Class                  | Inner Class                       |
|-------------------|------------------------------|-----------------------------------|
| Definition        | Normal class                 | Class inside another class        |
| Independent Use   | Yes                          | No                                |
| Access            | ClassName()                  | Outer().Inner()                   |
| Purpose           | Main functionality           | Helper / supporting logic         |
| Visibility        | Public                       | Limited to outer class            |
"""

# ==================================================
# WHEN TO USE INNER CLASS
# ==================================================

"""
✔ When logic is tightly coupled
✔ For better code organization
✔ To hide helper functionality
"""

# ==================================================
# QUICK SUMMARY (EXAM READY)
# ==================================================

"""
Outer Class:
------------
Main class

Inner Class:
------------
Class defined inside another class
Used for related helper logic
"""
