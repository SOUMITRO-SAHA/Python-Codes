# name = input("Enter your name : ")
# print(name)
# print("Type of name",type(name))
"""--------------------------"""
# x, y = input().split()

# print(x, y)
"""--------------------------"""
# Question -1 : Add two Numbers.
# num1 = int(input("Enter 1st number : \n"))
# num2 = int(input("Enter 2nd number : \n"))

# a = num1 + num2
# print("The Sum of num1 & num2 is -- ")
# print(num1 + num2)
# print("Type of a :", type(a))
"""-------End---------"""
""" Find Area of the Rectangle """
# # Length = L
# # Breadth = B
# # Area = A
# L, B = input().split()
# L1 = int(L)
# B1 = int(B)

# A = L1*B1
# print(A)
""" Print Name and age """
# """ Take the person's name and age as input and print out the name and age as specified in the output format."""
# name = input("Entre Your Name :")
# age = int(input("Enter Your age:"))
# print("The name of the person is ",name,"and the input age is ",age, end='.')
"""--------"""
"""Take two numbers as input and swap them and print the swapped values.
Input Format:
The first line of input contains a single integer 't', representing the total number of test cases.

The second line of input contains two integers 'a' and 'b', representing the second number. 
Output Format:
The first line of output prints the swapped value of 'a' and 'b'."""

# t = int(input("Enter the No. of test cases :"))
# a, b = input().split()
"""---------------------------------------------"""
# a = 10 
# b = 3
# # x = a // b
# # print(x)
# print(a > b)
# print(a < b)
"""Operators"""
# x = "Soumitra"
# l = [1,3,8]
# print('S'in x)
# print('Sou'in x)
# print('Soumitra'in x)
# print(1 in l)
# print(2 in l)

""" --------- Return Statement -----------"""
# def fact(n):
#     fact = 1
#     for i in range(1,n+1):
#         # fact = fact * i
#         fact *= i
#     return fact

# ans = fact(3)
# print(ans)

# def fact(n):
#     fact = 1
#     for i in range(1,n+1):
#         fact = fact * i
        
#     return fact
    
# ans = fact(5)
# print(ans)

""" --------------- Testing Code --------------"""
# # Nested List
# nList = ["ninja", [0, 0, 1, 1]]

# # Nested indexingprint(nList[0][1])
# print(nList[0][4])
# print(nList[1][1])
# List slicing in Python
myList = ['h','e','l','l','o','n','i','n','j','a','s']

# Elements 3rd to 5th
print(myList[2:5])

# Elements from beginning to 4th index.
print(myList[:-5])

# Elements 6th index to end.
print(myList[5:])

# Elements from beginning to end.
print(myList[:])