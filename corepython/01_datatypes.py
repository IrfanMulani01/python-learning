'''
Data Types:-Variables can hold values and every value has a data-type.
type()<-function-which returns the type of variable passed.

  himanshi=24
  print(type(himanshi))
  
Types of Data Types:
1.Mutable Data Types:-Object can change its state and content(modify after creation)
-List
-Dictionary
-set

2.Immuatble Data Types:-Object can't change.
-Integer
-Float
-Complex
-String
-tuple
'''

'''Integer'''
''' whole number'''




# a = 20 
# print(a)    
# print(type(a))

'''String'''

# b = "10"
# print(b)      
# print(type(b))

'''Float'''
'''represents decimal numbers'''
# c = 3.14
# print(c)
# print(type(c))                 

# d = 2.34444
# print(d)
# print(type(d))

'''Complex''' 
# represents numbers with a real and imaginary  

# e =1+0j
# print(e)
# print(type(e))

# z=23+4j
# print(type(z))
# print(z)


'''List'''

# f = ["orange", "yellow", "green"]      
# print(f)           
# print(type(f))

'''Tuple'''

# g = ("orange", "yellow", "green")
# print(g)
# print(type(g))

'''Set'''

# h = {"orange", "yellow", "green"}
# print(h)
# print(type(h))

'''Dictionary'''

# i = {"name" :"Reshma", "gender" : "female"}
# print(i)
# print(type(i))

'''Range'''

# j = range(10)
# print(j)
# print(type(j))

'''Boolean'''

# k = False
# print(k)
# print(type(k))


# '''String:String is the sequence of characters represents ' '' ''',
# '''immutable,duplicates allowed,ordered collection'''



  

#  capitalize() Method in Python Strings--->>

''' What is capitalize()? 

 The capitalize() method converts the first character of a string to uppercase
    and makes all other characters lowercase.
 It only affects the first letter and does not modify numbers or special characters.
 '''

'''Syntax 
string.capitalize()'''

# Example

# a = "expliciT"
# print(a.capitalize()) 

'''<<<------------------------------------------------------------------------------------------------------------------------------------------------------>>>'''

# casefold() Method in Python Strings--->>

'''What is casefold()?

 The casefold() method converts all characters in a string to lowercase,
   similar to lower(), but with better handling for special characters.
 It is more aggressive than lower(), meaning it converts certain special
   letters (like German ß) into their lowercase equivalents ("ss").
'''

''' Syntax
string.casefold()'''

# a="Aaduß"
# print(a.casefold())



# Example

# b = "ImpliciT"
# print(b.casefold())

'''<<<-------------------------------------------------------------------------------------------------------------------------------------------------------------->>>'''

# upper() Method in Python Strings--->>

'''What is upper()? 

The upper() method converts all lowercase letters in a string to uppercase (capital letters).
 It does not affect numbers, special characters, or already uppercase letters.
'''

'''Syntax 
string.upper()'''

#  Example

# b = "Implicit"
# print(b.upper())
'''<<<------------------------------------------------------------------------------------------------------------------------------------------------------->>>'''

# lower() Method in Python Strings

'''✅ What is lower()? (lower() म्हणजे काय?--->>

👉 The lower() method converts all uppercase letters in a string to lowercase (small letters).
👉 It does not affect numbers, special characters, or already lowercase letters.
👉 lower() फंक्शन संपूर्ण स्ट्रिंगमधील मोठी (uppercase) अक्षरे लहान (lowercase) अक्षरांमध्ये बदलते.
👉 संख्या, विशेष चिन्हे किंवा आधीच लहान अक्षरे बदलत नाहीत.'''

'''🔹 Syntax (सिंटॅक्स)
string.lower()'''

# ✅ Example

# c = "NESTEDß"
# print(c.lower())

'''<<<------------------------------------------------------------------------------------------------------------------------------------------------------------------>>>'''

#🔹 isupper() Method in Python Strings

