# LIST:- 

# li1 = ['gif', '1', '2']
# # li1.append('10')  #add element on the end of the list
# # li1.insert(1, 'ind')  #add or replace element with the help of index in list
# # li1.remove('1') #deleting the element from list using list data
# # li1.pop(2)    #removing element and returning index
# # li1.sort()  #sorting element in acsending order
# # li1.reverse()   #reversing elements in list
# print(li1)

# STRING:- 

name = str('Irfan Ganesh rohit')
# print(name.upper())
# print(name.lower())
# print(name.strip('rohit'))    #removing the element with help of data
# print(name.find('Irfan')) #returning index
# print(name.replace('Ganesh',"madan")) #replacing element
# print(name.split()) #dividing string with lep of comma(',') and return into list

#DICTIONARY:-

# name = {'name': 'irfan', 'age': 20}
# print(name.get('name'))   # accesing values with the help of key
# print(name.pop('age'))  # returnnig value using key
# print(name.keys()) # retuning key of dictionry
# print(name.values())    # returnnig values of dictionary
# print(name.items())     # returnnig all dictionry

# Write a program to convert a string to uppercase and lowercase.
# name = str('Irfan Ganesh rohit')
# print(name.upper())
# print(name.lower())

# Write a program to replace a word in a string.
# name = str('Irfan Ganesh rohit')
# print(name.replace('Ganesh', 'madan'))

# Write a program to count the number of characters in a string.
# name = str('Irfan Ganesh rohit')
# print(len(name))

# Write a program to reverse a string.
# name = str('Irfan Ganesh rohit')
# print(name[::-1])

#Write a program to check if a string is a palindrome.
# string = str("madam")
# if string == string[::-1]:
#     print("string palindrom")
# else :
#     print("not palindrom")

#Write a program to split a string into a list of words.
# name = 'Irfan Ganesh rohit'
# print(name.split(" "))

#Write a program to remove whitespace from the beginning and end of a string.
# name = '    Irfan Ganesh rohit'
# print(name.lstrip())

#Write a program to count the occurrences of a character in a string.
# name = "Irfan Ganesh 'manoj' rohit"
# print(name.count('a'))


# LIST:-

# Write a program to add and remove elements from a list.
# li = [1, 2, 3, 9,4,7,6,5, 10, 11]
# print(li.insert(5,'5'))
# # print(li.remove(2))

#Write a program to sort a list in ascending and descending order.
# li = [1, 2, 3, 9,4,7,6,5, 10, 11]
# li.sort(reverse=True)
# print(li)

# Write a program to reverse a list.
li = [1, 2, 3, 9,4,7,6,6,5, 10, 11]
# print(li[::-1])

# Write a program to remove duplicates from a list.
# li1 = set(li)
# print(li1)

# Write a program to merge two lists.
# li1 = ["irfan", "soham"]
# print(li + li1)

# Write a program to slice a list.
# print(slice(li[4:8]))

# # Write a program to count the occurrences of an element in a list.
# print(li.count(6))


# TUPLE:-

# Write a program to create a tuple and access its elements.
tup = (1, 2,0,0,0,0,3,4,5,6,7,8,9,0,1,12,14,15,161,611)
# print(tuple)

# # Write a program to find the length of a tuple.
# print(len(tuple))

# Write a program to count occurrences of an element in a tuple
# print(tuple.count(0))

# Write a program to find the index of an element in a tuple.
# print(tuple.index(0))

# Write a program to convert a tuple to a list and a list to a tuple.
# print(list(tup))
# print(tuple(li))

# Write a program to unpack a tuple into variables.
tup1 = ("apple", "pinapple", "cherry")
# (green, yellow, red) = tup1
# print(green)
# print(yellow)
# print(red)

# Write a program to concatenate two tuples.
# print(tup + tup1)

# Write a program to find the maximum and minimum value in a tuple.
# print(min(tup))
# print(max(tup))

# Write a program to slice a tuple.
# print(slice(tup[6]))


# DICTIONARY:-

# Write a program to create a dictionary and access its values.
dic = {1 : 'a', 2: 'b', 3: 'c'}
# print(dic.values())

# Write a program to add and update key-value pairs in a dictionary
# dic.update({4:'d'})
# print(dic)

# Write a program to delete a key from a dictionary.
# print(dic.pop(3))

# Write a program to check if a key exists in a dictionary.
# key = 4
# print(key in dic)

# Write a program to merge two dictionaries.
# dic1 = {4:'d', 5:'e', 6:'f'}
# dic.update(dic1)
# print("dicTionary: ", dic)

# Write a program to find the length of a dictionary.
# print(len(dic))

# Write a program to sort a dictionary by keys and values.
# for k, v in sorted(dic.items(), key=lambda item: item[1]):
#     print((k, v), end=" ")

# Write a program to count the frequency of each character in a string using a dictionary.
# freq = {c: name.count(c) for c in name}
# print(freq)

# COMBINE:-

# Write a program to convert a string to a list of characters.
# print(str(li))
# print(list(name))

# freq = {c: name.count(c) for c in name}
# print(freq)

# Write a program to store student names and marks in a dictionary and find the topper.
# n = int(input("Enter How Many Student Insert: "))
# data = {}

# for i in range(n):
#     stud_name = input(f"enter Name of the Student: ")
#     stud_marks = int(input(f"enter Marks of Student {stud_name}: "))
#     data[stud_name] = stud_marks
#     print("Student Info: ", data)
    
# topper = max(data, key=lambda x: data[x])
    
# print("topper",topper)


## set's additional methods:
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
# print(a | b)  # it returns combine of two sets
# print(a-b)    # it returns which element is in set1 and not in set2
# print(a^b)  # it returns not common in two sets
# print(a&b)  # it returns duplicate in two sets

## Write a Python program to count the number of sublists contain a particular element. 
		# Original list:
# lst = [[1, 3], [5, 7], [1, 11], [1, 15, 7]]
# element = int(input("Enter element to find: "))
# usp = len(list(filter(lambda sublist: element in sublist, lst)))
# print(usp)

## Write a Python program to sort each sublist of strings in a given list of lists. 
	# Original list:
lst = [[2], [0], [1, 3], [0, 7], [9, 11], [13, 15, 17]]
# print(sorted(lst))

## Write a Python program to sort a given list of lists by length and value. 
	# Original list:
	# [[2], [0], [1, 3], [0, 7], [9, 11], [13, 15, 17]]
print(sorted(lst, key=lambda x: (len(x), x)))
