## Q21. Write a class Person with private variable __age. Add a getter get_age() and setter set_age(age) that only allows age between 1 and 120.
# class person:
#     def __init__(self, name, age):
#         self.__name = name
#         self.__age = None
#         self.set_age(age)
#     def get_age(self):
#         self.__age
#     def set_age(self, age):
#         if 1<= age <= 120:
#             self.__age =age
#             print(f"{self.__age} valid age Entered")
#         else:
#             print(f"Enter valid age between 1 to 120")
#     def display(self):
#         print(f"\nName is {self.__name}")
#         print(f"Age is {self.__age}")
# p = person("irfan", 90)
# p.display()

## 2. Write a class Product with private variable __price. Add getter and setter methods where the setter rejects negative prices.
# class product:
#     def __init__(self, name, price):
#         self.name = name
#         self.__price = None
#         self.set_price(price)
#     def get_price(self):
#         self.__price
#     def set_price(self, price):
#         if price == 0:
#             print("Enter valid price")
#         else:
#             self.__price = price
#             return
#     def display(self):
#         print(f"name of product is {self.name}")
#         print(f"Price of {self.name} is {self.__price}")
# p = product("mouse", 2000)
# p.display()

## Write a class Person with protected variable _name and _age. Add a method display() to access and print them.
# class person:
#     def __init__(self):
#         self._name = []
#         self._age = []
#     def display(self):
#         name= input("Enter name: ")
#         age = int(input("Enter age: "))
#         self._name = name
#         self._age = age
#         print(f"Name is {self._name}")
#         print(f"Age is {self._age}")
#         return 
# p = person()
# p.display()

## Write a class BankAccount with protected variable _balance. Add methods deposit() and get_balance() to manage and access balance.
# class BankAccount:
#     def __init__(self, acctype, balance):
#         self._balance= None
#         self.acctype = acctype
#         self.deposit(balance)
#     def deposit(self, balance):
#         if balance >= 0:
#             self._balance = balance
#             print(f"{self._balance} successfully deposited")
#         else:
#             print(f"{self._balance} not valid amount")
#             return
#     def get_balance(self):
#         print(f"Total Balance is {self._balance}")
#         return
# ba = BankAccount("saving", 1000)
# ba.get_balance()

## Write a class Employee with protected variables _name and _department. Create a subclass Manager that accesses these variables 
# and adds a new variable _team_size
# class Employee:
#     def __init__(self, name, dept):
#         self._name = name
#         self._dept = dept
# class Manager(Employee):
#     def display(self):
#         size = int(input("Enter Team Size: "))
#         self._team_size = size
#         print(f"Employee Name is {self._name}")
#         print(f"Employee {self._name}'s department is {self._dept}")
#         print(f"Team size of {self._dept} is {self._team_size}")
#         return
# m = Manager("irfan", "it")
# m.display()

## Write a class Vehicle with protected variable _fuel_type. Create a subclass Car that inherits 
# and displays _fuel_type along with its own instance variable brand.
# class vehical:
#     def __init__(self, fuel_type, brand):
#         self._fuel_type = fuel_type
#         self.brand = brand
# class Car(vehical):
#     def display(self):
#         print(f"{self.brand} this brand's fuel Type is {self._fuel_type}")
#         return
# c = Car("petrol", "mahendra")
# c.display()

## Write a class Animal with protected variable _species. Create a subclass Dog that 
# accesses and prints _species from the parent class.
# class animal:
#     def __init__(self, species):
#         self._species=species
# class dog(animal):
#     def display(self):
#         print(f"{self._species} is Dog species")
#         return
# d = dog("dobarman")
# d.display()

## Write a complete Library Management program using encapsulation with:
# Private variables __book_name, __author, __available = True
# Methods borrow_book() that sets available to False if book is available
# Method return_book() that sets it back to True
# Method book_status() to show current availability
# Getters and setters for book name and author with validation
# class library:
#     def __init__(self, book, author):
#         self.__name = book
#         self.__author = None
#         self.__available = True
#         self.set_book(author)
#     def barrow_book(self):
#         if len(self.__name) == 0:
#             self.__available = False
#             print(f"{self.__name} is {self.__available}")
#         else:
#             print("Enter book name")
#     def return_book(self):
#         if self.__name == self.__available:
#             print(f"{self.__name} is returned")
#         else:
#             print(f"{self.__name} is not returned")
#             return
#     def get_book(self):
#         self.__author
#     def set_book(self, author):
#         self.__author = author
#         return
#     def display(self):
#         print(f"Book is {self.__name}")
#         print(f"{self.__author} of {self.__name}")
#         return
# l = library("python", "guido van russom")
# l.barrow_book()
# l.return_book()
# l.display()

