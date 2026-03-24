'''
Encapsulation:
-bundling data and methods within a single unit. 
-when you create a class, it means you are implementing encapsulation. 
-A class is an example of encapsulation as it binds all the data members
(instance variables) and 
 methods into a single unit.
(Wrapping data and the methods that works on data within same unit.)


Encapsulation (कॅप्स्युलेशन) म्हणजे डेटा (म्हणजेच व्हेरीएबल्स) आणि त्यावर काम करणारे फंक्शन्स 
(म्हणजेच मेथड्स) एका युनिटमध्ये म्हणजेच क्लासमध्ये बंद करून ठेवणे.


Why Use Encapsulation?
To protect data from unauthorized access.

To prevent accidental modification.

To control how important variables/methods are accessed or modified

# '''
# class Employee:
#     def __init__(self, name, salary, project):
#         self.name = name # public data member
#         self.salary = salary
#         self.project = project

#     def show(self):
#         # accessing public data member
#         print("Name: ", self.name, 'Salary:', self.salary)
#         # It accesses the public data members and prints them.
        
        
        
#     def work(self):
        
# #         # Another method in the class to show which 
# # project the employee is working on.
        
#         print(self.name, 'is working on', self.project)
# #         #  It prints the employee's name and project.


# emp = Employee('Akhilesh', 69000, 'NLP')
# emp.show()
# emp.work()




# How Encapsulation is Done Here 
# 1. Class as a container
# Encapsulation means binding data and methods inside a single unit — a class.
# Here, the Employee class contains both:

# Data (variables): name, salary, project

# Methods: show(), work()

# This is the first step of encapsulation — grouping related information into one logical unit.


# 2. Instance variables (data members)

# self.name = name
# self.salary = salary
# self.project = project

# These are instance variables.
# They are public by default in Python. While not protected or private,
# they are still part of the encapsulation since they belong to the class object
# and are accessed through methods like show() and work()


# 3. Accessing data through methods
# Instead of accessing or modifying variables directly, we use methods:

# def show(self):          # Accesses name and salary
#     print("Name: ", self.name, 'Salary:', self.salary)

# def work(self):          # Accesses name and project
#     print(self.name, 'is working on', self.project)
# # These methods encapsulate the logic for accessing and displaying data.
# These methods control how the data is used or shown, which is a form of controlled access, another key feature of encapsulation.

'''
Access Modifiers:
Access Modifiers define the scope of accessibility of variables and methods within a class or outside of it.
They are not enforced as strictly in Python as in languages like Java or C++, 
but naming conventions are used to indicate access level.

Access modifiers limit access to the variables and methods of a class.

Three types of access modifiers private, public, and protected.

1]Public Member: Accessible within or outside of a class.(.)
2]Protected Member: Accessible within the class and its sub-classes.(_)
3]Private Member: Accessible only within a class.(__)

| Modifier      | Syntax   | Accessibility                          |
| ------------- | -------- | -------------------------------------- |
| **Public**    | `name`   | Accessible everywhere                  |
| **Protected** | `_name`  | Accessible within class and subclasses |
| **Private**   | `__name` | Accessible only within the class       |
---------------------------------------------------------------------

'''
'''
Public Member:
Public data members are accessible within and outside of a class.
All member variables of the class are by default public.
# '''
# class Employee:
#     def __init__(self): 
#         # public data members
#         self.name = 'Navanath'
       

#     def show(self):
#         print('I am an employee')
        
#     def access(self):
#         print('Accessing public data member:', self.name)
#         # Accessing public data member and method
#         self.show()

# emp = Employee() # Creating an object of Employee class


# # Accessing public method and data member

# emp.access()    
# # Accessing public data member and method using the object of the class

# print(emp.name)  # Accessing public data member outside the class
# emp.show()  # Accessing public method outside the class






# class Employee:
#     def __init__(self):
#         self.name = 'Navanath'       # public attribute