'''✅ What is isupper()? (isupper() म्हणजे काय?--->>

👉 The isupper() method checks whether all letters in a string are uppercase.
👉 If all alphabetic characters are uppercase, it returns True; otherwise, it returns False.
👉 Numbers and special characters do not affect the result.
👉 isupper() फंक्शन तपासते की स्ट्रिंगमधील सर्व अक्षरे मोठी (uppercase) आहेत का.
👉 जर सर्व अक्षरे मोठी असतील तर True परत करते, अन्यथा False देते.
👉 संख्या आणि विशेष चिन्हांचा परिणाम होत नाही.'''

'''🔹 Syntax (सिंटॅक्स)
string.isupper()'''

# ✅ Example

# c = "NESTED"
# print(c.isupper())

# d="arJun"
# print(d.isupper())

'''<<<-------------------------------------------------------------------------------------------------------------------------------------------------------------------------->>>'''

# 🔹 islower() Method in Python Strings

'''✅ What is islower()? (islower() म्हणजे काय?--->>

👉 The islower() method checks whether all letters in a string are lowercase.
👉 If all alphabetic characters are lowercase, it returns True; otherwise, it returns False.
👉 Numbers and special characters do not affect the result.
👉 islower() फंक्शन तपासते की स्ट्रिंगमधील सर्व अक्षरे लहान (lowercase) आहेत का.
👉 जर सर्व अक्षरे लहान असतील तर True परत करते, अन्यथा False देते.
👉 संख्या आणि विशेष चिन्हांचा परिणाम होत नाही.'''

'''🔹 Syntax (सिंटॅक्स)
string.islower()'''

# ✅ Example 

# a = "explicit"
# print(a.islower())

# b="RaJU"
# print(b.islower())
'''<<<------------------------------------------------------------------------------------------------------------------------------------------------------------------------------>>>'''

# 🔹 isnumeric() Method in Python Strings

'''✅ What is isnumeric()? (isnumeric() म्हणजे काय?--->>

👉 The isnumeric() method checks whether a string consists only of numeric characters (digits).
👉 If all characters in the string are numbers (0-9 or other numeric characters like "²", "¾", etc.), 
it returns True. Otherwise, it returns False.
👉 isnumeric() फंक्शन तपासते की स्ट्रिंगमध्ये फक्त अंक (0-9 किंवा इतर संख्यात्मक चिन्हे) आहेत का.
👉 जर सर्व अक्षरे संख्यात्मक असतील तर True परत करते, अन्यथा False.'''

'''🔹 Syntax (सिंटॅक्स)
string.isnumeric()'''

'''✅ Example 1: Basic Usage of isnumeric()'''
# d = "5"
# print(d.isnumeric())
# print(type(d))

# c="python12"
# print(c.isnumeric())

'''<<<<------------------------------------------------------------------------------------------------------------------------------------------------------------------->>>'''

# 🔹 count() Method in Python Strings

'''✅ What is count()? (count() म्हणजे काय?--->>

👉 The count() method returns the number of times a specified substring appears in a given string.
👉 It can also work within a specific start and end position in the string.
👉 count() फंक्शन दिलेल्या स्ट्रिंगमध्ये एखादा विशिष्ट शब्द किंवा अक्षर किती वेळा आहे हे मोजते.
👉 तुम्ही start आणि end इंडेक्स वापरून शोधाची श्रेणी मर्यादित करू शकता.'''

'''🔹 Syntax (सिंटॅक्स)
string.count(substring, start, end)'''

'''✅ Example 1: Counting a Word in a String'''

# e = "---Ranjana---"
# print(e.count('a'))

'''<<<<<-------------------------------------------------------------------------------------------------------------------------------------------------------------------->>>'''


# 🔹 rstrip() Method in Python Strings

'''✅ What is rstrip()? (rstrip() म्हणजे काय?)
👉 The rstrip() method removes trailing whitespace or specified characters from the 
right side of a string.
👉 It does not modify the original string; instead, it returns a new string.
👉 rstrip() फंक्शन दिलेल्या स्ट्रिंगच्या शेवटी असलेली रिकामी जागा (whitespace) किंवा विशिष्ट अक्षरे काढून टाकते.
👉 मूळ स्ट्रिंग बदलत नाही, तर नवीन स्ट्रिंग परत करते.'''

'''🔹 Syntax (सिंटॅक्स)
string.rstrip(chars)'''

# ✅ Example

