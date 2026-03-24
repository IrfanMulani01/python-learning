# define instance variables inside __init__()
# class demo:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
        
#     def show(self):
#         print(f"Your name is {self.name}")
#         print(f"Your age is {self.age}")
# d = demo("irfan", 21)
# d.show()


## In the Circle class, pi = 3.14 is defined outside __init__().
# class circle:
#     pi = 3.14
#     def __init__(self, radius):
#         self.radius = radius
#     def show(self):
#         print(f"Area of Circle is: ", self.pi * self.radius ** 2)
# c = circle(2)
# c.show()

## If you do Circle.pi = 3.14159 after creating c1 and c2, and then call c1.area() again 
# class circle:
#     def __init__(self, radius):
#         self.radius = radius
#     def area(self):
#         print("Area of circle is:",self.pi * self.radius ** 2)
# circle.pi = 3.14     # class variable delared   
# c1 = circle(2)
# c2 = circle(2)
# c1.area()
# c2.area()

## In the Calculator class, result is a local variable. Can you access result outside the method like calc.result
# class calculater:
#     def add(self, var_1, var_2):
#         result = var_1 + var_2
#         return result
#     def sub(self, var_1, var_2):
#         result = var_1 - var_2
#         return result
#     def mul(self, var_1, var_2):
#         result = var_1 * var_2
#         return result
#     def div(self, var_1, var_2):
#         result = var_1 / var_2
#         return result
# calc = calculater()
# # print(calc.result)
# print(calc.add(12,5))
# print(calc.sub(12,5))
# print(calc.mul(12,5))
# print(calc.div(12,5))

## Rewrite the Circle class so that pi becomes an instance variable instead of a class variable
# class circle:
#     def __init__(self, radius,pi=3.14):
#         self.pi = pi
#         self.radius = radius
#     def area(self):
#         print("Area of circle is:", self.pi * self.radius ** 2)
# c = circle(2)
# c.area()

## Q1. Write a class Car with instance variables brand, model, and price. Add a method show_details() to display all details.
# class car:
#     def __init__(self, brand_name, model_name, price):
#         self.brand = brand_name
#         self.model = model_name
#         self.price = price
#     def show_details(self):
#         print(f"Brand is: {self.brand} \n Model of {self.brand} is: {self.model} \n Price of {self.model} is: {self.price}")
# c = car("Mahindra" , "SCORPIO", 2000000)
# c.show_details()

## Q2. Write a class Student with instance variables name, roll_no, and marks. Add a method result() that prints Pass if marks >= 40 else Fail.
# class student:
#     def __init__(self, stud_name, stud_roll_no, marks):
#         self.name = stud_name   
#         self.roll_no = stud_roll_no
#         self.marks = marks
#     def result(self):
#             if self.marks >= 40:
#                 print(f"Student {self.name} ({self.roll_no}) is Passed out")
#             else:
#                 print(f"Student {self.name} ({self.roll_no}) is Failed")
# stud= student(11, "irfan", 99)
# s1 = student("Alice", 101, 75)
# s2 = student("Bob", 102, 35)
# stud.result()
# s1.result()
# s2.result()

## Q3. Write a class BankAccount with instance variables owner and balance. Add methods deposit(amount) and withdraw(amount) with proper validation.
# class BankAccount:
#     def __init__(self, owner, balance):
#         self.owner = owner
#         self.balance = balance
#     def deposit(self, amount):
#         print(f"Your Current balance is {self.balance}")
#         if amount <= 0:
#             print("Please Enter Valid amount")
#         else:
#             self.balance += amount
#             print(f"Amount Successfully Deposited")
#             print(f"After Deposit Balance {self.balance}") 
#     def withdraw(self, amount):
#         if amount <= 0:
#             print("Enter Valid Amount")
#         else:
#             self.balance -= amount
#             print("Amount Successfully Withdraw")
#             print(f"After Withdraw balance is {self.balance}")
#     def show_balance(self):
#         print("Owner ", self.owner,"'s avalable balance is:", self.balance)
# ba = BankAccount("irfan", 10000)
# ba.deposit(2000)
# ba.show_balance()
# ba.withdraw(4000)
# ba.deposit(0)

## Q33. Write a class ShoppingCart with instance variable items = []. Add methods add_item(item, price), remove_item(item), and total_bill().
# class shoppingCart:
#     def __init__(self):
#         self.items = []
    
