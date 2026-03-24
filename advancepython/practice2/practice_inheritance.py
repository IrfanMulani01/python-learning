## Write a class Animal with method eat() and sleep(). Create a subclass Dog that adds a method bark(). 
# Create an object of Dog and call all three methods.
# class animal:
#     def eat(self):
#         print("animal  can eat")
#     def sleep(self):
#         print("animal can sleep")
#         return
# class dog(animal):
#     def bark(self):
#         print("dog bark")
# d = dog()
# d.eat()
# d.sleep()
# d.bark()

## Write a class Vehicle with instance variables brand and speed and a method move(). 
# Create a subclass Car that adds a method play_music().
# class vehicle:
#     def __init__(self, brand, speed):
#         self.brand = brand
#         self.speed= speed
#     def move(self):
#         print(f"{self.brand} this brand vehicle's speed is {self.speed}")
#         return
# class car(vehicle):
#     def __init__(self, brand, speed):
#         super().__init__(brand, speed)
#     def play_music(self):
#         print(f"{self.brand} can play music")
#         return
# c = car("mahindra", 200)
# c.move()
# c.play_music()

## Write a class Person with instance variables name and age and method introduce(). 
# Create subclass Student that adds roll_no and course and overrides introduce().
# class person:
#     def __init__(self, name, age):
#         self._name = name
#         self._age = age
#     def introduce(self):
#         print(f"My name is {self._name} and my age is {self._age}")
#         return
# class student(person):
#     def __init__(self, name, age, roll_no, course):
#         super().__init__(name, age)
#         self.roll = roll_no
#         self.course = course
#     def introduce(self):
#         print(f"My name is {self._name} and my age is {self._age}")
#         print(f"My Roll Number is {self.roll} and my course is {self.course}")
#         return
# s = student("irfan", 21, 36, "MCA")
# s.introduce()

## Write a class Shape with a method draw(). Create a subclass Circle that adds instance variable radius and a method area().
# class shape:
#     def draw(self):
#         print("shap drawing")
#         return
# class circle(shape):
#     def __init__(self, radius):
#         self.radius = radius
#     def area(self):
#         print(f"Area of circle is: {3.14 * self.radius ** 2} ")
#         return
# c = circle(2)
# c.draw()
# c.area()

##  Write a class Bank with method show_bank() displaying bank name. 
# Create subclass SavingsAccount with instance variables account_no and balance and methods deposit() and withdraw()
# class bank:
#     def __init__(self, b_name):
#         self.name = b_name
#     def show_bank(self):
#         print(f"Bank name is {self.name}")
#         return
# class SavingAccount(bank):
#     def __init__(self, b_name, account_no, balance):
#         super().__init__(b_name)
#         self._accno = account_no
#         self._bal = balance
#     def deposit(self):
#         amount = int(input("Enter amount for deposit: "))
#         if amount <= 0:
#             print("Enter valid amount")
#         else:
#             self._bal += amount
#             print(f"{amount} will deposited")
#             print(f"avialable balance is {self._bal}")
#             return
#     def withdraw(self):
#         amount = int(input("Enter amount for Withdraw: "))
#         if amount <= 0:
#             print("Enter valid amount")
#         else:
#             self._bal -= amount
#             print(f"{amount} will withdraw")
#             print(f"Available balance is {self._bal}")
#             return
# s = SavingAccount("sbi", 1243, 1000)
# s.show_bank()
# s.deposit()
# s.withdraw()

## Write a class Phone with method call() and message(). 
# Create subclass Smartphone that adds methods browse_internet() and install_app().
# class phone:
#     def call(self):
#         print("phone can call")
#         return
#     def messege(self):
#         print("phone can messege")
#         return
# class smartphone(phone):
#     def browse_internet(self):
#         print("smartphone can browse internet")
#         return
#     def install_app(self):
#         print("smartphone can install app")
#         return
# s= smartphone()
# s.call()
# s.messege()
# s.browse_internet()
# s.install_app()

##  Write a complete School System using inheritance:
# Base class Person with name and age
# Subclass Staff adding staff_id and department
# Subclass Teacher(Staff) adding subject and method take_class()
# Subclass Student(Person) adding roll_no and method attend_class()