# e = "---Ranjana---"
# print("hi!",e.rstrip('-'),"come here")

'''<<<---------------------------------------------------------------------------------------------------------------------------------------------------->>>'''
# 🔹 lstrip() Method in Python Strings

'''✅ What is lstrip()? (lstrip() म्हणजे काय?)
👉 The lstrip() method removes leading whitespace or specified characters from the left side of a string.
👉 It does not modify the original string; instead, it returns a new string.
👉 lstrip() फंक्शन दिलेल्या स्ट्रिंगच्या सुरुवातीला असलेली रिकामी जागा (whitespace) किंवा विशिष्ट अक्षरे काढून टाकते.
👉 मूळ स्ट्रिंग बदलत नाही, तर नवीन स्ट्रिंग परत करते.'''

'''🔹 Syntax (सिंटॅक्स)
string.lstrip(chars)'''

# ✅ Example

# e = "---Ranjana---"
# print("hi!",e.lstrip('-'),"come here")

'''<<<--------------------------------------------------------------------------------------------------------------------------------------------->>>'''

# 🔹 strip() Method in Python Strings

'''✅ What is strip()? (strip() म्हणजे काय?)
👉 The strip() method removes leading (left) and trailing (right) whitespace or specified characters from a string.
👉 It does not modify the original string; instead, it returns a new string.
👉 strip() फंक्शन दिलेल्या स्ट्रिंगच्या सुरुवातीला आणि शेवटी असलेली रिकामी जागा (whitespace) किंवा विशिष्ट अक्षरे काढून टाकते.
👉 मूळ स्ट्रिंग बदलत नाही, तर नवीन स्ट्रिंग परत करते.'''

'''🔹 Syntax (सिंटॅक्स)
string.strip(chars)'''

# ✅ Example

# e = "---Ranjana---"
# print("hi!",e.strip('-'),"come here")

'''<<<--------------------------------------------------------------------------------------------------------------------------------------------------------------->>>'''

# 🔹 split() Method in Python Strings

'''✅ What is split()? (split() म्हणजे काय?)
👉 The split() method breaks a string into a list of words based on a specified separator.
👉 If no separator is provided, it splits the string by spaces by default.
👉 The original string remains unchanged, and a list of substrings is returned.
👉 split() फंक्शन स्ट्रिंगला वेगवेगळ्या भागांमध्ये (words) विभागते आणि त्याचा एक लिस्ट (list) तयार करते.
👉 जर काहीही separator दिला नसेल, तर ती स्ट्रिंग स्पेसवरून विभाजित केली जाते.
👉 मूळ स्ट्रिंग बदलत नाही, तर नवीन लिस्ट परत मिळते.'''

'''
🔹 Syntax (सिंटॅक्स)
string.split(separator, maxsplit)

'''
# ✅ Example
# text = 'Python is a fun programming language'
# print(text.split())

# text1 = 'hello,my name is Pratik,I am 25 years old'
# print(text1.split(','))


'''<<<<----------------------------------------------------------------------------------------------------------------------------------->>>>'''

# ✅ What is Indexing in Strings?

'''👉 In Python, strings are sequences of characters, and each character has a unique index 
(position).
👉 Indexing allows us to access individual characters in a string using their position.

🔹 Types of Indexing in Python:
Positive Indexing → Starts from 0 (left to right).

Negative Indexing → Starts from -1 (right to left).
index(start:stop:step)

✅ स्ट्रिंगमध्ये प्रत्येक अक्षराला विशिष्ट क्रमांक (index) असतो.
✅ 0 पासून सुरू होणारे पॉझिटिव्ह इंडेक्स आणि -1 पासून सुरू होणारे निगेटिव्ह इंडेक्स असतात.
✅ अवैध इंडेक्स वापरल्यास IndexError त्रुटी येते.'''


# text = 'Python is a fun programming language'
# print(text[::-1])

# print(text[4])

# print(text[-7])
# '''<<<<<------------------------------------------------------------------------------------------------------------------------------------------------------->>>>>'''
# text2 = 'How are you'    
# print(text2 * 2)

# g = 12
# print(g * 2)

# text = 'Python is a fun programming language'
# text1 = 'hello,my name is Pratik,I am 25 years old'
# print(text +  text1)