#     def add_item(self, item, price):
#         product = {"item": item, "price": price}
#         self.items.append(product)
#         print(f"Product {item} will add to cart. Price Rs{price}")
    
#     def remove_item(self, item):
#         for product in self.items:
#             if product["item"] == item:
#                 self.items.remove(item)
#                 return
#         print(f"{item} is removed")
    
#     def total_bill(self):
#         if len(self.items) == 0:
#             print("cart is empty")
#             return
#         total = 0
#         print("\n------------ Bill ------------")
#         for product in self.items:
#             print(f"{product["item"]} - Rs.{product["price"]}")
#             total += product["price"]
#         print(f"Total Bill: {total}")
#         print("-------------- Bill Generated -----------------\n")
# sc = shoppingCart()
# sc.add_item("MOuse", 1000)
# sc.add_item("monitor", 2000)
# sc.add_item("keyboard", 500)
# sc.total_bill()
# sc.remove_item("mouse")

## Q32. Write a class Hostel with class variable total_rooms = 100 and instance variables student_name and room_no. Add a method allocate_room() that decrements available rooms each time.
# class hostel:
#     total_room = 100
#     def __init__(self, stud_name, stud_room_no):
#         self.name = stud_name
#         self.no = stud_room_no
    
#     def allocated(self):
#         print(f"{self.name}, {self.no}")
#         self.total_room -= 1
#         print(f"{self.no} was allocated")
#         print(f"Available rooms {self.total_room}")
        
# h = hostel("irfan", 15)
# h.allocated()

## Q34. Write a class Quiz with class variable total_questions = 10 and instance variables player_name and score. Add a method result() 
# that shows percentage and grade using local variables.
# class quiz:
#     total_questions = 10
#     def __init__(self, player_name, score):
#         self.name = player_name
#         self.score = score
    
#     def result(self):
#         print(f"{self.name}, {self.score}")
#         sub = 500
#         per = self.score / sub *100
#         print(f"Percentage is {per}")

#         if per <= 50 or per == 50:
#             print("grade E")
#         elif per == 60:
#             print("grade D")
#         elif per == 70 :
#             print("grade C")
#         elif per == 80 :
#             print("grade B")
#         elif per == 90 or per >= 90:
#             print("grade A")
#         else:
#             print("not valid score")
# q = quiz("umair", 450)
# q.result()

## Q35. Write a complete School Management mini program using:
# Class variable for school name and total students
# Instance variables for student name, age, and grade
# Local variables inside methods for calculations
# Methods: admit(), display_info(), promote(), and total_count()

# class School:
#     school_name = "Allana "
#     total_stud = 150

#     def __init__(self, stud_name, stud_age, grade):
#         self.name = stud_name
#         self.age = stud_age
#         self.grade = grade
    
#     def calculation(self):
#         grade_val = "ABCDE"
#         for i in self.grade:
#             if i in grade_val:
#                 print("90")
    
#     def admit(self, date):
#         print(f"School name is {self.school_name}")
#         print(f"Addmission Date is {date}")
    
#     def display_info(self):
#         print(f"{self.name}, {self.age}")
    
#     def total_count(self):
#         count = 0
#         if len(self.name) >= 0:
#             count += 1
#         print(f"{count}")
# s = School("irfan", 21, "E")
# s1 = School("umair", 20, "B")
# s.calculation()
# s1.calculation()
# s.admit(1/5/2026)
# s1.admit(2/5/2024)
# s.display_info()
# s1.display_info()
# s.total_count()
# s1.total_count()

##Q27. Write a class Hospital with:
# Class variable hospital_name
# Instance variables patient_name and disease
# Method admission_summary() combining all three variable types
# class hospital:
#     hospital_name ="Goldan Jublee"
#     def __init__(self, paitiant_name, disease):
#         self.name = paitiant_name
#         self.disease = disease
#     def addmission_summary(self):
#         print(f"Hospital Name: {self.hospital_name}")
#         print(f"Paitiant Name: {self.name},\n Patiant Diasease: {self.disease}")
#         date = int(input("Enter Addmission Date: "))
#         d_name = input("Enter Doctor name: ")
#         print(f"Addmission date is {date}")
#         print(f"doctor name{d_name}")
# h = hospital("irfan", "cuff")
# h.addmission_summary()