# class person:
#     def __init__(self, name, age):
#         self._name = name
#         self._age = age
# class staff(person):
#     def __init__(self, name, age, staff_id, department):
#         super().__init__(name, age)
#         self.id = staff_id
#         self.dept = department
#     def show(self):
#         print(f"Name of Staff is {self._name} and he's age is {self._age} staff ID is {self.id} and department is {self.dept}")
# class Teacher(person):
#     def __init__(self, name, age, subject):
#         super().__init__(name, age)
#         self.sub = subject
#     def take_class(self):
#         print(f"Teacher name is {self._name} he's age is {self._age} and he teaches on {self.sub}")
# class student(person):
#     def __init__(self, name, age, roll_no):
#         super().__init__(name, age)
#         self.no = roll_no
#     def attend_class(self):
#         print(f"student name is {self._name} and age is {self._age} he's roll number is {self.no}")
# s = staff("irfan", 21, 101, "Mca")
# s.show()
# t = Teacher("sanjay", 21, "math")
# t.take_class()
# st = student("ganesh", 21, 101)
# st.attend_class()

# ## Write:
# Class Animal with method breathe()
# Class Mammal(Animal) with method feed_milk()
# Class Dog(Mammal) with method bark()
# class animal:
#     def breath(self):
#         print("animal can breath")
# class mamal(animal):
#     def feed_milk(self):
#         print("Mamal can feed milk")
# class dog(mamal):
#     def bark(self):
#         print("dog can bark")
# d= dog()
# d.bark()
# d.breath()
# d.feed_milk()

# ##  Write:
# Class Person with name and age
# Class Employee(Person) with company and salary
# Class Manager(Employee) with department and team_size
# Add introduce() at each level and call all using Manager object.
# class person:
#     def introduce(self, name, age):
#         print(f"Person name is {name}")
#         print(f"Person age is {age}")
#         return  
# class Employee(person):
#     def introduce(self, name, age, comp, sal):
#         super().introduce(name, age)
#         print(f"Employee name is {name}")
#         print(f"Employee age is {age}")
#         print(f"Employee Company is {comp}")
#         print(f"Employee Salary is {sal}")
#         return
# class Manager(Employee):
#     def introduce(self, name, age, comp, sal, dep, team_size):
#         super().introduce(name, age, comp, sal)
#         print(f"Manager name is {name}")
#         print(f"Manager age is {age}")
#         print(f"Manager Company is {comp}")
#         print(f"Manager Salary is {sal}")
#         print(f"Manager department is {dep}")
#         print(f"Manager team size is {team_size}")
#         return
# m = Manager()
# m.introduce("irfan", 22, "abc", 10000, "it", 15)

# ## Write:
# Class Printable with method print_doc()
# Class Scannable with method scan_doc()
# Class Printer(Printable, Scannable) that inherits both and adds fax_doc()
# class printable:
#     def print_doc(self):
#         print("printing Document")
# class scannable:
#     def scan_doc(self):
#         print("document will scan")
# class printer(printable, scannable):
#     def fax_doc(self):
#         print("printer can fax the document")
# p = printer()
# p.scan_doc()
# p.print_doc()
# p.fax_doc()

# ## Write:
# Class Animal with method eat()
# Class Dog(Animal) with method bark()
# Class Cat(Animal) with method meow()
# Class Cow(Animal) with method moo()
# Create objects of all subclasses and call their methods.
# class animal:
#     def eat(self):
#         print("animal can eat")
# class dog(animal):
#     def bark(self):
#         print("dog can bark")
# class cat(animal):
#     def meow(self):
#         print("cat can meow")
# class cow(animal):
#     def moo(self):
#         print("cow can moo")
# d = dog()
# d.eat()
# d.bark()
# c = cat()
# c.eat()
# c.meow()
# c1 = cow()
# c1.eat()
# c1.moo()

# ## Write:
# Class Shape with method draw()
# Class Circle(Shape) with radius and method area()
# Class Rectangle(Shape) with length, width and method area()
# Class Triangle(Shape) with base, height and method area()
# class shape :
#     def draw(self):
#         print("shape will draw")
# class circle(shape):
#     def area(self, radius):
#         print(f"Area of circle is: {3.14 * radius ** 2}")
#         return
# class rectangle(shape):
#     def area(self,length,width):
#         print(f"Area of rectangle is: {length*width}")
#         return
# class triangle(shape):
#     def area(self,base,heigth):
#         print(f"Area of triangle is: {base*heigth}")
#         return
# c = circle()
# c.draw()
# c.area(2)
# r = rectangle()
# r.draw()
# r.area(2,5)
# t = triangle()
# t.draw()
# t.area(2,5)