# text = 'Python is a fun programming language'
# f = 12
# print(text + f)




 
'''List is the sequence of order and represents '[]',
muatable,working through indexing,duplicates allowd
 '''

# 🔹 insert() Method in Python

'''✅ What is insert()? (insert() म्हणजे काय?)
👉 The insert() method is used to insert an element at a specific position in a list.
👉 It does not replace any existing element but shifts elements to the right after inserting the new one.
👉 insert() फंक्शन लिस्टमध्ये विशिष्ट स्थानावर (index) एक नवीन घटक (element) घालते.
👉 हे कोणत्याही विद्यमान घटकाची जागा घेत नाही, तर नवीन घटक घालते आणि उर्वरित घटक उजवीकडे सरकतात.'''

# 🔹 Syntax (सिंटॅक्स)
# list.insert(index, element)

# ✅ Example : Insert an Element at a Specific Index
# list1 = [1,2,3,4,5,6,7,5,9,10,"a","b","red"]
# list1.insert(6,4)
# print(list1)
'''<<<------------------------------------------------------------------------------------------------------------------------------------------------------->>>'''
# 🔹 append() Method in Python 

'''✅ What is append()? (append() म्हणजे काय?)
👉 The append() method adds an element at the end of a list.
👉 It does not replace any existing element; it simply expands the list.
👉 append() फंक्शन लिस्टच्या शेवटी नवीन घटक (element) जोडते.
👉 हे कोणत्याही विद्यमान घटकाची जागा घेत नाही, फक्त लिस्ट मोठी करते.'''

# 🔹 Syntax (सिंटॅक्स)
# list.append(element)

# ✅ Example: Append an Element to a List

# list1 = [1,2,3,4,5,6,7,5,9,10,"a","b","red"]
# list1.append("green")
# list1.append(20)
# print(list1)

'''<<<---------------------------------------------------------------------------------------------------------------------------------------------------------->>>'''
# 🔹 extend() Method in Python

'''✅ What is extend()? (extend() म्हणजे काय?)
👉 The extend() method is used to add multiple elements from another iterable
(list, tuple, set, string, etc.) to the end of a list.
👉 Unlike append(), which adds the entire iterable as a single element, extend()
adds individual elements from the iterable.
👉 extend() फंक्शन लिस्टच्या शेवटी एका दुसऱ्या लिस्ट, ट्युपल किंवा इतर इटेरेबलचे (iterable) सर्व घटक (elements) जोडते.
👉 append() संपूर्ण लिस्ट एका घटकासारखी जोडतो, पण extend() प्रत्येक घटक स्वतंत्रपणे जोडतो.'''

# 🔹 Syntax (सिंटॅक्स)
# list.extend(iterable)

# ✅ Example
# list1 = [1,2,3,4,5,6,7,5,9,10,"a","b","red"]
# list1.extend(["hi",30,56,"bye"])
# print(list1)

'''<<<------------------------------------------------------------------------------------------------------------------------------------------------------------->>>'''
# 🔹 remove() Method in Python

'''✅ What is remove()? (remove() म्हणजे काय?)
👉 The remove() method is used to delete the first occurrence of a specific element from a list.
👉 If the element is not found, it raises a ValueError.
👉 remove() फंक्शन लिस्टमधून दिलेल्या घटकाचा (element) पहिला सापडलेला (first occurrence) भाग काढून टाकते.
👉 जर घटक लिस्टमध्ये नसेल, तर ValueError एरर दाखवते.'''

# 🔹 Syntax (सिंटॅक्स)
# list.remove(element)

# ✅ Example: Removing an Element from a List

# list1 = [1,2,3,4,5,6,7,7,5,9,10,"a","b","red"]
# list1.remove(7)
# list1.remove(10)
# list1.remove(70)
# print(list1)
'''<<<---------------------------------------------------------------------------------------------------------------------------------------------------------->>>'''

# 🔹 pop() Method in Python

