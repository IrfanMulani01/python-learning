# Write a function to add two numbers.
# def add(a,b):
#     addition = a + b
#     print(f"Addition of two numbers is: {addition}")
# add(3,6)

# Write a function to check if a number is even or odd.
# def check_number(x):
#     if x % 2 == 0:
#         print("Number is even")
#     else:
#         print("Odd Number")
# check_number(15)

# Write a function to find the area of a rectangle.
# def area(rad):
#     area_rectangle = 3.14* rad * rad
#     print(f"Area of rectangle is: {area_rectangle}")
# area(rad=5)

# Write a function to return the square of a number.
# def squ():
#     square = {i:i * i for i in range(1,11) }
#     print(square)
# squ()

# Write a function to check if a number is positive, negative, or zero.
# def check(x):
#     if x > 0:
#         print("NUmber is positive Number")
#     elif x < 0:
#         print("Number is Negative number")
#     elif x == 0:
#         print("number is zero")
#     else:
#         print("number is invalid")
# check(0)

# Write a function to convert Celsius to Fahrenheit.
# def convert(c):
#     f = (c*1.8)+32
#     print(f)
# convert(34)

# Write a function to find the factorial of a number.
# def fact(num):
#     for i in range(num):
#         num1 = i - 1
#         f=i*num1
#     print(f)
# fact(5)

# Write a function to check if a string is a palindrome.
# def pal():
#     num = int(input("Enter Number: "))
#     temp = num
#     rev = 0
#     while num > 0:
#         digit = num % 10
#         rev = rev * 10 + digit
#         num = num // 10
#     if temp == rev:
#         print("palindrom")
#     else:
#         print("Not palindrom")
# pal()

# Write a function to count vowels in a string.
# def count():
#     var = input("Enter string: ")
#     vowels = "aeiouAEIOU"
#     count = 0
#     for i in var:
#         if i in vowels:
#             count += 1
#     print(count)
# count()

# Write a function to return the reverse of a string.
# def rev():
#     var = input("enter string for reversing: ")
#     rev = ""
#     for i in var:
#         rev = i + rev
#     print(rev)
# rev()

#  Write a function to check if a number is prime.
# def prime():
#     num = int(input("Enter Number: "))
#     i=2
#     prime = True
#     while i < num:
#         if num % i == 0:
#             prime = False
#             break
#         i += 1
#     if prime and num > 1:
#         print("number is prime")
#     else:
#         print("number is not prime")
# prime()

# Write a function to calculate simple interest.
# def cal_interest(interst_rate = 5):
#     principle = int(input("Enter Principle(Amount Investment): "))
#     dur = int(input(("Enter time duration of loan: ")))
#     si = principle*interst_rate*dur/100
#     print(si)
# cal_interest()

# # Write a function that takes *args and returns their sum.
# def add(*num):
#     total = sum(num)
#     print(total)
# add(5,4)

# Write a function that takes **kwargs and prints key-value pairs.
# def function(**kv):
#     for k, v in kv.items():
#         print(k,":",v)
# function(name="irfan", age=21)

