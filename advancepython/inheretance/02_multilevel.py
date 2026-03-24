'''
Multilevel inheritance:
When a child class becomes a parent class for another child class.


 What is Multilevel Inheritance?
In multilevel inheritance, a class is derived from another derived class — meaning there’s more than one generation in the inheritance chain.

Think of it like a family tree:

Grandparent → Parent → Child

Each level can pass down traits (methods/attributes) to the next.

Structure:

Class A   (Base/Grandparent)
   ↓
Class B   (Derived from A / Parent)
   ↓
Class C   (Derived from B / Child)


'''  
#.# Grandparent Class
# class Grandparent:
#     def grandparent_method(self):
#         print("I am the Grandparent.")

# # Parent Class (inherits from Grandparent)
# class Parent(Grandparent):
#     def parent_method(self):
#         print("I am the Parent.")

# # Child Class (inherits from Parent)
# class Child(Parent):
#     def child_method(self):
#         print("I am the Child.")

# # Creating object of Child
# c = Child()

# # Access methods from all levels
# c.grandparent_method()  # Inherited from Grandparent
# c.parent_method()       # Inherited from Parent
# c.child_method()        # Defined in Child

'''
 How It Works
Child inherits from Parent, and Parent inherits from Grandparent.

The Child object gets everything from Parent and Grandparent.

Python resolves methods/attributes using the MRO (Method Resolution Order), starting from the child upwards.


Real-Life Analogy
Grandparent: Has family traditions.

Parent: Learns traditions from Grandparent, adds some new ones.

Child: Gets both traditions and creates their own.

In Python terms — methods and attributes flow down the chain.

'''


''' Example with super()'''


# class Grandparent:
#     def __init__(self):
#         print("Grandparent constructor")

# class Parent(Grandparent):
#     def __init__(self):
#         super().__init__()
#         print("Parent constructor")

# class Child(Parent):
#     def __init__(self):
#         super().__init__()
#         print("Child constructor")

# c = Child()



'''Example – Multilevel Inheritance MRO'''


# class A:
#     def show(self):
#         print("A method")

# class B(A):
#     def show(self):
#         print("B method")

# class C(B):
#     pass

# obj = C()
# obj.show()
# print(C.mro())

# '''Python searched: C → B → A → object''' 