'''✅ What is pop()? (pop() म्हणजे काय?)
👉 The pop() method removes and returns an element from a list.
👉 By default, it removes the last element if no index is specified.
👉 If an index is given, it removes the element at that position.
👉 If the index is out of range, it raises an IndexError.

👉 pop() फंक्शन लिस्टमधून एखादा घटक (element) काढून टाकतो आणि त्याच वेळी तो परत (return) करतो.
👉 जर कोणताही index दिला नसेल, तर pop() शेवटचा (last) घटक काढतो.
👉 जर index दिला असेल, तर त्या index वरील घटक काढतो.
👉 जर index चुकीचा असेल (out of range), तर IndexError एरर दाखवतो.'''

# 🔹 Syntax (सिंटॅक्स)
# list.pop(index)  # Removes and returns element at 'index'

# ✅ Example:

# list1 = [1,2,3,4,5,6,7,5,9,10,"a","b","red"]
# list1.pop(11)
# list1.pop(8)
# list1.pop()
# list1.pop(55)
# print(list1)
# # '''<----------------------------------------------------------------------------------------------------------------------------------------------------->>>'''

# 🔹 reverse() Method in Python

'''✅ What is reverse()? (reverse() म्हणजे काय?)
👉 The reverse() method reverses the order of elements in a list in place (i.e., it modifies the original list).
👉 It does not return a new list but changes the original list directly.
👉 reverse() फंक्शन लिस्टमधील घटकांची क्रमवारी उलटी (reverse) करते.
👉 हे नवीन लिस्ट परत करत नाही, तर मूळ (original) लिस्ट बदलते.'''

# 🔹 Syntax (सिंटॅक्स)
# list.reverse()

# ✅ Example: Reversing a List
# list1 = [1,2,3,4,5,6,7,5,9,10,"a","b","red"]
# list1.reverse()
# print(list1)
'''<<<------------------------------------------------------------------------------------------------------------------------------------------>>>'''

# 🔹 len() Function in Python

'''✅ What is len()? (len() म्हणजे काय?)
👉 The len() function returns the number of elements in a sequence (like a list, string, tuple, dictionary, etc.).
👉 It is used to find the length of an object.
👉 len() फंक्शनचा उपयोग लिस्ट, स्ट्रिंग, ट्युपल, आणि इतर ऑब्जेक्ट्समधील घटक (elements) किती आहेत हे शोधण्यासाठी होतो.'''


# 🔹 Syntax (सिंटॅक्स)
# len(object)


# # ✅ Example: Using len() with a List
# list2 = [10.1,9.34,50,40,12,"python",True,[1,2,3]]
# print(len(list2))
# '''<<<------------------------------------------------------------------------------------------------------------------------------------------------------------->>>'''
# 🔹 sort() Function in Python

'''✅ What is sort()? (sort() म्हणजे काय?)
👉 The sort() method sorts the elements of a list in ascending (default) or descending order.
👉 It modifies the original list and does not return a new list.
👉 sort() फंक्शनचा उपयोग लिस्टमधील (list) घटक (elements) वाढत्या (ascending) किंवा घटत्या (descending) क्रमाने लावण्यासाठी केला जातो.
👉 हे मूळ (original) लिस्ट बदलते आणि नवीन लिस्ट परत करत नाही.'''

# 🔹 Syntax (सिंटॅक्स)

# list.sort(reverse=False)  # Default: Ascending order
# list.sort(reverse=True)   # Descending order

# ✅ Example 1: Sorting a List in Ascending Order
# list3 = [2,3,4,10.5,78.4,8,1]
# list3.sort()
# print(list3)

# ✅ Example 2: Sorting a List in Descending Order
# numbers = [5, 2, 9, 1, 7]
# numbers.sort(reverse=True)  # Sort in descending order
# print(numbers)
'''<<<--------------------------------------------------------------------------------------------------------------------------------------->>>'''



# 🔹 Accessing List Elements Using Indexing in Python

'''✅ What is List Indexing? (लिस्ट इंडेक्सिंग म्हणजे काय?)
👉 Indexing is used to access elements in a list.
👉 Python uses zero-based indexing (0 for the first element).
👉 Negative indexing allows accessing elements from the end (-1 for the last element, 
-2 for the second last, etc.).

👉 इंडेक्सिंगचा उपयोग लिस्टमधील घटक (element) ऍक्सेस करण्यासाठी केला जातो.
👉 Python मध्ये 0 पासून सुरुवात होते (zero-based indexing).
👉 -1, -2 यांसारख्या निगेटिव्ह इंडेक्सिंगने (negative indexing) शेवटच्या घटकांना ऍक्सेस करता येते.'''
# Syntax: list[start : stop : step]

