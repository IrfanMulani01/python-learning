
# '''
# =============================================
# Python Casting: Type Conversion & Type Casting
# =============================================

# We can convert one data type into another.
# This process is called Type Conversion or Type Casting.

# Example:
# int → float
# string → int
# bool → float
# '''

# '''
# There are two types of Type Conversion:
# 1. Implicit Type Conversion
# 2. Explicit Type Conversion
# '''

# # -----------------------------------------
# # 1. IMPLICIT TYPE CONVERSION
# # -----------------------------------------
# '''
# Python automatically converts one data type into another.
# No user involvement is required.
# '''

# # Example 1
# a = 7
# b = 5.6
# c = a + b

# print(c)
# print(type(c))   # float

# # Example 2
# num = 123
# num1 = 1.23
# num_new = num + num1

# print("datatype of num:", type(num))
# print("datatype of num1:", type(num1))
# print("Value of num_new:", num_new)
# print("datatype of num_new:", type(num_new))

# # -----------------------------------------
# # 2. EXPLICIT TYPE CONVERSION
# # -----------------------------------------
# '''
# User explicitly converts data type using built-in functions.

# Built-in conversion functions:
# int(), float(), str(), bool(), complex()

# Mostly used with input() function.
# '''

# # input() example
# syntax=input()

# a = input("Enter a number: ")
# print(a)



# Convert input to float
# a = float(input("Enter number 1: "))
# b = float(input("Enter number 2: "))
# print(a + b)
# print(type(a))
# # -----------------------------------------
# # INT TYPE CONVERSION
# # -----------------------------------------
# '''
# int() converts other data types into integer.

# Python मध्ये int type conversion म्हणजे
# इतर data type ला integer मध्ये बदलणे.
# '''

# # Float → Int

# pi = 3.14345
# num = int(pi)

# print(num)       # decimal part removed
# print(type(num))



# # Boolean → Int


# flag_true = True
# flag_false = False

# print(int(flag_true))   
# print(int(flag_false))  


# # String → Int


# string_num = "225"
# num1 = int(string_num)

# print(num1)
# print(type(num1))


#
# # -----------------------------------------
# # FLOAT TYPE CONVERSION
# # -----------------------------------------
# '''
# float() converts values into floating-point numbers.
# '''

# Int → Float

# num = 7250
# num1 = float(num)

# print(num1)
# print(type(num1))


# # Boolean → Float


# print(float(True))    
# print(float(False))   


# # # String → Float
# string_num = "725"
# num2 = float(string_num)

# print(num2)
# print(type(num2))


# # -----------------------------------------
# # COMPLEX TYPE CONVERSION
# # -----------------------------------------
# '''
# Complex numbers are written as:
# a + bj

# a → real part
# b → imaginary part
# j → square root of -1
# '''

# # Int → Complex
# r_num = 135
# c_num = complex(r_num)

# print(c_num)
# print(type(c_num))

# # Two arguments
# c_num = complex(135, 235)
# print(c_num)

# # Float → Complex
# r_num = 530.25
# c_num = complex(r_num)
# print(c_num)

# # Boolean → Complex
# print(complex(True))     
# print(complex(False))    

# print(complex(False, True))   

# # -----------------------------------------
# # BOOLEAN TYPE CONVERSION
# # -----------------------------------------
# '''
# bool() converts value into True or False.

# Falsy values:
# 0, 0.0, "", [], (), {}, None





# Truthy values:
# Non-zero numbers, non-empty strings, collections
# '''

# # Int → Bool
# print(bool(2))
# print(bool(-5))

# # Float → Bool
# print(bool(25.35))
# print(bool(0))

# # String → Bool
# print(bool("False"))
# print(bool(""))
# print(bool("812"))

# # Complex → Bool
# print(bool(33 + 0j))
# print(bool(0j))

# # -----------------------------------------
# # STRING TYPE CONVERSION
# # -----------------------------------------
# '''
# str() converts any data type into string.
# '''

# # Int → String
# num = 15
# s1 = str(num)
# print(s1)
# print(type(s1))

# #Float → String
# num = 75.35
# s2 = str(num)
# print(s2)
# print(type(s2))

# # Complex → String
# complex_num = 15 + 5j
# s3 = str(complex_num)
# print(s3)
# print(type(s3))

# # Boolean → String
# print(str(True))
# b=False
# a=(str(b))
# print(a)
# print(type(a))


# '''
# ==============================
# END OF TYPE CONVERSION
# ==============================
# '''