#     def show(self):
#         print('I am an employee')    # public method

#     def access(self):
#         print("Within class, attribute:", self.name)
#         print("Within class, method output below:")
#         self.show()                 # calling public method inside the class

# emp = Employee()  # Creating an object of Employee class
# emp.access() # calling public method to access attribute and method within the class
# print("Outside class, attribute:", emp.name)  # accessing public attribute outside the class
# emp.show()  # calling public method outside the class


'''
Protected Member:
Protected members are accessible within the class and also available to its sub-classes. 
To define a protected member, prefix the member name with a single underscore _.

Protected data members are used when you implement inheritance and want to allow data members
access to only child classes.
'''
# class Employee:
#     def __init__(self):
#         self._name = 'Navanath'  # protected variable
#     def _show(self):
#         print(self._name, 'is an employee')  # protected method

# class Manager(Employee):
#     def access(self):
#         print('Accessing protected data member:', self._name)
#         # Accessing protected data member and method
#         self._show()  # Accessing protected method within the subclass  
              
# mng= Manager()  # Creating an object of Manager class
# # mng.show()  # Accessing protected method from the subclass
# mng.access()  # Accessing protected data member and method using the object of the subclass
'''
Private Member:
Private members are accessible only within the class, and we can’t access them directly 
from the class objects or outside the class.
To define a private member, prefix the member name with two underscores __.
Private data members are used when you want to hide the data members from outside the class.
They are not accessible outside the class, even in the child classes.

'''


# class Employee:
#     def __init__(self):
#         self.__name = 'Navanath' # private data member
 
#     def __show(self):    # private method
#         print('I am an employee')
    
#     def access(self):
#         print('Accessing private data member:', self.__name)
#         # Accessing private data member and method
#         self.__show()   # Accessing private method within the class

# emp= Employee() # Creating an object of Employee class

# # Accessing private method and data member using the object of the class
# # emp.access()

# # print(emp.__name)  # Attempting to access private data member outside the class will raise an AttributeError
# emp.__show()  # Attempting to access private method outside the class will also raise an AttributeError
            
'''-------------------------------------------------------------------------'''

# class A:
     
#     # Declaring public method
#     def fun(self):
#         print("Public method")
 
#     # Declaring private method
#     def __fun(self):
#         print("Private method")
 
#     # Calling private method
#     # another method
#     def Help(self):
#         self.fun()
#         self.__fun()
 
# obj = A()
# obj.Help()




# class Employee:
#     def __init__(self,name,salary):
#         self.__name = name
#         self.__salary = salary
#     def axd(self):
#         print(self.__salary)
#         print(self.__name)
    
        
        
# emp = Employee("Anjali",50000)
# emp.axd() 

'''
Name Mangling to access private members:
We can directly access private and protected variables from outside of a class through name mangling. 
The name mangling is created on an identifier by adding two leading underscores and one trailing underscore, 
like this _classname__dataMember.
# '''
# class Employee:
#     def __init__(self):
#         self.__name = 'Navanath'    # private variable
        
#     def __show(self):               # private method
#         print('I am an employee')
        
# emp= Employee()  # Creating an object of Employee class

# print(emp.Employee__name) 
# emp.Employee__show()  

# print(emp._Employee__name)  # Accessing private variable using name mangling
# emp._Employee__show()  # Accessing private method using name mangling        
              
    




