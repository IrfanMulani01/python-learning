## Q1. Write a program that asks the user to enter two numbers and divides them. 
# Handle ZeroDivisionError and print "Cannot divide by zero!" if the second number is 0.
# try:
#     num1 = int(input("Enter first number: "))
#     num2 = int(input("Enter second number"))
#     print(f"Division is: {num1/num2}")
    
# except ZeroDivisionError:
#     print("zero is non divisible")


## Q2. Write a program that takes a number as input from the user. Handle ValueError if the user enters a non-numeric value like "abc".
# class check:
#     try:
#         num1 = int(input("Enter first number: "))
#         num2 = int(input("Enter second number: "))
#         print(f"Division is: {num1/num2}")
#     except ValueError:
#         print("Enter only numbers not allowed non-numeric")

# c = check()

## Q3. Write a program that opens a file "data.txt" and reads it. 
# Handle FileNotFoundError and print "File not found!" if the file doesn't exist.
class check:
    try:
        f = open("data.txt", "r")
        print(f.read())
        f.close()
    except FileNotFoundError:
        print("file not found")
c = check()