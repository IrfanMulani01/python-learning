'''
Functions in python:-
-A function is a block of code which only runs when it is called.
-You can pass data, known as parameters, into a function.
-A value passed to a function when calling the function is called argument.
-A function can return data as a result.

फंक्शन म्हणजे कोडचा एक संच आहे जो केवळ आह्वान (call) केल्यावरच चालतो.

फंक्शनमध्ये डेटा—जो पॅरामीटर्स म्हणतात—दिवू शकतो.

जेव्हा आपण फंक्शन कॉल करतो, तेव्हा दिलेले ** arguments ** (उदा. 😉“Hello”) ही पॅरामीटर्सची मूल्यं असतात.

फंक्शन परिणाम म्हणून (return) एक मूल्य (value) परत करू शकतो.

Types of function:
1.user defined functions
2.built in functions
'''
# def कीवर्डने फंक्शन तयार केला जातो, त्याला नाव व पॅरामीटर्स देतो, नंतर कोड लिहितो.




# def fun():
#        print("Welcome to Function")
              
# fun()
'''____________________________________'''

# def names(fname,lname): 
#     print(fname+" "+lname)
    
# names("Pratik","Chavan") 


# def names(fname,lname):
#     print(fname+" "+lname)
    
# names("Pratik") 

# def evenOdd(x):
#     if x %  2== 0:
#         print("even")
#     else:
#         print("odd")
 
# evenOdd(4)
# evenOdd(5)

# def calci(a,b):
#     add = a + b
#     sub = a - b
#     mul = a * b
#     div = a / b
#     print(f"add = {add} sub ={sub} mul ={mul} div ={div}")          

# a = float(input("Enter a:"))
# b = float(input("Enter b:"))

# calci(a,b)






'''Docstrings:
the documentation string is also called a docstring. 
It is a descriptive text (like a comment) written by a programmer to let others know what block of code does.

It is being declared using triple single quotes (''' ''') or triple-double quote(""" """).
We can access docstring using doc attribute (__doc__) for any object like list, tuple, dict,and user-defined function, etc.



डॉकस्ट्रिंग म्हणजेच डॉक्युमेंटेशन स्ट्रिंग — ही फंक्शन, क्लास, किंवा मॉड्यूलच्या सुरुवातीला लिहिलेली स्ट्रिंग असते. हि रनटाइममध्ये __doc__ अॅट्रिब्यूटने किंवा help() मधून 

'''
# You can enclose them in either:

# Triple-double quotes: """..."""

# Triple-single quotes: '''...'''


'''
Single-Line Docstring:

Use triple quotes on the same line.

No blank lines before or after.

Ends with a period.


'''
# def vication(x):
#     """i am going for vication."""
    
# print(vication.__doc__ )

'''
Multi-Line Docstring:
# '''  
# def any_fun(parameter1):
#     """              
#    Description of function
                 
#    Arguments:   
#    parameter1(int):Description of parameter1
                 
#    Returns:      
#    int value     
# """              
# print(any_fun.__doc__)
   

'''4 types of functions arguments:

1. Positional Arguments (Required Arguments)
2. keyword Arguments
3. Default Arguments
4. variable Length Arguments(Arbitrary Arguments)'''








