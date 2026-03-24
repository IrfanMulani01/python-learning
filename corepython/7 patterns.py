'''
====================================
PYTHON PATTERN PRINTING – COMPLETE
====================================

Steps to Print Patterns in Python
---------------------------------

1. Decide number of rows and columns
   - Every pattern is based on rows and columns.
   - We use nested loops:
     • Outer loop → rows
     • Inner loop → columns

2. Iterate rows
   - Use a for loop with range() for rows.

3. Iterate columns
   - Use a nested loop.
   - Number of columns depends on the row number.

4. Print symbols or numbers
   - Use print("*", end=" ") or print(number, end=" ")

5. New line after each row
   - Use print() after inner loop.
'''

# ------------------------------------
# BASIC STAR PRINT
# ------------------------------------

# print("*")

# n = 5
# print("*" * n)

# ------------------------------------
# SINGLE ROW STARS
# ------------------------------------

# n = 5
# for j in range(n):
#     print("*", end=" ")

# ------------------------------------
# SQUARE STAR PATTERN
# ------------------------------------
'''
* * * * *
* * * * *
* * * * *
* * * * *
* * * * *
'''

# n = 5
# for i in range(n):          # rows
#     for j in range(n):      # columns
#         print("*", end=" ")
#     print()

'''
Explanation:
- Outer loop runs for rows.
- Inner loop prints stars in each row.
- print() moves to the next line.
'''

# ------------------------------------
# LEFT SIDE RIGHT ANGLE TRIANGLE
# ------------------------------------
'''
*
* *
* * *
* * * *
* * * * *
'''

# n = 5
# for i in range(n):
#     for j in range(i + 1):
#         print("*", end=" ")
#     print()

'''
Explanation:
- Row number decides how many stars to print.
'''

# ------------------------------------
# REVERSE LEFT TRIANGLE
# ------------------------------------
'''
* * * * *
* * * *
* * *
* *
*
'''

# n = 5
# for i in range(n):
#     for j in range(i, n):
#         print("*", end=" ")
#     print()

# ------------------------------------
# RIGHT SIDE TRIANGLE
# ------------------------------------
'''
        *
      * *
    * * *
  * * * *
* * * * *
'''

# n = 5
# for i in range(n):
#     for j in range(i, n):
#         print(" ", end=" ")
#     for j in range(i + 1):
#         print("*", end=" ")
#     print()

'''
Explanation:
- First loop prints spaces.
- Second loop prints stars.
'''

# ------------------------------------
# REVERSE RIGHT TRIANGLE
# ------------------------------------
'''
* * * * *
  * * * *
    * * *
      * *
        *
'''

# n = 5
# for i in range(n):
#     for j in range(i + 1):
#         print(" ", end=" ")
#     for j in range(i, n):
#         print("*", end=" ")
#     print()

# ------------------------------------
# PYRAMID (HILL PATTERN)
# ------------------------------------
'''
        *
      * * *
    * * * * *
  * * * * * * *
* * * * * * * * *
'''

# n = 5
# for i in range(n):
#     for j in range(i, n):
#         print(" ", end=" ")
#     for j in range(i):
#         print("*", end=" ")
#     for j in range(i + 1):
#         print("*", end=" ")
#     print()

# ------------------------------------
# INVERTED PYRAMID
# ------------------------------------
'''
* * * * * * * * *
  * * * * * * *
    * * * * *
      * * *
        *
'''

# n = 5
# for i in range(n):
#     for j in range(i + 1):
#         print(" ", end=" ")
#     for j in range(i, n - 1):
#         print("*", end=" ")
#     for j in range(i, n):
#         print("*", end=" ")
#     print()

# ------------------------------------
# DIAMOND PATTERN
# ------------------------------------
'''
        *
      * * *
    * * * * *
  * * * * * * *
* * * * * * * * *
  * * * * * * *
    * * * * *
      * * *
        *
'''

# n = 5
# for i in range(n - 1):
#     for j in range(i, n):
#         print(" ", end=" ")
#     for j in range(i):
#         print("*", end=" ")
#     for j in range(i + 1):
#         print("*", end=" ")
#     print()

# for i in range(n):
#     for j in range(i + 1):
#         print(" ", end=" ")
#     for j in range(i, n - 1):
#         print("*", end=" ")
#     for j in range(i, n):
#         print("*", end=" ")
#     print()

'''
Explanation:
- First part prints upper pyramid.
- Second part prints inverted pyramid.
- Together they form a diamond shape.
'''

# ------------------------------------
# NUMBER PATTERNS
# ------------------------------------

'''
1
1 1
1 1 1
'''

# n = 5
# for i in range(n):
#     for j in range(i + 1):
#         print("1", end=" ")
#     print()

'''
1
2 2
3 3 3
'''

# n = 5
# p = 1
# for i in range(n):
#     for j in range(i + 1):
#         print(p, end=" ")
#     p += 1
#     print()

# ------------------------------------
# FLOYD’S TRIANGLE
# ------------------------------------
'''
1
2 3
4 5 6
7 8 9 10
'''

# n = 4
# p = 1
# for i in range(n):
#     for j in range(i + 1):
#         print(p, end=" ")
#         p += 1
#     print()

# ------------------------------------
# ALPHABET PATTERNS
# ------------------------------------

'''
A
A A
A A A
'''

# n = 4
# for i in range(n):
#     for j in range(i + 1):
#         print("A", end=" ")
#     print()

'''
A
B B
C C C
'''

# n = 5
# p = 65
# for i in range(n):
#     for j in range(i + 1):
#         print(chr(p), end=" ")
#     p += 1
#     print()

'''
A
B C
D E F
'''

# n = 5
# p = 65
# for i in range(n):
#     for j in range(i + 1):
#         print(chr(p), end=" ")
#         p += 1
#     print()

'''
====================================
END OF PATTERN PROGRAMS
====================================
'''

