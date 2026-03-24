'''
====================================
PYTHON RECURSION – ALL IN ONE
====================================

What is Recursion?
------------------
Recursion is a programming technique where a function calls itself
to solve a problem by breaking it into smaller sub-problems.

A recursive function must always contain:
1. Base Case       → stops recursion
2. Recursive Case → function calls itself

Without a base case, recursion will run infinitely
and cause a RecursionError.

------------------------------------
RECURSION LIMIT
------------------------------------
• Python allows a maximum recursion depth of 1000
• Exceeding this limit raises:
  RecursionError: maximum recursion depth exceeded
'''

# ------------------------------------
# BASIC RECURSIVE STRUCTURE
# ------------------------------------
'''
def recursive_function(parameters):

    if base_condition:
        return result        # Base Case

    else:
        return recursive_function(smaller_input)  # Recursive Case
'''

# ------------------------------------
# EXAMPLE 1: FACTORIAL USING RECURSION
# ------------------------------------
'''
Factorial:
----------
n! = n × (n-1) × (n-2) × ... × 1

Example:
5! = 5 × 4 × 3 × 2 × 1 = 120
'''

# def factorial(n):
#     if n == 0:                 # Base Case
#         return 1
#     else:
#         return n * factorial(n - 1)  # Recursive Case

# print(factorial(5))

'''
Execution Flow:
---------------
factorial(5)
→ 5 * factorial(4)
→ 4 * factorial(3)
→ 3 * factorial(2)
→ 2 * factorial(1)
→ 1 * factorial(0)
→ 1 (Base Case)

Final Result = 120
'''

# ------------------------------------
# EXAMPLE 2: PRINT NUMBERS (1 TO N)
# ------------------------------------

# def print_numbers(n):
#     if n == 0:          # Base Case
#         return
#     print_numbers(n - 1)
#     print(n)

# print_numbers(5)

'''
Output:
-------
1
2
3
4
5
'''

# ------------------------------------
# EXAMPLE 3: SUM OF FIRST N NUMBERS
# ------------------------------------

# def sum_numbers(n):
#     if n == 0:          # Base Case
#         return 0
#     return n + sum_numbers(n - 1)

# print(sum_numbers(5))

'''
Calculation:
------------
5 + 4 + 3 + 2 + 1 = 15
'''

# ------------------------------------
# EXAMPLE 4: REVERSE STRING
# ------------------------------------

# def reverse_string(s):
#     if len(s) <= 1:     # Base Case
#         return s
#     return s[-1] + reverse_string(s[:-1])

# print(reverse_string("hello"))

'''
Execution:
----------
"hello"
→ o + reverse("hell")
→ l + reverse("hel")
→ l + reverse("he")
→ e + reverse("h")
→ h (Base Case)

Output: olleh
'''

# ------------------------------------
# EXAMPLE 5: FIBONACCI USING RECURSION
# ------------------------------------
'''
Fibonacci Rule:
---------------
F(n) = F(n-1) + F(n-2)

Base Cases:
-----------
F(0) = 0
F(1) = 1
'''

# def fibonacci(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fibonacci(n - 1) + fibonacci(n - 2)

# print(fibonacci(10))

'''
Fibonacci Values:
-----------------
0 → 0
1 → 1
2 → 1
3 → 2
4 → 3
5 → 5
6 → 8
7 → 13
8 → 21
9 → 34
10 → 55
'''

# ------------------------------------
# ADVANTAGES OF RECURSION
# ------------------------------------
'''
• Code becomes clean and readable
• Useful for problems like:
  - Tree traversal
  - Divide and conquer
  - Mathematical problems
'''

# ------------------------------------
# DISADVANTAGES OF RECURSION
# ------------------------------------
'''
• Slower than loops
• Uses more memory
• Risk of stack overflow
• Base case is mandatory
'''

'''
====================================
END OF PYTHON RECURSION
====================================
'''
