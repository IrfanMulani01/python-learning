'''
Hierarchical Inheritance:
When multiple child classes inherit from the same parent class, it is called Hierarchical Inheritance.

जेव्हा एकाच पॅरेंट क्लासकडून एकापेक्षा जास्त चाइल्ड क्लासेस वारसा घेतात, त्याला Hierarchical Inheritance म्हणतात.

 Structure:  
 
         Parent
       /   |   \
Child1  Child2  Child3


पालक (Parent) = समान नियम, संस्कार, गुणधर्म

मुले (Child1, Child2, Child3) = पालकांकडून सारखे गुण मिळतात पण प्रत्येकाकडे स्वतःचे खास गुणही असतात.
    


'''

# Parent class
# class Parent:
#     def parent_method(self):
#         print("I am the Parent.")

# # Child 1
# class Child1(Parent):
#     def child1_method(self):
#         print("I am Child 1.")

# # Child 2
# class Child2(Parent):
#     def child2_method(self):
#         print("I am Child 2.")

# # Child 3
# class Child3(Parent):
#     def child3_method(self):
#         print("I am Child 3.")

# # Objects of each child
# c1 = Child1()
# c1.parent_method()
# c1.child1_method()

# c2 = Child2()
# c2.parent_method()
# c2.child2_method()

# c3 = Child3()
# c3.parent_method()
# c3.child3_method()


'''Example – Hierarchical Inheritance MRO'''

# # Parent class
# class Parent:
#     def show(self):
#         print("Parent method")

# # Child 1 inherits from Parent
# class Child1(Parent):
#     pass  # show() not overridden

# # Child 2 inherits from Parent
# class Child2(Parent):
#     def show(self):  # Overriding method
#         print("Child2 method")

# # Object of Child1
# c1 = Child1()
# c1.show()  # MRO: Child1 -> Parent -> object
# print("Child1 MRO:", Child1.mro())

# # Object of Child2
# c2 = Child2()
# c2.show()  # MRO: Child2 -> Parent -> object
# print("Child2 MRO:", Child2.mro())

# '''Child1: स्वतःकडे show() method नाही, त्यामुळे Python MRO नुसार →
# Child1 → Parent → object क्रम वापरतो आणि Parent method कॉल करतो.

# Child2: स्वतःकडे show() method आहे, त्यामुळे Parent मध्ये जाण्याची गरज नाही.

# mro() ने method शोधायचा अचूक क्रम दिसतो.'''



