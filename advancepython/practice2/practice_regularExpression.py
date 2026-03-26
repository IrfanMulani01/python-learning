## Q1. Write a program using re.search() to check if the word "Python" exists in a given string. Print "Found!" or "Not Found!".
import re
# string = "python is simple language"
# result = re.match("python", string)
# print(result)

# ## Q2. Write a program using re.match() to check if a string starts with "Hello". Test with:
# "Hello World" → Match
# "World Hello" → No Match
# string = "hello World"
# result = re.match("hello", string)
# print(result)

# ## Q3. Write a program using re.findall() to extract all numbers from the string:
# "I have 2 cats, 3 dogs and 10 fish"
# string = "I have 2 cats, 3 dogs and 10 fish"
# result = re.findall(r'\d+', string)
# print(result)

# ## Q4. Write a program using re.sub() to replace all spaces in a string with underscores _.
# Input:  "Hello World Python"
# Output: "Hello_World_Python"
# string = "Hello World Python"
# result = re.sub(r'\s', '_', string)
# print(result)

# ## Q5. Write a program using re.split() to split a string by comma, space, or semicolon:
# Input:  "apple, banana; mango orange"
# Output: ['apple', 'banana', 'mango', 'orange']
# string = "apple, banana; mango orange"
# result = re.split(r'[,;\s]+', string)
# print(result)

# ## Q6. Write a program to validate an email address using regex. Check if it follows the pattern name@domain.com:
# "test@gmail.com" → Valid
# "testgmail.com" → Invalid
# "test@gmailcom" → Invalid
# email = "irfanmulani01@gmail.com"
# pattern = r'^[\w\.-]+@[\w\.-]+\w+$'
# if re.match(pattern, email):
#     print("valid Email")
# else:
#     print("Invalid Email")

# ## Q7. Write a program to validate a mobile number:
# Must be exactly 10 digits
# Must start with 6, 7, 8, or 9
# "9876543210" → Valid
# "1234567890" → Invalid
# mo_no = "8530904366"
# pattern = r'^[6-9]\d{9}$'
# if re.match(pattern, mo_no):
#     print("valid mobile number")
# else:
#     print("invalid mobile number")

## Q8. Write a program using re.findall() to extract all words that start with a capital letter from a paragraph.
# paragraph = "Alice and Bob went to Paris. They visited the Eiffel Tower and Louvre Museum."
# result= re.findall(r'\b[A-Z][a-z]*\b', paragraph)
# print(result)

## Q11. Write a program using groups () in regex to extract the name, domain, and extension separately from an email:
# Input:  "user@gmail.com"
# Output: Name=user  Domain=gmail  Ext=com
# email = "irfanmulani01@gmail.com"
# result = re.match(r'(\w+)@(\w+)\.(\w+)', email)
# if result:
#     print(f"full match : {result.group(0)}")
#     print(f"name : {result.group(1)}")
#     print(f"domain : {result.group(2)}")
#     print(f"extension : {result.group(3)}")

# ## Q13. Write a program to validate an IP address using regex:
# Must follow 0-255.0-255.0-255.0-255
# "192.168.1.1" → Valid
# "999.168.1.1" → Invalid

# ip = "198.221.0.1"

# pattern = r'^((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)\.){3}(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)$'

# if re.match(pattern, ip):
#     print("Valid IP address")
# else:
#     print("invalid ip address")


# ## Q16. Create a class Validator with static methods using regex:
# validate_email(email) — checks valid email
# validate_phone(number) — checks valid 10-digit number
# validate_password(pwd) — checks strong password
# class validator:
    
#     def __init__(self, email, mobile, password):
#         self.email    = email
#         self.mobile   = mobile
#         self.password = password

#         self.validate_email(email)
#         self.validate_phone(mobile)
#         self.validate_password(password)        
    
#     @staticmethod
#     def validate_email(email):
#         pattern = r'^[\w.-]+@[\w.-]+\.\w{2,4}$'
#         if re.match(pattern, email):
#             print(f"Email    : {email} → Valid ✅")
#         else:
#             print(f"Email    : {email} → Invalid ❌")

    
#     @staticmethod
#     def validate_phone(mobile):
#         pattern = r'^\d{10}$'
#         if re.match(pattern, mobile):
#             print(f"Mobile   : {mobile} → Valid ✅")
#         else:
#             print(f"Mobile   : {mobile} → Invalid ❌")
    
#     @staticmethod
#     def validate_password(password):
#         pattern = r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@#$%^&+=]).{8,}$'
#         if re.match(pattern, password):
#             print(f"Password : {password} → Valid ✅")
#         else:
#             print(f"Password : {password} → Invalid ❌")

# va = validator("irfanmlani01@gmail.com","8530904366","Irfan@123")

##💡 Mini Project
# Q18. Build a Form Validator using a class FormValidator that validates a user registration form:
# pythondata = {
#     "name": "Rohit Sharma",
#     "email": "rohit@gmail.com",
#     "phone": "9876543210",
#     "password": "Rohit@123",
#     "dob": "15-08-1995"
# }
# Validate each field using regex:
# name — only alphabets and spaces
# email — valid email format
# phone — 10 digit starting with 6–9
# password — strong password rules
# dob — format DD-MM-YYYY
# Print "Valid" or "Invalid" with reason for each field.

# class FormValidator:
#     def __init__(self,name,email,phone,password,dob):
#         self.name = name
#         self.email = email
#         self.phone = phone
#         self.password = password
#         self.dob = dob
        
#         self.validate_name(name)
#         self.validate_email(email)
#         self.validate_phone(phone)
#         self.validate_password(password)
#         self.validate_dob(dob)
        
#     def validate_name(self,name):
#         pattern = r'^[A-Za-z]+\s[A-Za-z]+$'
#         if re.match(pattern, name):
#             print("valid name")
#         else:
#             print("invalid name")
    
#     def validate_email(self, email):
#         pattern = r'^[\w\.]+@[\w\.]+\.[\w]+$'
#         if re.match(pattern, email):
#             print("valid email")
#         else:
#             print("invalid email")
            
#     def validate_phone(self, phone):
#         pattern = r'^\d{10}'
#         if re.match(pattern, phone):
#             print("valid phone")
#         else:
#             print("invalid phone")
            
#     def validate_password(self, password):
#         pattern = r'^(?=.*[A-z])(?=.*[a-z])(?=.*\d)(?=.*[@$%&*^#+-~]).{8,}$'
#         if re.match(pattern, password):
#             print("valid password")
#         else:
#             print("invalid password")
            
#     def validate_dob(self, dob):
#         pattern = r'^(0[1-9]|[12][0-9]|3[01])-(0[1-9]|1[0-2])-\d{4}'
#         if re.match(pattern, dob):
#             print("valid date of birth")
#         else:
#             print("invalid date of birth")
            
# fv = FormValidator("Rohit Sharma","rohit@gmail.com","9876543210","Rohit@123","15-08-1995")