## Write a class Animal with method sound() printing "Some sound". 
# Override it in subclasses Dog, Cat, Cow, and Lion to print their specific sounds.
# class animal:
#     def sound(self):
#         print("animal can generate sound")
#         return
# class dog(animal):
#     def sound(self):
#         print("dog bark")
#         return
# class cat(animal):
#     def sound(self):
#         print("cat meow")
#         return
# class cow(animal):
#     def sound(self):
#         print("cow moo")
#         return
# class lion(animal):
#     def sound(self):
#         print("lion sound")
#         return
# d = dog()
# d.sound()
# c = cat()
# c.sound()
# co = cow()
# co.sound()
# l = lion()
# l.sound()

## Write a class Payment with method pay(amount). Override it in subclasses 
# CashPayment, CardPayment, and UPIPayment with different payment messages.
# class payment:
#     def pay(self,amount):
#         print(f"payble amount is {amount}")
#         return
# class cashPayment(payment):
#     def pay(self,amount):
#         print(f"Cash payble amount is {amount}")
#         return
# class cardPayment(payment):
#     def pay(self,amount):
#         print(f"Card payble amount is {amount}")
#         return
# class UPIPayment(payment):
#     def pay(self,amount):
#         print(f"UPI payble amount is {amount}")
#         return
# ca = cashPayment()
# ca.pay(1000)
# c = cardPayment()
# c.pay(1000)
# upi = UPIPayment()
# upi.pay(1000)

# ## Write a complete School System using inheritance:
# Class Person — name, age
# Class Student(Person) — roll_no, marks, method result()
# Class Teacher(Person) — subject, salary, method teach()
# Class HeadTeacher(Teacher) — experience, method manage()
# class person:
#     def show(self,name,age):
#         print(f"person name is {name}\n person age is {age}")
#         return
# class student(person):
#     def result(self, name, age, roll_no, marks):
#         print(f"student name is {name} \n student age is {age} \n student roll number is {roll_no} \n student marks is {marks}")
#         return
# class teacher(person):
#     def teach(self, name, age, subject, salary):
#         print(f"teacher name is {name} \n teacher age is {age} \n teacher subject is {subject} \n teacher salary is {salary}")
#         return
# class headTeacher(teacher):
#     def manage(self, name, age, subject, salary, experience):
#         print(f"head teacher name is {name} \n head teacher age is {age} \n head teacher salary is {salary} \n head teacher experience is {experience} year")
#         return
# st = student()
# st.result("irfan", 21, 102, 55)
# t = headTeacher()
# t.teach("ganesh", 21,"math",10000)
# t.manage("ritesh", 21, "math", 20000,10)

# ## Write a complete Hospital System using all inheritance types:
# Class Person — name, age
# Class Doctor(Person) — specialization, fees
# Class Surgeon(Doctor) — operation_type (multilevel)
# Class Patient(Person) — disease, ward
# Class MedicalStaff(Person) — role, shift
# Add appropriate methods in each class and create objects to demonstrate
# class person: 
#     def show(self,name,age):
#         print(f"name is {name} age is {age}")
#         return
# class doctor(person):
#     print("doctor details")
#     def disp(self, name, age, specialist, fees):
#         super().show(name, age)
#         print(f"doctor specialist in {specialist}\n doctor's fees is {fees}")
#         return
# class surgeon(doctor):
#     def disp1(self, name, age, specialist, fees, oper_type):
#         print("\nsurgaon details")
#         super().disp(name, age, specialist, fees)
#         print(f"opration type is {oper_type}")
#         return
# class patient(person):
#     def show1(self, name, age, disease, ward):
#         print("\npatient details")
#         super().show(name, age)
#         print(f"patient disease is {disease}\n patient ward is {ward}")
#         return
# class medicalStaff(person):
#     def show2(self, name, age, role, shift):
#         print("\nmedical staff details")
#         super().show(name, age)
#         print(f"staff role is {role}\n staff shift is {shift}")
#         return
# d=surgeon()
# d.disp("sujal",23,"lungs",200)
# d.disp1("irfan",21,"orto",100,"demo")
# p = patient()
# p.show1("ganesh",21,"na",101)
# ms = medicalStaff()
# ms.show2("lila",22,"wardan","nigth")
