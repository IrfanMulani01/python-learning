''' Hybrid Inheritance:

Hybrid Inheritance means combining two or more types of inheritance in a single program.
It is basically a mix of Single, Multiple, Multilevel, or Hierarchical inheritance.


Since hybrid inheritance can lead to the diamond problem (when two parent 
classes have the
same method, and a child inherits from both), many languages like Java do not
allow it directly with classes — but Python supports it.


Hybrid Inheritance म्हणजे दोन किंवा अधिक प्रकारच्या inheritance एकत्र वापरणे.
उदा. Single Inheritance, Multiple Inheritance, Multilevel Inheritance, Hierarchical Inheritance यापैकी काही प्रकार एकत्र करणे.

हे केल्याने कधी कधी diamond problem येऊ शकते (जेव्हा दोन parent classes मध्ये एकच method असेल आणि child दोन्ही inherit करत असेल). म्हणून Java मध्ये हे थेट शक्य नाही, पण Python मध्ये शक्य आहे.


'''

# # Single Inheritance + Multiple Inheritance = Hybrid

# class A:
#     def displayA(self):
#         print("This is class A")

# class B(A):  # Single Inheritance (B inherits from A)
#     def displayB(self):
#         print("This is class B")

# class C:
#     def displayC(self):
#         print("This is class C")

# class D(B, C):  # Multiple Inheritance (D inherits from B and C)
#     def displayD(self):
#         print("This is class D")

# # Object of class D
# obj = D()
# obj.displayA()  # From A
# obj.displayB()  # From B
# obj.displayC()  # From C
# obj.displayD()  # From D


'''
A → B is Single Inheritance

D inherits from both B and C — Multiple Inheritance

Together → Hybrid Inheritance

'''