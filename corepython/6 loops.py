'''
==========================
PYTHON LOOPS
==========================

Python provides loops to repeat a block of code multiple times.

There are two types of loops:
1. for loop
2. while loop
'''

'''
Python for Loop
---------------
A for loop is used to repeat a block of code for a specific number of times.
It is commonly used to iterate over sequences such as:
list, tuple, string, dictionary, or range.

Iterating over a sequence is called traversal.
'''

'''
Syntax:
for variable in sequence:
    statements
'''

# Example: for loop with list

# list1 = [1, 2, 3, 4, 5]
# for item in list1:
#     print(item)


# Example: for loop with string
# st = "max"
# for var in st:
#     print(var)
    
 



'''
Range() Function
----------------
range() is used to generate a sequence of numbers.

Syntax:
range(start, stop, step)

• start → starting value (default = 0)
• stop  → ending value (excluded)
• step  → increment value (default = 1)
'''

# Convert range to list
# print(list(range(10)))          # 0 to 9
# print(list(range(2, 8)))         # 2 to 7
# print(list(range(0, 20, 5)))     # step of 5

# Convert range to tuple
# print(tuple(range(10)))
# print(tuple(range(2, 20, 3)))


'''
Iterating using index
'''

# genre = ['pop', 'rock', 'jazz']
# for i in range(len(genre)):
#     print("I like", genre[i])


'''
break statement
---------------
break is used to exit the loop immediately.
'''

# for i in range(10):
#     if i == 8:
#         break
#     print(i)


'''
continue statement
------------------
continue skips the current iteration and moves to the next iteration.
'''

# for i in range(13):
#     if i == 7:
#         continue
#     print(i)


'''
pass statement
--------------
pass means "do nothing".
It is used when a statement is syntactically required but no action is needed.
'''

# i = 3
# if i < 3:
#     pass
# print("Welcome to Python")


'''
Even and Odd numbers using for loop
'''

# list1 = []
# list2 = []

# for i in range(1, 21):
#     if i % 2 == 0:
#         list1.append(i)
#     else:
#         list2.append(i)

# print("Even numbers:", list1)
# print("Odd numbers:", list2)


'''
String method with loop
'''

# names = ["Sonam", "Anidha", "Priyanka", "Sonali"]
# for name in names:
#     if name.startswith("S"):
#         print("Hello", name)


'''
Loop with Dictionary
'''

# name = "Pratik"
# data = {"Suraj": 12, "Nikhil": 3, "Pratik": 7}

# for key in data:
#     if key == name:
#         print(data[key])
#         break
# else:
#     print("Name not found")


'''
Prime number program
'''

# num = int(input("Enter a number: "))
# prime = True

# for i in range(2, num):
#     if num % i == 0:
#         prime = False
#         break

# if prime:
#     print(num, "is a Prime number")
# else:
#     print(num, "is not a Prime number")


'''
Factorial program
'''

# num = int(input("Enter a number: "))
# factorial = 1

# for i in range(1, num + 1):
#     factorial *= i

# print("Factorial is:", factorial)


'''
Multiplication table using for loop
'''

# n = int(input("Enter a number: "))
# for i in range(1, 11):
#     print(f"{n} x {i} = {n*i}")


'''
zip() Function
--------------
zip() combines multiple sequences element-wise.
It stops when the shortest sequence ends.
'''

# l1 = [10, 20, 30]
# l2 = [40, 50, 60, 70]

# for a, b in zip(l1, l2):
#     print(a, "-", b)


'''
enumerate() Function
-------------------
enumerate() returns index and value together.
'''

# for i, v in enumerate(["tic", "tac", "toe"]):
#     print(i, v)


'''
reversed() Function
------------------
Used to loop in reverse order.
'''

# for i in reversed(range(1, 10, 2)):
#     print(i)


'''
sorted() Function
----------------
Returns a sorted list without changing the original.
'''

# basket = ['apple', 'banana', 'apple','cherry', 'orange']
# for fruit in sorted(set(basket)):
#     print(fruit)


'''
==========================
WHILE LOOP
==========================

A while loop executes a block of code as long as the condition is TRUE.
The condition is checked before executing the loop body.
'''

'''
Syntax:
while condition:
    statements
'''

# Example: while loop

# i = 5
# while i <= 10:
#     print(i)
#     i += 1


'''
Reverse counting using while loop
'''

# a = 7
# while a >= 1:
#     print(a)
#     a -= 1


'''
Infinite loop with break
'''

# while True:
#     name = input("Enter your name: ")
#     if name == "John":
#         break
# print("Correct name entered")

# while True:
#     print('hello world')
#     break


'''
LCM of 4 and 7
'''

# x = 0
# while True:
#     x += 1
#     if not (x % 4 or x % 7):
#         break
# print(x, "is divisible by 4 and 7")




'''
Password validation using while loop
'''

# password = "python123"
# user_input = ""

# while user_input != password:
#     user_input = input("Enter password: ")

# print("Access Granted")