'''Getters and Setters in Python:
Use the getter method to access data mmbers and the setter methods to modify the data members.
private variables are not hidden fields like in other programming languages. 
The getters and setters methods are often used when:
1.When we want to avoid direct access to private variables
2.To add validation logic for setting a value


Getter (accessor) is a method that retrieves a value of a private (non‑public) attribute.

Setter (mutator) is a method that modifies its value—often enforcing validation rules or encapsulation.

In Python, getters and setters are used to preserve encapsulation while allowing controlled access 
to private data (e.g. converting, validating, or logging)

गेटर (Getter) म्हणजे method जिच्या माध्यमातून आपण एखाद्या private (non‑public) attribute ची value read करू शकतो.

सेटर (Setter) म्हणजे method जी त्या attribute value बदलायला वापरली जाते, आणि यात validation 
(उदा. value ≥ 0 आहे का, type योग्य आहे का) केली जाते—यामुळे data integrity राखली जाते.

Python मध्ये public attributes थेट access करणे सोपे आहे, परंतु जर आपण भविष्यात त्या attribute वर
behavior जोडायचा इच्छित असाल (validation, transformation वगैरे), तर getters/setters आवश्यक होतात


 '''

# class Student:
#     def __init__(self, name, age):
#         # private member
#         self.name = name
#         self.__age = age

#     # getter method
#     def get_age(self):
#         return self.__age

#     # setter method
#     def set_age(self, age):
#         self.__age = age

# stud = Student('Jessa', 14)

# # retrieving age using getter
# print('Name:', stud.name, stud.get_age())

# # changing age using setter 
# stud.set_age(16)

# # retrieving age using getter
# print('Name:', stud.name, stud.get_age())





# class Employee:
#     def set_enum(self, enum):        # This method is a setter for the enum attribute.
#         # It sets the value of the enum attribute.
#         # This allows controlled modification of the enum attribute.
#         # It is used to set the value of the enum attribute.
#         self.enum = enum            # Assigns the value of enum to the instance variable self.enum.
        
        
        
    
#     def get_enum(self):        # This method is a getter for the enum attribute.
#         # It returns the value of the enum attribute.
#         # This allows controlled access to the enum attribute.
#         return self.enum #        # Returns the value of the enum attribute.
    
# emp= Employee()  # Creating an instance of the Employee class
# emp.set_enum(1001)  # Setting the enum attribute using the setter method    
 
# print(emp.get_enum())  # Accessing the enum attribute using the getter method   





'''
Information Hiding and conditional logic for setting an object attributes:

1 What is Information Hiding?
Information Hiding is the OOP principle of restricting direct access to the internal state (data) of an object

It is achieved using:

Access Modifiers (private, protected)

Getter/Setter methods

Goal: Protect internal object data from direct modification and expose only necessary parts.






Information Hiding आणि Conditional Logic for Setting Attributes हे Object Oriented Programming (OOP) मधील महत्वाचे concepts आहेत.

1. Information Hiding म्हणजे काय? (माहिती लपवणे)
Information Hiding म्हणजे object च्या internal data (जसं की variable, state) ला थेट access करण्यापासून थांबवणं.

हे का करतात?
चुकीचा डेटा change होऊ नये म्हणून

object सुरक्षित ठेवण्यासाठी

योग्य access control ठेवण्यासाठी

हे achieve कसं करतात?
Access Modifiers वापरून
➤ private: __name (double underscore)
➤ protected: _name (single underscore)

Getter आणि Setter methods वापरून





'''
# class BankAccount:
#     def __init__(self, balance):
#         self.__balance = balance   # private attribute (hidden)

#     def get_balance(self):
#         return self.__balance      # getter

#     def deposit(self, amount):
#         if amount > 0:
#             self.__balance += amount

#     def withdraw(self, amount):
#         if 0 < amount <= self.__balance:
#             self.__balance -= amount
#         else:
#             print("Invalid withdrawal")



# account = BankAccount(1000)

# print(account.get_balance())   # ✅ safe access

# account.deposit(500)
# print(account.get_balance())   # 1500

# Direct access (not allowed)
# print(account.__balance)     #❌ Error

# Name mangling (technically possible, discouraged)
# print(account._BankAccount__balance)  # 1500 ✅

#  ------------------------------------------------------------------------------------------------------

# class BankAccount:
#     def __init__(self, balance):
#         self.__balance = balance   # private attribute (लपवलेला balance)

#     def get_balance(self):
#         return self.__balance      # getter - सुरक्षितपणे balance देतो

