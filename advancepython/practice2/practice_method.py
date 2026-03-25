## Q1. Create a class Student with instance variables name and marks. Add an instance method display() that prints both. 
# Create 2 objects with different data and call display() on each.
# class Student:  # create class name Student
#     def __init__(self, name , marks):   # create cunstructor
#         self.name = name    ##
#         self.marks = marks  # create instance variable
#     def display(self):  # create instance method
#         print(f"Student name is {self.name}")   # print both name and marks
#         print(f"Student Marks is {self.marks}")
#         return
# s1 = Student("irfan", 123)  #create first object
# s1.display()    

# s2 = Student("ritesh", 234) # create second object
# s2.display()

# ## Q2. Create a class BankAccount with instance variables owner and balance. Write instance methods:
# deposit(amount) — adds to balance
# withdraw(amount) — deducts if sufficient, else prints "Insufficient funds"
# show_balance() — prints current balance
# class BankAccount:  # create class Banck Account
#     def __init__(self, owner, balance):
#         self.owner = owner      # create instance variables
#         self.balance = balance
        
#     # create deposite method for adding the amount into current balance
#     def deposite(self,amount):
#         if amount <= 0:
#             print("Enter valid and above 0 amount")
#         else:
#             self.balance += amount      # add new amount in current balance
#             return
    
#     def withdraw(self, amount):
#         if amount <= 0:
#             print("Enter valid and above 0 amount")
#         else:
#             self.balance -= amount  # remove the amount from balance
#             return
        
#     def show_balance(self):
#         print(f"Available balance is {self.balance}")
#         return
    
# ba = BankAccount("irfan", 1000)
# ba.deposite(500)
# ba.withdraw(200)
# ba.show_balance()