# list2 = [10.1,9.34,50,40,12,"python",True,[1,2,3]]
# list2[0:4]=["Watermelon"]
# print(list2)
# print(list2[2:5:2])
# 
# print(list2[3:])

'''<<<------------------------------------------------------------------------------------------------------------------------>>>'''
# list1 = [1,2,3,4,5,6,7,5,9,10,"a","b","red"]
# list2 = [10.1,9.34,50,40,12,"python",True,[1,2,3]]
# print(list1 + list2)
# print(list2 * 3)


'''<----------------------------------------------------------------------------------------------------------------------------->>>'''


'''Tuple is used to store multiple items in single variable and represents '()',
immutable,ordered,duplicates allowed'''


'''Python मधील Tuple म्हणजे काय? (Marathi)
Python मध्ये tuple म्हणजे क्रमबद्ध आणि अपरिवर्तनीय (immutable) घटकांचा संग्रह होय. हे list प्रमाणेच असते, पण त्यामध्ये एकदा तयार झाल्यावर त्यात बदल (जसे की नवीन घटक जोडणे, काढणे किंवा बदलणे) करता येत नाही.

मुख्य वैशिष्ट्ये:
✅ क्रमबद्ध — घटकांची विशिष्ट क्रमवारी असते
✅ अपरिवर्तनीय — एकदा तयार झाल्यावर त्यात बदल करता येत नाही
✅ वेगवेगळ्या प्रकारचे डेटा ठेवू शकतो (उदा. string, number, इतर tuple)'''


tuple1 = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15) 

# print(tuple1[0:5])

# print(tuple1[6:2:-1])

# print(tuple1[:9])

# print(tuple1[2:])

# print(tuple1[5:15:3]) 
 
# print(tuple1[::4])

# print(tuple1[::-1])

# print(tuple1[-4])

# print(tuple1[-6:-2])

# print(tuple1[::-3])

# print(tuple1[-5::-2])

# print(tuple1[6:2:-2])


# #
# Tuple1 = (0, 1, 2, 3, 2, 3, 1, 3, 2)
# Tuple2 = ('python', 'geek', 'python','python', 'java', 'python')

# print(Tuple1.count(3))
# print(Tuple2.count('python'))








'''Sets are used to store multiple items in a single variable.
Set is an unorderd collection of data and represents "{}"_
it is muatable,does not allowed duplicate elements

sets do not maintain order, so items may appear in a different sequence each time you print them

Duplicates are automatically removed

Sets do not support indexing or slicing because they're unordered collections

'''


# 🔹 add() Method in Python

'''✅ What is add() in Python? (add() म्हणजे काय?)
👉 The add() method is used to add an element to a set.
👉 It does not allow duplicate values.
👉 add() फंक्शनचा उपयोग सेट (set) मध्ये नवीन घटक (element) घालण्यासाठी केला जातो.
👉 set मध्ये डुप्लिकेट (duplicate) मूल्ये परवानगी नसतात.'''

# 🔹 Syntax (सिंटॅक्स)
# set_name.add(element)

# ✅ Example 1: Adding Elements to a Set
# set1 = {1,2,3,4,5} 
# set1.add(10)
# print(set1)

# ✅ Example 2: Adding Elements to a Set
# fruits = {"apple", "banana", "cherry"}
# fruits.add("mango")
# print(fruits)
# '''<<<------------------------------------------------------------------------------------------------------------------------------------------------------------->>>'''

# 🔹 update() Method in Python

'''✅ What is update()? (update() म्हणजे काय?)
👉 The update() method is used to add multiple elements to a set at once.
👉 It can take lists, tuples, sets, or other iterables as input.
👉 It does not allow duplicate values.
👉 update() फंक्शनचा उपयोग सेट (set) मध्ये एकाच वेळी अनेक घटक (elements) घालण्यासाठी केला जातो.
👉 set मध्ये डुप्लिकेट (duplicate) मूल्ये परवानगी नसतात.'''

