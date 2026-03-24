# 1. Create a list of squares of numbers from 1 to 10.
# square = [i*i for i in range(1,11)]
# print(square)

# 2. Extract all even numbers from [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] using a list comprehension.
# even = [i for i in range(1,11) if i % 2 == 0]
# print(even)

# 3. Convert all strings in ["hello", "world", "python"] to uppercase.
# string = ["hello", "world", "python"]
# convert = [i.upper() for i in string]
# print(convert)

# 4. Create a list of lengths of each word in ["apple", "banana", "cherry"].
# strings = ["apple", "banana", "cherry"]
# length = [len(i) for i in strings]
# print(length)

# 5. Flatten this nested list using a list comprehension:
# lst = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# nested = [i for row in lst for i in row]
# print(nested)

# 6. Create a dictionary mapping each word to its length from ["cat", "elephant", "dog"].
# lst1 = ["cat", "elephant", "dog"]
# dic = {i: len(i) for i in lst1}
# print(dic)

# 7. Using a set comprehension, find all unique vowels in the string "comprehension practice".
# string = "comprehension practice"
# wovels = {i for i in string if i in 'aeiou'}
# print(wovels)

# 8. Filter out words shorter than 4 characters from ["hi", "hello", "hey", "howdy", "yo"].
# lst2 = ["hi", "hello", "hey", "howdy", "yo"]
# short = [char for char in lst2 if len(char) >= 4]
# print(short)

# 9. Create a list of (x, y) pairs where x is from [1,2,3] and y is from [4,5,6] — but only when x != y.
# prt = [(x,y) for x in [1,2,3] for y in [4,5,6] if x != y]
# print(prt)

# 10. Using a dictionary comprehension, invert this dictionary (swap keys and values):
# dic = {"a": 1, "b": 2, "c": 3}
# d = {v:k for k, v in dic.items()}
# print(d)

# 11. Create a list of all prime numbers between 2 and 50 using a list comprehension.
# prime = [x for x in range(1,21) if all(x % i != 0 for i in range(2,x))]
# print(prime)

# 12. Given a list of sentences, extract all words that start with a vowel:
# sentences = ["an apple a day", "every good deed", "open the door"]
# extract = [i for sentence in sentences for i in sentence if i[0] in 'aeiou']
# print(extract)



