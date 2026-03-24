'''FOR LOOP'''

# Write a program to print numbers from 1 to 10 using a for loop.

# for i in range(1, 11):
#     print(i)
    

# Write a program to print even numbers from 1 to 20.

# for i in range(1, 20):
#     if i%2 == 0:
#         print("No. is EVEN", i)
        
#     else:
#         print("No. is ODD", i)


# Write a program to print the multiplication table of a given number.
# num = 2
# for i in range(1, 11):
#     print(f"{num} X {i} = {num * i}")


# Write a program to find the sum of numbers from 1 to 100.

# Write a program to print squares of numbers from 1 to 10.
# for i in range(1, 11):
#     print(f"{i} = {i*i}")

# Write a program to find the factorial of a number using a for loop.
# factorial = 1
# for i in range(1,11):
#     factorial = factorial * i
#     print(f"{i} of factorial {factorial}")

# Write a program to print the sum of even and odd numbers separately from 1 to 20.
# list = []
# list1 = []
# for i in range(1, 21):
#     if i % 2 == 0:
#         list.append(i)
        
#     else:
#         list1.append(i)
# print("EVEN Numbers: ", list)
# print("ODD Numbers: ", list1)
# print("Sum of Even and Odd numbers is : ", list + list1)

# Write a program to print multiples of 5 from 1 to 100.
# for i in range(1, 101):
#     if i % 5 == 0:
#         print("multiple of 5 is: ", i)

# Write a program to print each character of a string using a for loop.
# for i in "irfan":
#     print(i)

# Write a program to count vowels in a string using a for loop.
# count = 0
# string = "character"
# for i in string:
#     if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
#         count = count + 1

# print("Vowels : ", count) 


# for i in range(1, 5):
#     for j in range(i):
#         print("*", end=" ")
#     print()

# for i in range(5, 0, -1):
#     for j in range(i):
#         print("*", end=" ")
#     print()



# for i in range(1,5):
#     for j in range(1, i+1):
#         print(j, end=" ")
#     print()


# for i in range(20, 0, -1):
#     for j in range(10, i - 1):
#         print(j, end=" ")
#     print()


# for i in range(1,5+1):
#     for j in range(i):
#         print(chr(65+j), end=" ")
#     print()


# for i in range(5, 0, -1):
#     for j in range(i):
#         print(chr(65+j), end=" ")
#     print()


# for i in range(1, 5+1):
#     print(" " * (5 - i), end="")
#     for j in range(i):
#         print(i, end=" ")
#     print()


# for i in range(5, 0, -1):
#     print(" " * (5 - i), end="")
#     for j in range(i):
#         print(i, end=" ")
#     print()


# Write a program to check if a number is prime using a for loop.
# num = int(input("Enter the number: "))
# prime = True
# for i in range(2, num):
#     if (num % i == 0): 
#        prime = False
#        break
   
# if prime:
#     print("Number is prime")
# else:
#     print("number is not prime")


# Print all even numbers from 1 to 20.
# for i in range(1,10):
#     if i % 2 == 0:
#         print(i)
        
# Calculate the sum of digits in a number (e.g., 1234 → 10)
# num = 12345
# total=0
# for i in str(num):
#     total += int(i)
# print(total)

# Print the multiplication table for a given number.
# num = 2
# for i in range(1, 11):
#     result = num * i
#     print(f"{num} X {i} =", result)
    # print(f"{num} X {i} = {i*num}") # Optional

# Reverse a string using a for loop.
# string = 'irfan'
# rev = ""
# for i in "irfan":
#     rev = i + rev
# print(rev)

# Count how many vowels are in a given string.
# string = "python is fun language"

            # this for returning count of vowels
# vowels = "aeiouAEIOU"
# count =0 
# for i in string:
#     if i in vowels:
#         count += 1
# print(count)

                # this is for only returning vowels
# # for i in string:
# #     if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
# #         print(i)
# #     # else:
# #     #     print("no vowels are present")

#  Find Largest & Smallest (without min/max)
li = [1,7,3,7,9,3]
# small = li[0]
# large = li [0]

# for i in li:
#     if i<small:
#         small = i
#     elif i>large:
#         large = i
        
# print("largest: ", large)
# print("smallest: ", small)

#  Remove Duplicates (Preserving Order)

# see= []
# result=[]

# for i in li:
#     if i not in see:
#         see.append(i)
#         result.append(i)
# print(result)

# Rotate a List by k Positions (Right)
# k=2
# for i in range(k):
#     last = li.pop()
#     li.insert(0, last)
    
# print(li)

# Find Second Largest Element
# large = li[0]
# second_large = None

# for i in li:
#     if i>large:
#         large= i
# for i in li:
#     if i != large:
#         if second_large is None or i>second_large:
#             second_large = i
        
# print(large)
# print(second_large)

# Count the frequency of each character in a string using a dict.
# name = "irfan"
# freq = {}
# for i in name:
#     if i in freq:
#         freq[i] +=1
#     else:
#         freq[i]=1
# print(freq)

# Merge two dictionaries; if a key exists in both, sum the values.
dict = {1:"irfan", 2:"tayyab"}
# dict1 = {1:"mulani"}
# merge = dict.copy()
# for key,value in dict1.items():
#     merge[key] = value 
# print(merge)

# Invert a dictionary (swap keys and values).
# inverted = {v:k for k,v in dict.items()}
# print(inverted)

# shift common element in end of the list
# li = [1,4,2,4,1,5]
# see = []
# duplicate = []
# for i in li:
#     if i not in see:
#         see.append(i)
#     else:
#         duplicate.append(i)
# result = see + duplicate
# print(result)

# n=5
# for i in range(0, 5):
#     for j in range(i+1):
#         print(" *", end=" ")
#     print()

# for i in range(0,5):
#     for j in range(i, 5):
#         print("*", end=" ")
#     print()

# for i in range(0,5):
#     for j in range(i, 5):
#         print(" ", end=" ")
#     for e in range(i+1):
#         print("*", end=" ")
#     print()

# for i in range(0, 5):
#     for j in range(i + 1):
#         print(" ",end=" ")
#     for e in range(i, 5):
#         print("*", end=" ")
#     print()

# for i in range(0, 5):
#     for j in range(i,5):
#         print(" ", end=" ")
#     for e in range(i):
#         print("*", end=" ")
#     for f in range(i+1):
#         print("*", end=" ")
#     print()

# for i in range(0, 5):
#     for e in range(i+1):
#         print(" ", end=" ")
#     for f in range(i,5-1):
#         print("*", end=" ")
#     for j in range(i,5):
#         print("*", end=" ")
#     print()