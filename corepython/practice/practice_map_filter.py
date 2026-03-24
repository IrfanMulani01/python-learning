# Use map() to convert a list of strings ["1", "2", "3", "4"] into a list of integers
# strings = ["1", "2", "3", "4"]
# lst = list(map(int, strings))
# print(lst)

# Use filter() to remove all negative numbers from [-3, -1, 0, 2, 5, -7, 8].
# lst = [-3, -1, 0, 2, 5, -7, 8]
# remove = list(filter(lambda i : i > 0, lst))
# print(remove)

# Use map() to square every number in [1, 2, 3, 4, 5].
# lst1 = [1, 2, 3, 4, 5]
# square = list(map(lambda i : i * i, lst1))
# print(square)

# Use filter() to keep only even numbers from [1, 2, 3, 4, 5, 6, 7, 8].
# lst = [1, 2, 3, 4, 5, 6, 7, 8]
# even = list(filter(lambda i : i % 2 == 0, lst))
# print(even)

# Use map() to convert a list of temperatures in Celsius [0, 20, 37, 100] to Fahrenheit. (Formula: F = C × 9/5 + 32)
# temp = [0, 20, 37, 100]
# fahren = list(map(lambda i : i * 9 / 5 +32, temp))
# print(fahren)

# Use filter() to extract all words longer than 4 characters from ["apple", "cat", "banana", "dog", "mango"].
# string = ["apple", "cat", "banana", "dog", "mango"]
# lessword = list(filter(lambda i : len(i) < 4, string))
# print(lessword)

# Use map() with a lambda to capitalize every word in ["hello", "world", "python"].
# string = ["apple", "cat", "banana", "dog", "mango"]
# cap = list(map(lambda i : i.upper(), string))
# print(cap)

# Combine map() and filter() to: first filter out odd numbers from [1–10], then square the remaining even numbers.
# def even(i):
#     return i % 2 == 0
# def square(i):
#     return i * i
# num = list(range(1,11))
# combo = list(map(square, filter(even, num)))
# print(combo)

# Use filter() to find all numbers divisible by both 3 and 5 from a list of numbers 1 to 50.
# def check(i):
#     if i % 3 == 0 and i % 5 == 0:
#         return i
# num = list(range(1,50))
# divi = list(filter(check, num))
# print(divi)

# You have a list of dictionaries representing students:
students = [
        {"name": "Alice", "grade": 85},
        {"name": "Bob", "grade": 42},
        {"name": "Charlie", "grade": 91},
        {"name": "Diana", "grade": 58},
    ]
# Use `filter()` to get students who passed (grade ≥ 60), then use `map()` to extract just their names.
# def grade(i):
#     return i["grade"] >= 60
# def names(i):
#     return i["name"]
# passed = list(map(names, filter(grade, students)))
# print(passed)

# 11. Use map() to apply a function that returns "even" or "odd" for each number in [1, 2, 3, 4, 5, 6].
# num = [1, 2, 3, 4, 5, 6]
# enveodd = list(map(lambda i : (i,"even" if i%2 == 0 else "odd"), num))
# print(enveodd)

# 12. Given two lists [1, 2, 3] and [4, 5, 6], use map() to produce their element-wise sum [5, 7, 9].
# def add(i,j):
#     return i + j
# lst1 = [1,2,3]
# lst2 = [4,5,6]
# elementwize = list(map(add, lst1, lst2))
# print(elementwize)

# 13. Use filter() with a custom function (not a lambda) to keep only palindromes from ["racecar", "hello", "level", "world", "madam"].
# def rev(word):
#     return word == word[::-1]
# string = ["racecar", "hello", "level", "world", "madam"]
# reverse = list(filter(rev, string))
# print(reverse)

