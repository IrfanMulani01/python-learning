'''
Data Types:-Variables can hold values and every value has a data-type.
type()<-function-which returns the type of variable passed.


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

# a = 20 
# print(a)    
# print(type(a))

# '''String'''

# b = "hello"
# print(b)      
# print(type(b))

# # # '''Float'''

# c = 3.14
# print(c)
# print(type(c))                 

# # # d = 2.34444
# # # print(d)
# # # print(type(d))

# # # # '''Complex'''

# e = complex(1+0j)           
# print(e)
# print(type(e))


# # # # # '''List'''

# f = ["orange", "yellow", "green"]     
# print(f)           
# print(type(f))

# # # # # # '''Tuple'''

# g = ("orange", "yellow", "green")
# print(g)
# print(type(g))

# # # # # # # # # '''Set'''

# h = {"orange", "yellow", "green"}
# print(h)
# print(type(h))

# # # # # # # # '''Dictionary'''

# i = {"name" :"Reshma", "gender" : "female"}
# print(i)
# print(type(i))


# # # '''Range'''

# j = range(8)
# print(j)
# print(type(j))

# # # # # # '''Boolean'''

# k = False
# print(k)
# print(type(k))


'''String:String is the sequence of characters represents ' '' ''',
'''immutable,duplicates allowed,ordered collection'''

a = "explicit"
b = "Implicit"
c = "NESTED"
d = "5"
e = "---Ranjana---"
text = 'Python is a fun programming language'
text1 = 'hello,my name is Priya,I am 25 years old'
text2 = 'How are you'
f = 12
g = 12


# print(a.capitalize())

# print(b.casefold())
# print(b.upper())
# print(c.lower())
# print(c.isupper())
# print(a.islower())
# print(d.isnumeric()) 
# print(e.count('a'))
# print("hi!",e.lstrip('-'),"come here")
# print("hi!",e.strip('-'),"come here")
# print(text.split(' '))
# print(text1.split(','))
# print(text[2:6])
# print(text[4])
# print(text2 * 3)
# print(g * 2)
# print(text +  text1)
# print(text + f)

'''List is the sequence of order and represents '[]',
muatable,working through indexing,duplicates allowd
 '''
list1 = [1,2,3,4,5,6,7,5,9,10,"a","b","red"]
# list1.insert(6,4)
# list1.append("green")
# list1.append(20)
# list1.extend(["hi",30,56,"bye"])
# list1.remove(7)
# list1.remove(10)
# list1.pop(8)
# list1.reverse()
# print(list1)




list2 = [10.1,9.34,50,40,12,"python",True,[1,2,3]]
# list2[0:4]=["Watermelon"]
# print(len(list2))
# print(list2[3:])
# list2 = [1,2,3,4,5,6,7,8,9,10,12,13]
# print(list2[2:10:3])                    
# print(list1 + list2)
# print(list2 * 3)
# list3 = [2,3,4,10.5,78.4,8,1]
# list3.sort()
# print(list3)
# print(list2)



'''Tuple is used to store multiple items in single variable and represents '()',
immutable,ordered,duplicates allowed'''

tuple1 = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15) 

# print(tuple1[2:9])
# print(tuple1[:9])
# print(tuple1[2:])
# print(tuple1[5:15:3])    
# print(tuple1[::4])
# print(tuple1[::-3])
# print(tuple1[-4])
# print(tuple1[::-1])
# print(tuple1[-5::-2])



# Tuple1 = (0, 1, 2, 3, 2, 3, 1, 3, 2)
# Tuple2 = ('python', 'geek', 'python','python', 'java', 'python')

# print(Tuple1.count(2))
# print(Tuple2.count('python'))

'''Sets are used to store multiple items in a single variable.
Set is an unorderd collection of data and represents "{}"
it is muatable,doest not allowed duplicate elements'''

set1 = {1,2,3,4,5}                     
set2 = {6,7,1,2}
# set1.add(10) 
# set1.update('red') 
# set1.update(['red'])
# set1.remove(3) 
# set1.discard(5)
# print(set1)

# set3 = set2.union(set1)
# print(set3)


'''Dictionary is a key:value pair of items an it is unorderd and represnts "{key:value}"
it is muatable,does not allowed duplicate'''

dict = {1:"a",2:"b",3:"c",4:"d",5:"e"}
# print(dict.keys())
# print(dict.values())


# dict.update({6:'f'})
# dict[3] = 'k' 

# dict.pop(3)


# print(dict)
# dict1 = dict.copy()
# print("Dict1:",dict1)

# # add three dict in one dict
# d1 = {10:'a',20:'b'}
# d2 = {30:'c',40:'d'}
# d3 = {50:'e',60:'d'}

# d2.update(d1)

# d2.update(d3)
# print("d1:",d1)
# print("d2:",d2)



