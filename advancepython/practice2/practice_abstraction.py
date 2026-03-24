## 1. Abstract Base Class Create an abstract class Shape with an abstract method area(). Implement it in Circle and Rectangle subclasses.
from abc import ABC, abstractclassmethod, abstractproperty
# class shape(ABC):
#     @abstractclassmethod
#     def area(self):
#         pass
# class circle(shape):
#     def area(self, radius):
#         print(f"Area of Circle is {3.14 * radius ** 2}")
#         return
# class rectangle(shape):
#     def area(self, l , b):
#         print(f"Area of rectangle is {l*b}")
#         return
# c = circle()
# c.area(2)
# r = rectangle()
# r.area(2,4)

## 2. Interface via ABC
# Define an abstract class Animal with abstract methods speak() and move(). Create Dog and Bird classes that implement both.
# class animal(ABC):
#     @abstractclassmethod
#     def speak(self):
#         pass
#     @abstractclassmethod
#     def move(self):
#         pass
# class dog(animal):
#     def speak(self):
#         print("Dog can bark")
#     def move(self):
#         print("dog can move")
# class bird(animal):
#     def speak(self):
#         print("bird can speak")
#     def move(self):
#         print("bird can move")
# d = dog()
# b = bird()
# d.speak()
# d.move()
# b.speak()
# b.move()

## 3. Property Abstraction
# Create an abstract class BankAccount with an abstract property balance. Implement it in SavingsAccount that stores balance privately.
# class BankAccount(ABC):
#     @abstractclassmethod
#     def show(self):
#         pass
#     @property
#     def balance(self):
#         pass
# class SavingAccount(BankAccount):
#     def __init__(self, balance):
#         self.__balance = balance
#     @property
#     def balance(self):
#         return self.__balance
#     def show(self):
#         print(f"available balance is {self.__balance}")
# sa = SavingAccount(1000)
# # sa.balance()
# sa.show()

