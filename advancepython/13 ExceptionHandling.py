"""
========================================
EXCEPTION HANDLING IN PYTHON
========================================

Definition:
-----------
An exception is a runtime error that
stops the normal execution of a program.

Exception handling allows us to:
✔ Handle errors gracefully
✔ Prevent program crash
✔ Continue program execution
"""

# ==================================================
# WHY EXCEPTION HANDLING IS IMPORTANT
# ==================================================

"""
✔ Prevents sudden program termination
✔ Helps identify errors clearly
✔ Improves program reliability
✔ Used heavily in real applications
"""

# ==================================================
# COMMON BUILT-IN EXCEPTIONS
# ==================================================

"""
✔ ZeroDivisionError
✔ ValueError
✔ TypeError
✔ IndexError
✔ KeyError
✔ FileNotFoundError
"""

# ==================================================
# BASIC try-except
# ==================================================

# try:
#     x = int(input("Enter a number: "))
#     y = int(input("Enter another number: "))
#     print(x / y)
# except ZeroDivisionError:
#     print("Cannot divide by zero")
# except ValueError:
#     print("Please enter valid integers")

# ==================================================
# PROGRAM LOGIC
# ==================================================

"""
1. Code inside try is executed
2. If error occurs, control goes to except
3. Program does not crash
"""

# ==================================================
# MULTIPLE except BLOCKS
# ==================================================

# try:
#     a = int(input("Enter number: "))
#     b = int(input("Enter number: "))
#     print(a / b)
# except ZeroDivisionError:
#     print("Division by zero not allowed")
# except ValueError:
#     print("Invalid input")
# except Exception as e:
#     print("Error:", e)

# ==================================================
# try-except-else
# ==================================================

"""
else block executes if no exception occurs
"""

# try:
#     num = int(input("Enter number: "))
#     print(100 / num)
# except ZeroDivisionError:
#     print("Zero not allowed")
# else:
#     print("Execution successful")

# ==================================================
# try-except-finally
# ==================================================

"""
finally block always executes
Used for cleanup code
"""

# try:
#     f = open("dataa.txt", "r")
#     print(f.read())
# except FileNotFoundError:
#     print("File not found")
# finally:
#     print("File operation attempted")

# ==================================================
# RAISING EXCEPTIONS
# ==================================================

"""
raise keyword is used to create
custom error situations
"""

# age = int(input("Enter age: "))
# if age < 18:
#     raise ValueError("Age must be 18 or above")
# else:
#     print("Access granted")

# ==================================================
# CUSTOM EXCEPTION
# ==================================================

"""
User-defined exceptions improve
error clarity in applications
"""

# class NegativeNumberError(Exception):
#     pass

# try:
#     num = int(input("Enter number: "))
#     if num < 0:
#         raise NegativeNumberError("Negative numbers not allowed")
#     print("Valid number:", num)
# except NegativeNumberError as e:
#     print(e)

# ==================================================
# EXCEPTION CHAINING
# ==================================================

"""
Raising one exception from another
"""

# try:
#     x = int("abc")
# except ValueError as e:
#     raise RuntimeError("Conversion failed") from e

# ==================================================
# BEST PRACTICES
# ==================================================

"""
✔ Catch specific exceptions first
✔ Avoid bare except
✔ Use finally for resource cleanup
✔ Do not hide errors silently
"""

# ==================================================
# QUICK SUMMARY (EXAM READY)
# ==================================================

"""
Exception Handling:
-------------------
try → test code
except → handle error
else → runs if no error
finally → always runs
raise → create exception
"""
