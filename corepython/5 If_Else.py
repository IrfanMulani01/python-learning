'''
=================================
IF – ELIF – ELSE (CONTROL FLOW)
=================================

If-else statements control the flow of a program.
They are also called control statements.

The if-else statement is used for decision-making.

• If the given condition is TRUE → if block executes
• If the condition is FALSE → else block executes

elif:
If the previous condition was false, then try this condition.

Indentation:
Indentation refers to the spaces at the beginning of a line of code.
In Python, indentation is mandatory to define a block of code.

Standard indentation = 4 spaces or 1 tab
'''

'''
Python if Statement
-------------------
Syntax:

if condition:

    statement(s)
'''

# Example: Check if number is positive

# num = 3
# if num > 0:
    
#     print(num, "is a positive number")

# print("This is always printed")



'''
Python if-else Statement
-----------------------
Syntax:

if condition:
    statement(s)
else:
    statement(s)
'''

# Example: Rain decision

# raining = input("Is it raining (yes/no): ")
# if raining == "yes":
#     print("Do not water the plants")
    
# else:
#     print("Water the plants")



# Logical OR example

# holiday = "Sunday"
# if holiday == "Sunday" or holiday == "National":
#     print("Off Day")
# else:
#     print("Working Day")



# Logical AND example

# holiday = "National"
# if holiday == "Sunday" and holiday == "National":
#     print("Off Day")
# else:
#     print("Working Day")



'''
Write a program to check whether a number entered by user is even or odd.

If a number is completely divisible by 2 (remainder = 0),
then it is an even number.
Otherwise, it is an odd number.
'''



'''
Python if-elif-else Statement
----------------------------
Syntax:

if condition:
    block
elif condition:
    block
else:
    block
'''

# Example

# month = input("Enter a month: ")

# if month == "Saturday":
#     print("Holiday")
# elif month == "June":
#     print("Vacation Month")
# else:
#     print("Working Days")



'''
Check the maximum of three numbers
'''

# a = int(input("Enter number a: "))
# b = int(input("Enter number b: "))
# c = int(input("Enter number c: "))

# if a > b and a > c:
#     print(a, "is the maximum")
# elif b > a and b > c:
#     print(b, "is the maximum")
# elif c > a and c > b:
#     print(c, "is the maximum")
# else:
#     print("Invalid input")



'''
Calculator using if-elif
'''

# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# op = input("Enter operator (+, -, *, /): ")

# if op == "+":
#     print(a + b)
# elif op == "-":
#     print(a - b)
# elif op == "*":
#     print(a * b)
# elif op == "/":
#     print(a / b)
# else:
#     print("Invalid operator")



'''
If-Elif Ladder Example
'''

# a = 3
# if a < 3:
#     print("Value is less than 3")
# elif a > 13:
#     print("Value is greater than 13")
# elif a > 7:
#     print("Value is greater than 7")
# else:
#     print("No condition matched")





# print("""
# 1. BIKE
# 2. CAR
# 3. SUV
# 4. SEDAN
# """)
# choice = int(input("Select your ride: "))

# if choice == 1:
#     print("You selected Bike")
# elif choice == 2:
#     print("You selected Car")
# elif choice == 3:
#     print("You selected SUV")
# elif choice == 4:
#     print("You selected Sedan")
# else:
#     print("Wrong choice")



'''
Nested if-else
--------------

Nested if-else means an if-else statement inside another if-else.

Used when multiple conditions depend on each other.
'''

# var = 100

# if var  < 200:
#     print("Less than 200")
#     if var == 150:
#         print("Value is 150")
#     elif var == 100:
#         print("Value is 100")
# else:
#     print("Greater than 200")



'''
Indentation in Python
--------------------
Python uses indentation instead of curly braces { }.

If indentation is incorrect → IndentationError

Standard indentation = 4 spaces
'''



'''
Check number type using nested if
'''

# num = int(input("Enter a number: "))

# if num >= 0:
#     if num == 0:
#         print("Zero")
#     else:
#         print("Positive number")
# else:
#     print("Negative number")



'''
Membership Operator Example
'''

# names = ["harry", "shubham", "rohit", "aditi"]
# name = input("Enter name: ")

# if name in names:
#     print("Name found")
# else:
#     print("Name not found")



'''
Shorthand if Statement
---------------------
Used when only one statement exists in if block.
'''

# name = "Rocky"
# if name == "Rocky": print("Hello Rocky")



'''
Shorthand if-else Statement
--------------------------
Syntax:

statement_if_true if condition else statement_if_false
'''

# name = "Dan"
# print("Hello Dan") if name == "Dan" else print("Unknown User")



'''
The pass Keyword
----------------
pass means: do nothing and move to next statement.
Used when a block is required syntactically but no action is needed.
'''

# a = 33
# b = 200

# if b > a:
    
#     pass
    
# print("Program continues")
