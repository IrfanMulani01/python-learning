'''
Multiple Inheritance:
When a class inherits from more than one parent class, 
it is called Multiple Inheritance.

What is Multiple Inheritance?
In multiple inheritance, a class can inherit attributes and 
methods from more than one parent class.

जेव्हा एकच क्लास एकापेक्षा जास्त पॅरेंट क्लासेसकडून वारसा घेतो, त्याला Multiple
Inheritance म्हणतात.

Think of it like a family with multiple parents:
Parent 1 → Parent 2 → Child
Each parent can contribute traits (methods/attributes) to the child.
Structure:
Class A   (Base/Parent 1)
   ↓
Class B   (Base/Parent 2)
   ↓
Class C   (Derived from A and B / Child)
How It Works
Child inherits from both Parent 1 and Parent 2.
The Child object gets everything from both parents.
Python resolves methods/attributes using the MRO (Method Resolution Order), starting from the child upwards
Real-Life Analogy
Parent 1: Has certain skills and knowledge.
Parent 2: Has different skills and knowledge.
Child: Learns from both parents, combining their skills and knowledge.



'''
# Parent 1
# class Father:
#     def father_method(self):
#         print("I am Father.")

# # Parent 2
# class Mother:
#     def mother_method(self):
#         print("I am Mother.")

# # Child inherits from both Father and Mother
# class Child(Father, Mother):
#     def child_method(self):
#         print("I am Child.")

# # Object of Child
# c = Child()

# # Access methods from both parents and itself
# c.father_method()  # From Father
# c.mother_method()  # From Mother
# c.child_method()   # From Child


'''Example – Multiple Inheritance MRO'''

# class A:
#     def show(self):
#         print("A method")

# class B:
#     def show(self):
#         print("B method")

# class C(A, B):
#     pass

# obj = C()
# obj.show()
# print(C.mro())


''' Python searched: C → A → B → object (Left-to-right priority)'''