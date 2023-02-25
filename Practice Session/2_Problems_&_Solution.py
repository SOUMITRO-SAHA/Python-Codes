""" My Solution """
# def sum(N):
#     sum = 0
#     for i in range(1,N+1):
#         if i%2 == 0:
#             sum += i
#     return sum


# N = int(input("Entre the Number :"))
# even = sum(N)
# print(even)

""" Expert Solution """
# #Take the input
# n = int(input())


# #initialize the variable sm with value zero.
# sm = 0

# for i in range(0,n+1):

#     if(i % 2 == 0):
#         sm += i

# #print the value of sum.        
# print(sm)
""" Fahrenheit to Celsius """
# s = Start Fahrenheit value
# e = End Fahrenheit value
# w = Gap 
# Taking the inputs
# from math import floor


# s = int(input())
# e = int(input())
# w = int(input())
# i = 0
# E = e + w
# for i in range(s,E,w):
#     c = floor((((i - 32)*5) // 9))

#     print(i,c)

""" Expert Solution"""
# S = Start Fahrenheit value
# E = End Fahrenheit value
# W = Gap 
# Taking the inputs

# S = int(input())
# E = int(input())
# W = int(input())

# #Iterating over the loop with given step size as W. 

# for i in range(S,E + 1,W):

#     cel = int((i - 32) * 5 /9)

#     print(i,cel,sep = "\t")
""" Print the sum of even digits and odd digits of given number """
# Taking Input 
### Expert Solution
# n = int(input())
# evenSum = 0
# oddSum = 0

# while n > 0:

#     last = n % 10

#     #Checking for even case.
#     if n % 2 == 0:
#         evenSum += last

#     else:
#         #if the number is odd.
#         oddSum += last

#     n = n // 10

# print(evenSum,oddSum)

""" Find power of a number """
# My Solution 
### It worked
# a,b = input().split()
# x = int(a)
# n = int(b)

# c = x**n
# print(c)
# print(int(x),int(n))

""" Factorial of a Number """
## My Solution.
# n = int(input())
# fact = 1
# for f in range(1,n+1):
#     fact *= f

# if n > 0:
#     print(fact)
# elif n == 0:
#     print(1)
# else:
#     print("Error")

""" N-th Fibonacci Number """
# def f(n):
#     n = input()
#     if n > 0:
#         a = n - 1
#         b = n - 2

""" Print all Divisors of a number """
## My code
# n = int(input())
# def div(n):
#     for i in range(1,n+1):
#         if n % i == 0:
#             print(i, end=" ")
# div(n)
""" Set Bits """
'''Write a program to count the number of 1's in the binary representation of an integer.
Input Format :
 The only line of input contains a single integer N.
Output Format :
The only line of the output prints the total number of 1.'''

# n = int(input())
# a = (bin(n)[2:].zfill(16))
# c = 0
'''
##### Not Working Properly
# print(a)
# print(type(a))
# def sum(*args):
#     sum = 0
#     b = 0
#     for i in args:
#         b = int(i)
#         sum += b
#     print(sum)
# sum(a)'''

# for i in a:
#     b = int(i)
#     if b > 0:
#         c += b
# print(c)
""" Total Prime No. """
'''Write a program to find the total number of a primes number in a given interval.
Given two integers S and E, count all primes between S and E.
Input Format :
The only line of input contains two integers S and E separated by a single space.
Output Format :
The only line of the output prints the total number of primes.'''
import math

a, b = input().split()
a = int(a)
b = int(b)


def total_Prime(a, b):
    c = 0

    for i in range(a, b + 1):
        sq = int(math.sqrt(i))
        if i % sq != 0:
            print(i)
            i = 1
            c += i
    # print(c)


total_Prime(a, b)