## Write a class Pizza with instance variables size, crust, and price. Add a method order_summary() 
# that displays the full order details.
# class pizza:
#     def __init__(self, size, crust, price):
#         self.size = size
#         self.crust = crust
#         self.price = price
#     def order_summary(self):
#         print("\n===========================")
#         print("       🍕 PIZZA ORDER      ")
#         print("===========================")
#         print(f"  Size   : {self.size}")
#         print(f"  Crust  : {self.crust}")
#         print(f"  Price  : ₹{self.price}")
#         print("===========================\n")
# p = pizza("large", "sangr", 200)
# p1 = pizza("medium","dagag", 150)
# p.order_summary()
# p1.order_summary()

## Write a class Train with instance variables train_no, source, destination, and fare. 
# Add a method journey_info() to display all details.
# class train:
#     def __init__(self, train_no, source, destination):
#         self.__no = train_no
#         self.__source = source
#         self.__dest = destination
#     def journey_info(self):
#         print("\n===============================================")
#         print("                 Orde summary                   ")
#         print("===============================================")
#         print(f"    Train Number    :   {self.__no}")
#         print(f"    Source          :   {self.__source}")
#         print(f"    Destination     :   {self.__dest}")
#         print("===============================================")
#         print("                     End                         ")
#         print("===============================================\n")
# tr= train(71402, "Baramati", "Pune")
# tr1= train(71401, "Pune", "Baramati")
# tr.journey_info()
# tr1.journey_info()

# ##  Write a class SocialMedia with:
# Private variables __username and __password
# Setter for password that enforces: min 8 chars, must contain a digit
# Method login(username, password) that validates credentials
# Method change_password(old, new) that verifies old password before updating

# class socialMedia:
#     def __init__(self):
#         self.__username = ""
#         self.__password = ""
#     def setter(self):
#         self.__username = input("Enter your usename: ")
#         pas = "1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
#         passinput = input("Enter Your password: ")
#         for i in passinput:
#             if i not in pas:
#                 print("Invalid character in password")
#                 return
#         self.__password = passinput
#         print("Password accepted")
#     def login(self):
#         username= input("enter username:")
#         passinput = input("Enter Your password: ")
#         if self.__username == username and self.__password == passinput:
#             print("Login successful. Welcome", self.__username)
#         else:
#             print("Invalid username or password")
#     def change_password(self):
#         old = input("Enter old password: ")
#         if old != self.__password:
#             print("Old password is incorrect.")
#             return
#         passinput = input("Enter New password: ")
#         confirmpass = input("Enter Confirm Password: ")
#         if passinput == confirmpass:
#             self.__password = confirmpass
#             print("Password changed")
#             return
# sm = socialMedia()
# sm.setter()
# sm.login()
# sm.change_password()

# ## Write a class Hospital with:
# Private variables __patient_name, __age, __disease
# Protected variable _ward
# Getters and setters for all private variables
# Method admit() that displays admission details
# import datetime as dt 
# class hospital:
#     def __init__(self):
#         self.__patient_name = ""
#         self.__age = []
#         self.__disease = ""
#         self._ward = []
#     def getter(self):
#         self.__patient_name = input("Enter Patient Name: ")
#         self.__age = int(input("Enter Patient age: "))
#         self.__disease = input("Enter patient disease: ")
#         self._ward = int(input("Enter ward number: "))
#     def setter(self):
#         print(f"Patient name is {self.__patient_name} ")
#         print(f"Patient age is {self.__age}")
#         print(f"Patient Disease is {self.__disease}")
#         print(f"Patient's ward number is {self._ward}")
#     def admit(self):
#         print("\n============================ Admit Card  =============================")
#         print(f"                Patient Name    :   {self.__patient_name}")
#         print(f"                Patient Age     :   {self.__age}")
#         print(f"                Patient Disease :   {self.__disease}")
#         print(f"            Patient Ward Number :   {self._ward}")
#         print(f"                Admit Date      :   {dt.datetime.now().date()}")
#         print("============================     End     =============================\n")
# h = hospital()
# h.getter()
# h.setter()
# h.admit()