#     def deposit(self, amount):
#         if amount > 0:
#             self.__balance += amount   # जर amount योग्य असेल तर जमा करतो

#     def withdraw(self, amount):
#         if 0 < amount <= self.__balance:
#             self.__balance -= amount   # योग्य रक्कम असल्यासच पैसे काढू देतो
#         else:
#             print("Invalid withdrawal")



# account = BankAccount(1000)

# print(account.get_balance())   # ✅ balance मिळतो - सुरक्षित access

# account.deposit(500)           # 500 जमा
# print(account.get_balance())   # आता balance 1500

# खालील थेट access ❌ - कारण तो private आहे
# print(account.__balance)     # ❌ error येतो

# पण technically (name mangling) वापरून access करता येतो (हे discouraged आहे)
# print(account._BankAccount__balance)  # ✅ 1500 - पण वापरू नये



'''

|                         |                                                                                                      |
| ----------------------- | ----------------------------------------------------------------------------------------------------------------- |
| `__balance`             | हा private variable आहे. दुसऱ्या ठिकाणाहून direct access करता येत नाही.                                           |
| `get_balance()`         | हा getter method आहे. याने आपण सुरक्षितरित्या balance मिळवतो.                                                     |
| `deposit()`             | condition check करतो की amount positive आहे का, आणि मगच जमा करतो.                                                 |
| `withdraw()`            | account मध्ये किती रक्कम आहे, ते पाहूनच पैसे काढण्याची परवानगी देतो.                                              |
| `_BankAccount__balance` | हे name mangling वापरून private variable access करणे आहे. पण हे **नसावं**. कारण ते OOP principles चं उल्लंघन आहे. |


Information hiding म्हणजे "जे गरजेचं आहे तेवढंच दाखवा, उगाच सगळं बाहेरून बदलता येईल असं करू नका."

'''





'''
2. Conditional Logic for Setting Object Attributes
Conditional logic allows setting object attributes based on specific rules or validations.

Goal: Ensure only valid or meaningful values are assigned to object attributes.


Conditional Logic म्हणजे काय?
Conditional Logic म्हणजे "Attribute सेट करताना काही अटी घालणे."

याचा मुख्य उद्देश म्हणजे:

योग्य आणि वैध (valid) डेटा फक्त object मध्ये सेट होणं.

चुकीचा डेटा येऊ नये म्हणून validation लावणं.

'''

# class Student:
#     def __init__(self, name, age):
#         self.name = name
#         self.set_age(age)   # using setter with logic

#     def set_age(self, age):
#         if age >= 5:
#             self.__age = age
#         else:
#             print("Age must be 5 or older")
#             self.__age = None

#     def get_age(self):
#         return self.__age


# s = Student("Rahul", 4)    # Invalid age
# print(s.get_age())         # None

# s.set_age(10)              # Valid age
# print(s.get_age())         # 10







# class Student:
#     def __init__(self, name, age):
#         self.name = name
#         self.set_age(age)   # constructor मधूनच set_age() कॉल करतो

#     def set_age(self, age):
#         if age >= 5:
#             self.__age = age     # जर योग्य वय असेल, तर सेट करतो
#         else:
#             print("Age must be 5 or older")  # अट पूर्ण नाही
#             self.__age = None               # चुकीचा वय असल्यास None ठेवतो

#     def get_age(self):
#         return self.__age


# s = Student("Rahul", 4)     # चुकीचं वय दिलं
# print(s.get_age())          # None (वय सेट नाही)

# s.set_age(10)               # योग्य वय
# print(s.get_age())          # 10



# set_age() हे method एक setter आहे.

# ते वय (age) सेट करताना एक अट (condition) तपासतो – वय 5 पेक्षा जास्त असावं.

# जर अट पूर्ण नसेल, तर वय सेटच होत नाही, आणि एक वॉर्निंग दिली जाते.
# हे conditional logic आहे.
# हे conditional logic म्हणजेच object च्या अ‍ॅट्रीब्यूट्स सेट करताना काही शर्ती लावणे.






