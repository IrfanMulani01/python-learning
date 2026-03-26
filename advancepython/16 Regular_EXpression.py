"""
========================================
REGULAR EXPRESSIONS (REGEX) IN PYTHON
========================================

Definition:
-----------
A Regular Expression (Regex) is a sequence of
characters used to search, match, and manipulate
text patterns.

Python provides the `re` module for working
with regular expressions.
"""

# ==================================================
# WHY REGEX IS IMPORTANT
# ==================================================

"""
✔ Data validation
✔ Text searching
✔ Pattern matching
✔ Used in log analysis, scraping, validation
"""
# Regex is mainly used to check formats like email, phone number, etc.

# ==================================================
# IMPORT re MODULE
# ==================================================

import re
# Imports regex module so that regex functions can be used.

# ==================================================
# BASIC REGEX FUNCTIONS
# ==================================================

"""
re.match()   → Match at beginning
re.search()  → Search anywhere
re.findall() → Find all matches
re.sub()     → Replace text
"""
# These functions help in finding, matching, and replacing text.

# ==================================================
# re.match() EXAMPLE
# ==================================================

# text = "Python Programming"
# result = re.match("Python", text)
# print(result)


'''re.match() checks only from the starting of the string
Since "Python" is at the beginning, it will match.
'''
# ==================================================
# re.search() EXAMPLE
# ==================================================

# text = "Learning Python is easy"
# result = re.search("easy", text)
# print(result.group())



''' re.search() --> searches the word anywhere in the string
 group() --> returns the matched word.
'''
# ==================================================
# re.findall() EXAMPLE
# ==================================================

# text = "Python Java Python C"
# result = re.findall("Python", text)
# print(result)
#             
''' re.findall()  returns all matches as a list.'''


# ==================================================
# re.sub() EXAMPLE
# ==================================================

# text = "I love Java"
# result = re.sub("Java", "Python", text)
# print(result)
 
'''      re.sub() -->      replaces "Java" with "Python" in the string'''

# ==================================================
# PROGRAM LOGIC
# ==================================================

"""
1. Import re module
2. Define pattern
3. Apply regex function
4. Get matched result
"""
# These steps are followed in all regex-based programs.

# ==================================================
# REGEX METACHARACTERS
# ==================================================

"""
.     → Any character
^     → Start of string
$     → End of string
*     → Zero or more
+     → One or more
?     → Zero or one
[]    → Character set
{}    → Exact count
|     → OR
"""
# Metacharacters give special meaning to regex patterns.

# ==================================================
# CHARACTER CLASSES
# ==================================================

"""
\d  → Digit (0-9)
\D  → Non-digit
\w  → Letters, digits, underscore
\W  → Non-word characters
\s  → Space
\S  → Non-space
"""
# Character classes are shortcuts used in patterns.

# ==================================================
# VALIDATING EMAIL (EXAMPLE)
# ==================================================

'''
This Python code checks whether an email address is valid using
regular expressions (regex).

If the email matches a certain pattern → Valid Email
Otherwise → Invalid Email
'''
# This block explains the purpose of email validation.

# email = "test123@gmail.com"
# # Email value to be checked.

# pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"

# # # '''^       → start of string
# # # [\w.-]+ → username part
# # # @       → must contain @ symbol
# # # [\w.-]+ → domain name
# # # \.      → dot (.)
# # # \w+     → domain extension like com
# # # $       → end of string'''

# if re.match(pattern, email):
# # #     # Checks whether the email matches the pattern from the beginning.
#     print("Valid Email")
# else:
# #     # Executes if email does not follow the pattern.
#     print("Invalid Email")

# ==================================================
# VALIDATING MOBILE NUMBER
# ==================================================

mobile = "5765432101"
pattern = r"^[6-9]\d{9}$"
# '''^      → start
# [6-9]  → first digit must be between 6 and 9
# \d{9}  → remaining 9 digits
# $ → end'''     

# if re.match(pattern, mobile):
#     print("Valid Mobile Number")
# else:
#     print("Invalid Mobile Number")

# ==================================================
# SPLITTING STRING USING REGEX
# ==================================================

# text = "apple,orange;banana|grapes"
# result = re.split("[,;|]", text)
# print(result)
                  
# 
# 
'''splits string using comma, semicolon, or | symbol.
Output will be a list of fruits.'''

# ==================================================
# IMPORTANT POINTS
# ==================================================

"""
✔ Regex is case-sensitive by default
✔ Use raw strings (r"pattern")
✔ Complex but powerful
✔ Very useful for validation
"""
# These are important rules to remember.

# ==================================================
# QUICK SUMMARY (EXAM READY)
# ==================================================

"""
Regex:
------
Used for pattern matching
Handled using re module
"""
