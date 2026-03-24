
'''
Why is self important?
When you create a class in Python, you're defining a blueprint for objects. 
Each object (or instance) created from this 
class can have its own unique attributes and behaviors. The self parameter 
allows methods within the class to refer to the 
specific instance they're operating on
and access its attributes and methods.



self म्हणजे काय?
self हे class च्या instance ला सूचित करते.

हे instance methods मध्ये पहिल्या parameter म्हणून वापरले जाते.

self चा उपयोग करून आपण त्या specific object च्या attributes आणि methods ला access करू शकतो.

self का आवश्यक आहे?
प्रत्येक object च्या attributes वेगळे असतात. 
self चा उपयोग करून आपण त्या specific object च्या attributes ला access करू शकतो.

self मुळे methods मध्ये कोणत्या object वर operation करायचा आहे हे स्पष्ट होते.

self शिवाय, methods ला कोणत्या object च्या data वर काम करायचं आहे हे कळणार नाही.

self हे keyword नाही
self हे Python मध्ये keyword नाही, परंतु एक convention आहे. 
आपण ते दुसऱ्या नावानेही वापरू शकतो, परंतु self वापरणे हे standard आणि readable code साठी चांगले आहे.

            

'''
# example of self:---->>> 


# class Person:
#     def __init__(self, name):
#         self.name = name  # Assigns the name to the instance

#     def greet(self):
#         print(f"Hello, my name is {self.name}")

# # Creating an instance of Person
# person1 = Person("Alice")
# person1.greet()


# In this example, self.name = name assigns the provided name to the instance's
# name attribute. The greet method then accesses this attribute using self.name.


# Not a Keyword: self is not a reserved keyword in Python;
# it's just a naming convention. You could name it differently, but using self is standard practice for readability.




'''

A constructor is a special method in Python that is automatically 
called when an object of a class is created.
It is defined using the __init__() method. The primary purpose
of a constructor is to initialize 
the attributes of the class when an
object is created.   
It allows you to set initial values for the attributes of the class,
ensuring that the object is in a valid state right from the start.

'''

# class Employee:
#     def __init__(self):
#         print("Constructor will call automatically ,no need to call constructor")

# e1=Employee()



# Consturctor are used when we initialize the object(create object) we can set the value of attribute that are
# present in the class
#


# class Employee:
#     def __init__(self,ename,address,sal):
#         self.name=ename
#         self.addr=address
#         self.salary=sal

#         print("Name of emp is",self.name,"\nAddress of emp is",self.addr,"\nsalary of emp is",self.salary)
# e1=Employee("Rohit","Pune",90000)




# class Bank:
#     def __init__(self,bname,ifsccode):
#         self.name=bname
#         self.code=ifsccode

#         print("Name of bank is",self.name,"\nIFSC code of bank is",self.code)

# b=Bank("SBI","SBI004")




# Taking input form user

# class Student:
#     def __init__(self):
#         self.p=int(input("Enter python marks"))
#         self.j=int(input("Enter java marks"))
#         self.c=int(input("Enter c programming marks"))

#     def disp(self):
#         print("python marks is",self.p)
#         print("Java marks is",self.j)
#         print("C prog marks is",self.c)

#         total=self.p+self.j+self.c
#         print(total)
# s=Student()
# s.disp()


# # # using function
# class student:
#     def disp(self,name):
#         self.n=name
#         print(self.n)
# s=student()
# s.disp("Rohit")


# # using constructor
# class student:
#     def __init__(self,name):
#         self.n=name
#         print(self.n)
# S=student("Rohit")        





'''Special (Magic) Methods

These are special methods that start and end with __ (double underscores), 
also called dunder methods.



__init__: constructor

__str__: string representation

__len__, __add__, etc.'''


'''What is __str__?

__str__ is a special method (dunder/magic method) in Python.

It tells Python how to represent your object as a string,
usually when you use print() or str().

How it Works
If a class has a __str__ method:

When you call print(object), Python calls object.__str__().

The return value must be a string.

If __str__ is not defined, Python falls back to __repr__ (or the default <ClassName object at 0x...>).

'''

# not using __str__

# If you don’t define __str__, Python will print something like:

# class Book:
#     def __init__(self, title):
#         self.title = title

# b = Book("Python")
# print(b)


#  Not very readable. Just tells you it's a Book object at some memory location.


# Using __str__
# By adding __str__, you can define how you want your object to look when printed.


# class Book:
#     def __init__(self, title):
#         self.title = title

#     def __str__(self):
#         return f"Book Title: {self.title}"

# b = Book("Python Mastery")
# print(b)
# print(str(b))  # Calls b.__str__()
# print(type(b))  # <class '__main__.Book'>




# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def __str__(self):
#         return f"Person(Name: {self.name}, Age: {self.age})"

# p = Person("Navanath", 25)
# print(p)  # Calls p.__str__()




'''What is __len__?


__len__ is a special (dunder / magic) method in Python.

It tells Python how to get the length of your object, i.e. what len(obj) should return.

Tells Python how many items are in an object.

Lets your custom classes behave like lists, tuples, strings, etc., when using len().


How it Works:
If your class defines a __len__ method:

When you call len(object), Python actually calls object.__len__().

It must return an integer (≥ 0).


'''


# class BookShelf:
#     def __init__(self, books):
#         self.books = books

#     def __len__(self):
#         return len(self.books)

# shelf = BookShelf(["Python", "Django", "Flask"])
# print(len(shelf))  # calls shelf.__len__()


# 
# class Team:
#     def __init__(self, players):
#         self.players = players

#     def __len__(self):
#         return len(self.players)

# t = Team(["Alice", "Bob", "Charlie"])
# print(len(t))  


#without __len__


# class MyList:
#     def __init__(self, items):
#         self.items = items

# ml = MyList([10, 20, 30])
# print(len(ml))   # TypeError: object of type 'MyList' has no len()




'''What is __add__?


__add__ is a special (dunder / magic) method in Python.

It defines what happens when you use the + operator on your objects.

➡ Normally, + works like this:
print(5 + 10)           # 15
print("Hello" + " World") # Hello World
# But you can customize it for your own classes using __add__.
'''

# Using __add__ in your own class


# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def __add__(self, other):
#         return Point(self.x + other.x, self.y + other.y)

#     def __str__(self):
#         return f"({self.x}, {self.y})"

# p1 = Point(2, 3) # creates a Point object at (2, 3)
# p2 = Point(4, 5) # creates another Point object at (4, 5)

# result = p1 + p2  # calls p1.__add__(p2)
# print(result)     






# Using __add__ for custom objects
# class Vector:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def __add__(self, other):
#         return Vector(self.x + other.x, self.y + other.y)

#     def __str__(self):
#         return f"Vector({self.x}, {self.y})"
# v1 = Vector(1, 2)
# v2 = Vector(3, 4)
# result_vector = v1 + v2  # calls v1.__add__(v2)
# # This will create a new Vector object with x = 4 and y = 6
# print(result_vector)  




# class Word:
#     def __init__(self, text):
#         self.text = text

#     def __add__(self, other):
#         return Word(self.text + " " + other.text)

#     def __str__(self):
#         return self.text

# w1 = Word("Hello")
# w2 = Word("Python")
# print(w1 + w2) # This will print "Hello Python" by calling w1.__add__(w2) and then w1.__str__()