# जेव्हा एखादा अ‍ॅट्रीब्यूट सेट करताना शर्ती लावली जाते, तेव्हा त्याला conditional logic म्हणतात.

# वय 5 पेक्षा कमी असल्यास वय सेट होत नाही आणि वॉर्निंग दिली जाते.

# यामुळे object योग्य डेटा ने तयार होतो.











"""
========================================================
ENCAPSULATION & ACCESS MODIFIERS IN PYTHON
(THEORY + CODE WITH EXPLANATION)
========================================================

--------------------------------------------------------
WHAT IS ENCAPSULATION?
--------------------------------------------------------
Encapsulation is an Object-Oriented Programming (OOP)
concept where:

• Data (variables)
• Methods (functions)

are wrapped together inside a single unit called a CLASS.

In simple words:
Encapsulation = Data + Methods inside one class

मराठीत:
Encapsulation म्हणजे data (variables) आणि त्यावर काम करणारे
methods एकाच class मध्ये बंद करून ठेवणे.

--------------------------------------------------------
WHY DO WE USE ENCAPSULATION?
--------------------------------------------------------
1. To protect data from unauthorized access
2. To avoid accidental modification of data
3. To control how data is accessed or modified
4. To maintain data integrity
5. To make code secure and maintainable

--------------------------------------------------------
ACCESS MODIFIERS IN PYTHON
--------------------------------------------------------
Access modifiers define how and where class members
(variables and methods) can be accessed.

⚠️ Important:
Python does NOT strictly enforce access modifiers
like Java or C++.
It uses NAMING CONVENTIONS.

There are THREE types of access modifiers:

--------------------------------------------------------
1) PUBLIC MEMBERS
--------------------------------------------------------
• Accessible from anywhere
• Inside the class
• Outside the class
• Default access level in Python

Syntax:
    variable_name
    method_name

--------------------------------------------------------
2) PROTECTED MEMBERS
--------------------------------------------------------
• Accessible inside the class
• Accessible inside child (sub) classes
• Should NOT be accessed directly outside (by convention)

Syntax:
    _variable_name
    _method_name

⚠️ Note:
Protected members are NOT enforced by Python.
They are only a naming convention.

--------------------------------------------------------
3) PRIVATE MEMBERS
--------------------------------------------------------
• Accessible ONLY inside the class
• Not accessible directly outside the class
• Python uses NAME MANGLING to hide them

Syntax:
    __variable_name
    __method_name

Private members help in INFORMATION HIDING.
"""

# ======================================================
# 1. BASIC EXAMPLE OF ENCAPSULATION
# ======================================================

# class Employee:
#     """
#     This class demonstrates encapsulation by
#     wrapping data and methods together.
#     """

#     def __init__(self, name, salary, project):
#         # Constructor: runs when object is created

#         self.name = name
#         # Public variable

#         self.salary = salary
#         # Public variable

#         self.project = project
#         # Public variable

#     def show(self):
#         # Public method to access data
#         print("Name:", self.name, "Salary:", self.salary)

#     def work(self):
#         # Public method showing behavior
#         print(self.name, "is working on", self.project)


# emp = Employee("Akhilesh", 69000, "NLP")
# emp.show()
# emp.work()

# ======================================================
# 2. PUBLIC MEMBERS
# ======================================================

"""
PUBLIC MEMBERS:
• Can be accessed anywhere
• Inside class
• Outside class
"""

# class Employee:
#     def __init__(self):
#         self.name = "Navanath"
#         # Public variable

#     def show(self):
#         # Public method
#         print("I am an employee")


# emp = Employee()

# print(emp.name)   # Accessing public variable outside class
# emp.show()        # Accessing public method outside class

# ======================================================
# 3. PROTECTED MEMBERS
# ======================================================