# 🔹 Syntax (सिंटॅक्स)
# set_name.update(iterable)



# ✅ Example 1: Adding Multiple Elements to a Set
# set1 = {1,2,3,4,5} 
# set1.update('red')
# set1.update(['red'])
# print(set1)

# fruits = {"apple", "banana", "cherry"}
# fruits.update(["mango", "grapes", "orange"])
# fruits.update("Raj")
# print(fruits)


# ✅ Example  2: Adding Elements from Another Set

# set1 = {1, 2, 3}
# set2 = {4, 5, 6}
# set1.update(set2)
# print(set1)

'''<<<---------------------------------------------------------------------------------------------------------------------------------------------------------------------->>>'''
# 🔹 remove() Method in Python

'''✅ What is remove()? (remove() म्हणजे काय?)
👉 The remove() method is used to delete a specific element from a set.
👉 If the element is not found in the set, it raises a KeyError.
👉 remove() फंक्शनचा उपयोग सेट (set) मधून एखादा विशिष्ट घटक (element) काढण्यासाठी केला जातो.
👉 जर घटक सेटमध्ये नसेल, तर KeyError येतो.'''

# 🔹 Syntax (सिंटॅक्स)
# set_name.remove(element)

# ✅ Example 1: Removing an Element from a Set
# set1 = {1,2,3,4,5}
# set1.remove(3) 
# set1.remove(8)
# print(set1)



'''<<<<-------------------------------------------------------------------------------------------------------------------------------------------------->>>>'''
# 🔹 discard() Method in Python

'''✅ What is discard()? (discard() म्हणजे काय?)
👉 The discard() method is used to remove a specific element from a set.
👉 If the element is not found, it does NOT raise an error (unlike remove()).
👉 discard() फंक्शनचा उपयोग सेट (set) मधून एखादा विशिष्ट घटक (element) काढण्यासाठी केला जातो.
👉 जर घटक सेटमध्ये नसेल, तरीही कोणतीही KeyError त्रुटी येत नाही.'''

# 🔹 Syntax (सिंटॅक्स)
# set_name.discard(element)

# ✅ Example 1: Removing an Element from a Set
# set1 = {1,2,3,4,5} 
# set1.discard(5)
# set1.discard(8)
# print(set1) 
'''<<<----------------------------------------------------------------------------------------------------------------------------------------------------------->>>'''

# 🔹 union() Method in Python

'''✅ What is union()? (union() म्हणजे काय?)
👉 The union() method combines two or more sets and returns a new set containing all unique elements.
👉 It does NOT modify the original sets.
👉 Duplicates are removed automatically.
👉 union() फंक्शनचा उपयोग दोन किंवा अधिक set एकत्र करण्यासाठी केला जातो.
👉 हे नवीन set परत देते आणि मूळ set बदलत नाही.
👉 डुप्लिकेट (duplicate) मूल्ये आपोआप काढली जातात.'''

# 🔹 Syntax (सिंटॅक्स)
# set1.union(set2, set3, ...)

# ✅ Example 1: Union of Two Sets
# set1 = {1,2,3,4,5}                     
# set2 = {6,7,1,2}
# set3 = set2.union(set1)
# print(set3)

# A = {1, 2, 3}
# B = {3, 4, 5}
# result = A.union(B)
# print(result)

# set1 = {"apple", "banana"}
# set2 = {"banana", "cherry"}
# set3 = {"mango", "apple"}
# result = set1.union(set2, set3)
# print(result)
'''<<<<---------------------------------------------------------------------------------------------------------------------------------------------------------------->>>>'''





'''Dictionary is a key:value pair of items an it is unorderd and represnts "{key:value}"
it is muatable,does not allowed duplicate'''


# 🔹 update() Method in Dictionary

'''✅ What is update() in Dictionary? (update() म्हणजे काय?)
👉 The update() method adds key-value pairs from another dictionary or
iterable (like a list of tuples) to the existing dictionary.
👉 If a key already exists, its value gets updated.
👉 It modifies the original dictionary instead of creating a new one.
👉 update() फंक्शनचा उपयोग dictionary मध्ये नवीन key-value जोडण्यासाठी केला जातो.
👉 जर key आधीपासून अस्तित्वात असेल, तर त्याची value अपडेट होते.
👉 मूळ dictionary बदलतो, नवीन dictionary तयार करत नाही.'''

