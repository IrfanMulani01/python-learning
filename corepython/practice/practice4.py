# Write a program to check whether a number entered by user is even or odd.
# num = int(input("Enter Number: "))
# if num % 2 == 0:
#     print(f"{num} is Even NUmber")
# else:
#     print(f"{num} is odd Number")

# # 1. Write a Python program to sum all the items in a list. 
lst = [1,4,2,1,3,2,5,6,3]
# print(sum(list))

# 2. Write a Python program to multiply all the items in a list. 
# total = 1
# for i in list:
#     total *= i
# print(total)

# 3. Write a Python program to get the largest number from a list. 
# large = list[0]
# for i in list:
#     if i>large:
#         large = i
# print(large)

# 4. Write a Python program to get the smallest number from a list.
# small = list[0]
# for i in list:
#     if i<small:
#         small = i
# print(small)

# 5. Write a Python program to count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings. 
# string = 'abc', 'xyz', 'aba', '1221'
# for i in string:
#     if i in string:
#         i <= 2
# print(i)

# 7. Write a Python program to remove duplicates from a list. 
# print(list(set(lst)))

# 8. Write a Python program to check a list is empty or not. 
# lst1 = []
# empty = 0
# if len(lst1) == empty:
#     print("list is empty")
# else:
#     print("list is full")

# 9. Write a Python program to clone or copy a list.
# list1 = lst.copy()
# print(list1)

# 10. Write a Python program to find the list of words that are longer than n from a given list of words. 
# words = ["apple", "cat", "banana", "dog", "elephant"]
# n = 4
# result = []
# for i in words:
#     if len(i) > n:
#         result.append(i)
# print(result)

# 11. Write a Python function that takes two lists and returns True if they have at least one common member.
# def check_List(lst1, lst2):
#     for i in lst1:
#         if i in lst2:
#             return True
#         else:
#             return False
lst1 = [1, 2,3,4,5,6,7,8]
# lst2 = [1,11,12,13,31,41,51,5]
# print(check_List(lst1,lst2))

# 12. Write a Python program to print a specified list after removing the 0th, 4th and 5th elements. 
# list1 = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
# result = [X for i, X in enumerate(list1) if i not in (0,4,5)]
# print(result)

# 14. Write a Python program to print the numbers of a specified list after removing even numbers from it. 
lst2 = [1,11,12,22,34,41,51,5]
# result = {n for n in lst2 if n % 2 != 0}
# print(result)

# 15. Write a Python program to shuffle and print a specified list.
import random
# random.shuffle(lst2)
# print(lst2)
