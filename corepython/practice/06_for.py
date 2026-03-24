'''
Python for Loop:-
Loop - sometimes we want to repeat a set of statement in our program. 
and it tells to the computer which set of instuctions to repeat and how?.

Two types of loop - 
1.for loop 
2.while loop
'''
'''
A for loop is used to itrate through a sequence like list,tuple or string[iterables]
Iterating over a sequence is called traversal.
'''
'''
Syntax:
for itrator_var in sequence:
    statements(s)

Rest of the code   

for (initialization; condition; iteration)
{
//body of for loop
} 
'''
    
#using for loop in list

# l = [1,2,3,4,5,6,7,8]
# for item in l:
#     print(item)
    
# fruits = ["Banana","Apple","Orange","Grapes"]
# for var in fruits:
#     print(var)   
     
# for i in "maxgen":
#     print(i)

'''Range()function - 
   It is used to generate a sequence of numbers.(0 - (n-1))
   range(start, stop,step_size)  step_size is by default 1 if not provoided
'''
'''range using list'''

# print(list(range(10)))
# print(list(range(2, 8)))
# print(list(range(2, 20, 2)))

# '''range using tuple'''

# print(tuple(range(10)))
# print(tuple(range(2, 8)))
# print(tuple(range(2, 20, 3)))

# range(5)
# start=0
# condition<5
# increment 1 (by default)
#0 1 2 3 4

# for i in range(6):
#     if i< 5:
#         print(i)
    
#range(1,6)
# start=0
# condition<6
# increment 1 (by default)
#1 2 3 4 5

# for i in range(1,6):
#     if i<5:
#         print(i)            
            
        
#range(1,6,2)
# start=0
# condition<6
# increment 2 (from range)
#1 3 5

# for i in range(1,6,2):
#     if i<6:
#         print(i)

# for i in range(1,10,2):
#     if i<10:
#         print(i) 
        
              
# for i in range(8):
#     print(i)
    
# for i in range(3,9):
#     print(i)    

# for i in range(1,10,3):  
#     print(i)

'''Program to iterate through a list using indexing'''

# genre = ['pop', 'rock', 'jazz']

# # iterate over the list using index
# for i in range(len(genre)):
#     print("I like", genre[i])

# for i in range(10):
#     if i == 8:
#         break 
#                     #    it instruct the program to exit the loop now
#     print(i)                
    
# for i in range(13):
#     if i == 7:
#         continue                   #it instruct the program to skip the iteration
#     print(i)    
    
# i = 3
# if(i<3):
#     pass

# # # # # #                                    #it instruct to Do nothing
# print("hi welcome to python")

# list1 = []
# list2 = []

# for i in range(1,21):
#     if i % 2 == 0:                                  
#         list1.append(i)
#     else:
#         list2.append(i)
# print("list of even numbers:",list1)
# print("list of odd numbers",list2)

   
        
# names = ["Sonam","Anidha","Priyanka","Sonali"]

# for name in names:
#     if name.startswith("S"):
#         print("Hello "+ name)

'''With Dictionary'''

# name = "Nikhil"
# dict = {"Suraj":12,"Nikhil":3,"Priya":7}
# for i in dict:
#     if i == name:
#         print(dict[i])
#         break
# else:
#     print("no name found in dictionary")    

# num = int(input("Enter the number: "))
# prime = True

# for i in range(2, num):
#     if(num%i == 0):
#         prime = False
#         break
# if prime:
#     print(num,"This number is Prime")
# else:
#     print(num,"This number is not Prime")
                
        
# num = int(input("Enter a number:"))
                                            
# factorial = 1
                            
# for i in range(1,num+1): 
#     factorial = factorial * i                  
# print(f"The factorial of {num} is {factorial}")  



# n = int(input("Enter a table number :"))

# for i in range(1,11):
#     print(f'{n} x {i} = {n*i}')        
    
# x = ""
# for i in range(1,101):
#     a = str(i)

#     x = x + "+" + a 
# print(x)  

# s = 0                                                
# a = int(input("Enter a number:"))            
# for i in range(1,a+1,1):                           
#     s  = s + i                          
#     print(s) 

#'''Explanation'''
# 0 + (1+1) =   1                    
# 1 + (2+1) =   3
# 3 + (3+1) =  6
# 6 + (4+1) =   10
# 10 + (5+1) = 15
# 15 + (6+1) = 21                
    
# for x in ("yellow","white","pink","green","blue"):
#     if x == "pink":
#         break
#     print(x) 
    
# for x in(1,2,3,4,5,6,7,8,9):
#     if x == 5:
#         break
#     print(x)  
    
# for x in("monday","tuesday","wendsday","thrusday","friday","saterday","sunday"):
#     if x == "friday":
#         continue
#     print(x)           
    
# for x in(1,2,3,4,5):
#     if x == 3:
#         continue
#     print(x) 
'''
zip() is used to merge 2 lists together. It returns the first element of each list,
then 2nd element of each list, etc. 
This is a trick to consider the two lists as key and data to create a dictionary.'''
# l1 = [10,20,30,40,34,55,54]
# l2 = [50,60,70,80,99,56,34,67]

# for a,b in zip(l1,l2):
#     print(a,"->",b)

# x = zip(l1,l2)
# print(x)

# questions = ["name","quest","favorite color"]
# answers = ["lancelot","the holy grail","blue"]
# for q,a in zip(questions,answers):
#     print("What is your {0}? It is {1}.".format(q,a))

'''
When looping through a sequence, the position index and corresponding value can be retrieved 
at the same time using the enumerate() function.
# '''
# for i,v in enumerate(["tic","tac","toe"]):
#     print(i,v)

'''
To loop over a sequence in reverse, first specify the sequence in a forward direction and then call the
reversed() function.
'''
# for i in reversed(range(1, 10, 2)): 
#     print(i)

'''
To loop over a sequence in sorted order, use the sorted() function which returns a new sorted list while
leaving the source unaltered.
'''
# basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
# for f in sorted(set(basket)):
#     print(f)

    

    





    
    