# 🔹 Syntax (सिंटॅक्स)
# dict1.update(dict2)

# ✅ Example 1: Updating a Dictionary with Another Dictionary

# student = {"name": "John", "age": 20}
# new_data = {"age": 21, "city": "New York"}

# student.update(new_data)
# print(student)

# dict = {1:"a",2:"b",3:"c",4:"d",5:"e"}
# dict.update({6:'f'})
# dict[3] = 'k' 
# print(dict)


# dict = {1:"a",2:"b",3:"c",4:"d",5:"e"}
# print(dict.keys())
# print(dict.values())


# dict.pop(3)
# print(dict)

# print(dict.items())     


# dict = {1:"a",2:"b",3:"c",4:"d",5:"e"}

# dict1 = dict.copy()
# print ("Dict1:",dict1)

# add three dict in one dict
# d1 = {10:'a',20:'b'}
# d2 = {30:'c',40:'d'}
# d3 = {50:'e',60:'d'}

# d2.update(d1) 

# d2.update(d3)

# print("d2:",d2)

    
'''The range() function in Python is a built-in function used to generate a sequence of numbers. 
It is commonly used in loops to iterate a specific number of times. Here's a breakdown of its functionality:
Syntax:
The range() function has three possible syntaxes:
range(stop): Generates a sequence of numbers starting from 0 up to
(but not including) the stop value, incrementing by 1.



range(start, stop): Generates a sequence of numbers 
starting from the start value up to (but not including) the stop value, incrementing by 1.

range(start, stop, step): Generates a sequence of numbers
starting from the start value up to (but not including) the stop value, incrementing by the step value.

Parameters:

start: (Optional) The starting value of the sequence. If not provided, it defaults to 0.
stop: (Required) The ending value of the sequence. The sequence will stop before this value.
step: (Optional) The increment between each number in the sequence. If not provided, it defaults to 1. 
Key Characteristics:
The range() function generates numbers up to, but not including, the stop value.
It only works with integers.
The step value can be negative to generate a sequence of numbers in descending order.
Common Use Cases:
Iterating a specific number of times in a for loop.
Generating a sequence of numbers for indexing purposes.
Creating custom sequences with specific start, stop, and step values.'''


# Examples:

# a=range(10)
# print(a)

# for i in a:
#     print(i)

# range(stop)
# for i in range(5):
#     print(i)  

# range(start, stop)
# for i in range(2, 7):
#     print(i)  

# range(start, stop, step)
# for i in range(1, 10, 2):
#     print(i)  

# Negative step
# for i in range(10, 0, -2):
#     print(i)  






'''
Numeric Types

int: Represents whole numbers, e.g., 42.

float: Represents decimal numbers, e.g., 3.14.

complex: Represents complex numbers with real and imaginary parts, e.g., 2 + 3j.

Text Type

str: Represents sequences of Unicode characters, e.g., "Hello, World!".

Sequence Types

list: Ordered, mutable collection of items, e.g., [1, 2, 3].

tuple: Ordered, immutable collection of items, e.g., (1, 2, 3).

range: Represents a sequence of numbers, commonly used for looping a specific number of times, e.g., range(5).


Mapping Type

dict: Unordered collection of key-value pairs, e.g., {"name": "Alice", "age": 25}.

Set Types

set: Unordered collection of unique items, e.g., {1, 2, 3}.

frozenset: Immutable version of a set.

Boolean Type

bool: Represents truth values, True or False.


Binary Types

bytes: Immutable sequence of bytes, e.g., b"hello".

bytearray: Mutable sequence of bytes.

memoryview: Memory view object that allows Python code to access the internal data of an object that supports the buffer protocol without copying.


None Type

NoneType: Represents the absence of a value, e.g., None.'''


# data types

# Text: str

# Numbers: int, float, complex

# Sequences: list, tuple, range

# Mapping: dict

# Sets: set, frozenset

# Boolean: bool

# Binary: bytes, bytearray, memoryview

# NoneType: NoneType (None)


