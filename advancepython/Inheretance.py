'''
Python Inheritance
Inheritance allows us to define a class that inherits all the methods and properties from another class.

Parent class is the class being inherited from, also called base class.

Child class is the class that inherits from another class, also called derived class.
'''

# class Person:
#       def __init__(self, fname, lname):
#         self.firstname = fname
#         self.lastname = lname

#       def printname(self):
#         print(self.firstname, self.lastname)
           

# # Use the Person class to create an object, and then execute the printname method:

# x = Person("John", "Doe")
# x.printname()
'''
Create a Child Class:
inherits the functionality from another class, send the parent class as a parameter when creating the child class
The __init__() function is called automatically every time the class is being used to create a new object.
'''
# class Person:
#       def __init__(self, fname, lname):
#         self.firstname = fname
#         self.lastname = lname

#       def printname(self):
#         print(self.firstname, self.lastname)
           
# class Student(Person):
#     pass
# # #Use the Person class to create an object, and then execute the printname method:

# x = Student("Naruto", "Uzumaki")
# x.printname()

'''
Add the __init__() Function:
'''
# class Person: # Parent class
#       def __init__(self, fname, lname): # Constructor
#         self.firstname = fname # Instance variable
#         self.lastname = lname # Instance variable

#       def printname(self): # Method
#         # Method to print the full name
#         print(self.firstname, self.lastname)

# class Student(Person): # Child class
#     # Inherits from Person class
#   def __init__(self, fname, lname): # Constructor
      
#     # Call the constructor of the parent class
#     # to initialize the instance variables
#     # This allows the child class to inherit the properties of the parent class
    
#     Person.__init__(self, fname, lname)

# x = Student("Tanjiro", "Kamado") # Create an instance of the Student class
# # Call the printname method from the parent class
# x.printname()





'''

| Line / Section            | What It Does                                                            |
| ------------------------- | ----------------------------------------------------------------------- |
| `class Person`            | Defines the parent class with constructor and print method              |
| `self.firstname/lаstname` | Stores object-specific data                                             |
| `class Student(Person)`   | Declares that `Student` inherits from `Person`                          |
| `Student.__init__`        | Overrides the parent constructor and explicitly calls `Person.__init__` |
| `x = Student(...)`        | Creates a child class instance with inherited attributes initialized    |
| `x.printname()`           | Calls the inherited method to display the full name                     |
-----------------------------------------------------------------------------------------------------------------
'''







'''
Use the super() Function:
super() function that will make the child class inherit all the methods and properties from its parent.
By using the super() function, you do not have to use the name of the parent element, it will automatically
inherit the methods and properties from its parent.


'''

# class Person:
#     def __init__(self, fname, lname):
#         self.firstname = fname
#         self.lastname = lname

#     def printname(self):
#         print(self.firstname, self.lastname)

# class Student(Person):
#     def __init__(self, fname, lname):
#         super().__init__(fname, lname)  # Modern way to initialize parent
#         # Additional Student-specific initializations can go here

# x = Student("Tanjiro", "Kamado")
# x.printname()




'''
super().__init__(…) वापरल्यामुळे Person class चा constructor (__init__) call होतो.

यातून firstname आणि lastname initialize होतात.

super() वापरल्याने parent class चे name hard‑code न करता MRO (Method Resolution Order) व्यवस्थित काम करते, विशेषतः multiple inheritance मध्ये फायदा होतो

'''


'''
the year 2019 should be a variable, and passed into the Student class when creating student objects. To do so,
add another parameter in the __init__() function
'''
# class Person:
#       def __init__(self, fname, lname):
#         self.firstname = fname
#         self.lastname = lname

#       def printname(self):
#         print(self.firstname, self.lastname)

# class Student(Person):
#   def __init__(self, fname, lname):
#     super().__init__(fname, lname)
#     self.graduationyear = 2019

# x = Student("Mike", "Olsen")

# print(x.graduationyear)

'''
If you add a method in the child class with the same name as a function in the parent class, the inheritance of the
 parent method will be overridden.
'''
# class Person:
#       def __init__(self, fname, lname):
#         self.firstname = fname
#         self.lastname = lname

#       def printname(self):
#         print(self.firstname, self.lastname)

# class Student(Person):
#   def __init__(self, fname, lname, year):
#     super().__init__(fname, lname)
#     self.graduationyear = year

#   def printname(self):
#     print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)

# x = Student("Mike", "Olsen", 2019)
# x.printname()



