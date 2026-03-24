'''
Types of Inheritance in Python:

Inheritance means a class (child) inherits the properties and behaviors (variables and methods) 
of another class (parent).

It helps in code reusability and organizing code better.

The types of inheritance depend on the number of children and parents involved. 

Ever heard of this dialogue from relatives “you look exactly like your father/mother” the reason behind
this is called 'inheritance'. From the Programming aspect, It generally means “inheriting or transfer of 
characteristics from parent to child class without any modification”. The new class is called
the derived/child class and the one from which it is derived is called a parent/base class.

Types of Inheretance:
1. Single Inheritance          	One child class inherits from one parent class
                                एकच child class एका parent class पासून गुण घेते.

2. Multiple Inheritance        	One child class inherits from more than one parent class
                                एकच child class एकापेक्षा जास्त parent classes पासून गुण घेते
                                
                                
3. Multilevel Inheritance	    A class inherits from a child class which in turn inherits from another parent class
                                chain मधून – एक class दुसऱ्या पासून, आणि पुढचा तिसऱ्या पासून.


4. Hierarchical Inheritance 	Multiple child classes inherit from a single parent class
                                एकाच parent class पासून अनेक child classes तयार होतात.



5. Hybrid Inheritance	       Combination of any of the above inheritance types
                               वरील प्रकारांचे मिश्रण.


'''
# class Human:     #parent class
#     def __init__(self, name, age, gender):
#         self.name = name
#         self.age = age
#         self.gender = gender

#     def description(self):
#         print(f"Hey! My name is {self.name}, I'm a {self.gender} and I'm {self.age} years old")

# class Boy(Human):    #child class
#     def schoolName(self, schoolname):
#         print(f"I study in {schoolname}")

# b = Boy('John', 15, 'male')
# b.description()
# b.schoolName("Sunshine Model School")

# h = Human('John', 15, 'male')
# h.description()
# h.schoolName("Sunshine Model School")


'''
Single Inheritance:
Single inheritance allows a derivate class to inherit properties of one parent class,
 and this allows code reuse and the introduction of additional features in existing code.
(When a child class inherits only a single parent class.)
'''

# class Parent1:  
#     def func1(self):  
#         print ("This function is defined inside the parent class.")  
  
# # now, we will create the Derived class  
# class Child1(Parent1):  
#     def func2(self):  
#         print ("This function is defined inside the child class.")  
  
# # Driver's code  
# object = Child1()  
  
# object.func2() 
# object.func1() 



'''
Python Super() Function
Super function allows us to call a method from the parent class.
'''
# class Parent:
#      def func1(self):
#          print("this is function 1")
# class Child(Parent):
#     def func2(self):
#      super().func1()
#      print("this is function 2")
 
# ob = Child()
# ob.func2()




# class Human:
#     def __init__(self,name,age,gender):
#         self.name = name
#         self.age = age
#         self.gender = gender
#     def description(self):
#         print(f"Hey! My name is {self.name}, I'm a {self.gender} and I'm {self.age} years old")
    
#     def dance(self):
#         print("I can dance")
        
# class Girl(Human):
#     def dance(self):
#         print("I can do classic dance")
#     def activity(self):
#         super().dance()
        
# g = Girl('Lily', 20, 'girl')

# g.description()

# g.activity()


