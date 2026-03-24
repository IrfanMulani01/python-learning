'''
4.variable length or Arbitary Arguments:
pass multiple arguments to the function.
when we used Arbitrary arguments,if we don't know the number of arguments needed for the function in advance.
Types of Arbitrary Arguments:

1.arbitrary positional arguments (*args)
2.arbitrary keyword arguments (**kwargs)
'''
'''
1.arbitrary positional arguments (*args):
*args in variable length.Internally all these values are reprensented in the form of tuple. 
# '''
# def car(*name,model):  #form of tuple
#     print(name)
#     print(model)
# car('city','verna','Q7','Maybatch',model='A8')


# def new(title, *project):
#     print(title)
#     print(project)

# new('sales','marketing','A25','A1800')

# def num(*args):
#     print(args)
# num('a','b','c',1,2,3,4,5)

# def printinfo( arg1, *vartuple ):
#    "This prints a variable passed arguments"
#    print("Output is: ",arg1)
#    for var in vartuple:
#       print(var)
#    return

# printinfo( 10 )
# printinfo( 70, 60, 50 )



# def percentage(*args):
#     sum = 0
#     for i in args:
#         # get total
#         sum = sum + i
#     # calculate average
#     avg = sum / len(args)
#     print('Average =', avg)

# percentage(56, 61, 73)

'''
2.arbitrary keyword arguments (**kwargs):
**kwargs in keyword .Keyword arguments passed to a kwargs are acced using key-value pair(Dictionary)
# # # '''
# def num(**kwargs):  #form of dictionary
#     print(kwargs)
# num(salary = 10000, city ='pune', name = 'max',age = 20)


# def var(**kwargs):
#     print(kwargs)
# var(place ='max',city = 'pune',name = 'python',salary = 15000, age = 18)


# variable number of keyword arguments---->Dictionary
# rno = 100
# name = "Raj"
# avg = 98.9
# def display(**kwargs):

#    print(type(kwargs))
#    for k,v in kwargs.items():
#        print(k,"----->",v)

#        print("________________")
       
  
# print(f"Rno = {rno} Name = {name} Avg = {avg}")

# display(name = "Raj" , avg = 98.9 , rno = 100)
# display(name = "Raj" , avg = 98.9)
# display(name = "Raj" , avg = 98.9 , rno = 100,classsn = "ENGG2")
# display(bg = "A+ve", div = "A", grade = "A+")



# def percentage(**kwargs):
    
#     for sub in kwargs:
#         # get argument name
#         sub_name = sub
#         # get argument value
#         sub_marks = kwargs[sub]
#         print(sub_name, "=", sub_marks)

# # # pass multiple keyword arguments
# percentage(math=56, english=61, science=73)


'''both arbitrary positional and keyword argument use'''

# def all_aboard(a, *args, **kw): 
#    print(a, args, kw)

# all_aboard(2, 56, 89, 4, 7, x=3, y=0)









    


'''passing list as an arg and return value'''
   
# def maximum(a, b, c): 
#    list = [a, b, c] 
#    return max(list) 
# # Driven code  
# x = int(input("Enter First number"))
# y = int(input("Enter Second number"))
# z = int(input("Enter Third number"))
# print("Maximum Number is",maximum(x, y, z)) 