"""
PROTECTED MEMBERS:
• Defined using single underscore (_)
• Accessible in class and subclass
• Meant for internal use
"""

# class Employee:
#     def __init__(self):
#         self._name = "Navanath"
#         # Protected variable

#     def _show(self):
#         # Protected method
#         print(self._name, "is an employee")


# class Manager(Employee):
#     # Child class of Employee

#     def access(self):
#         # Accessing protected members inside subclass
#         print(self._name)
#         self._show()


# mgr = Manager()
# mgr.access()

"""
NOTE:
Even though protected members can be accessed
outside the class, it should NOT be done.
"""

# ======================================================
# 4. PRIVATE MEMBERS
# ======================================================

"""
PRIVATE MEMBERS:
• Defined using double underscore (__)
• Accessible ONLY inside the class
• Used for information hiding
"""

# class Employee:
#     def __init__(self):
#         self.__name = "Navanath"
#         # Private variable

#     def __show(self):
#         # Private method
#         print("I am an employee")

#     def access(self):
#         # Public method accessing private members
#         print(self.__name)
#         self.__show()


# emp = Employee()
# emp.access()

# ❌ These will cause error if uncommented
# print(emp.__name)
# emp.__show()

# ======================================================
# 5. NAME MANGLING (INTERNAL MECHANISM)
# ======================================================

"""
Python internally changes private members as:

__name  -->  _ClassName__name

This is called NAME MANGLING.

It prevents accidental access,
but it is NOT true security.
"""

# print(emp._Employee__name)
# emp._Employee__show()

"""
⚠️ Accessing private members using name mangling
is strongly DISCOURAGED.
"""

# ======================================================
# 6. GETTERS AND SETTERS
# ======================================================

"""
GETTERS AND SETTERS:
Used to access and modify private variables safely.

Getter  → Read value
Setter  → Modify value (with or without validation)
"""

# class Student:
#     def __init__(self, name, age):
#         self.name = name
#         # Public variable

#         self.__age = age
#         # Private variable

#     def get_age(self):
#         # Getter method
#         return self.__age

#     def set_age(self, age):
#         # Setter method
#         self.__age = age


# stud = Student("Jessa", 14)
# print(stud.get_age())

# stud.set_age(16)
# print(stud.get_age())

# ======================================================
# 7. INFORMATION HIDING + CONDITIONAL LOGIC
# ======================================================

"""
INFORMATION HIDING:
Direct access to data is restricted.
Only safe methods are exposed.
"""

# class BankAccount:
#     def __init__(self, balance):
#         self.__balance = balance
#         # Private balance

#     def get_balance(self):
#         # Getter
#         return self.__balance

#     def deposit(self, amount):
#         # Conditional logic
#         if amount > 0:
#             self.__balance += amount

#     def withdraw(self, amount):
#         # Conditional logic
#         if 0 < amount <= self.__balance:
#             self.__balance -= amount
#         else:
#             print("Invalid withdrawal")


# account = BankAccount(1000)
# print(account.get_balance())

# account.deposit(500)
# print(account.get_balance())

# ======================================================
# 8. CONDITIONAL LOGIC WHILE SETTING ATTRIBUTES
# ======================================================

"""
Conditional Logic:
Attributes are set only if conditions are satisfied.
"""

# class Student:
#     def __init__(self, name, age):
#         self.name = name
#         self.set_age(age)

#     def set_age(self, age):
#         if age >= 5:
#             self.__age = age
#         else:
#             print("Age must be 5 or older")
#             self.__age = None

#     def get_age(self):
#         return self.__age


# s = Student("Rahul", 4)
# print(s.get_age())

# s.set_age(10)
# print(s.get_age())

# ======================================================
# FINAL SUMMARY
# ======================================================

"""
ENCAPSULATION PROVIDES:
✔ Data security
✔ Controlled access
✔ Validation
✔ Maintainable and clean code

Golden Rule:
"Show only what is necessary, hide the rest."
"""
