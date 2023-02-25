""" List Comprehension"""
# # A list Comprehension in side list []
# pow2 = [2 ** x for x in range(10)]
# print(pow2)
# # a list Comprehension outside list []
# pow3 = []
# for x in range(10):
#     pow3.append(2**x)
# print(pow3)
#
# # We can use other expressions to modify or creat a new list.
# newList = [x for x in range(12) if x % 2 == 1]
# print(newList)

""" Print items except some of the item that you wantto exclude. """
# list1 = [i for i in "myString" if i not in "aeiou"]
# for i in list1:
#     print(i)

""" Line Separated Input for 2-D list in Python """
# n = int(input())
# input = [[int(col) for col in input().split()] for row in range(n)]
# print(input)

""" Practicing Taking Test cases """
# Failed to do so.
# n = int(input())

""" Space Separated Input """
# #Number of the rows
# row = int(input())
#
# #Number of columns
# col = int(input())
#
# # Conperting input string to list
# inputList = input().split()
#
# fullList = [[int(inputList[i*col + j]) for j in range(col)] for i in range(row)]
# print(fullList)

" Printing in Multiple Lines Like a Matrix "
# twoDList = [[2,3,9],[1,2,3],[4,5,6]]
#
# # Iterate in row of 2-D list
# for row in twoDList:
#     #Iterate in column in 2-D list.
#     for col in row:
#         print(col,end=" ")
#     print()
"""Question on 2D-List """
# list=[[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# for j in range(4):
#     for element in list:
#         # print(element)
#         print(element[j],end = " ")
""" Problems Regarding List """
""" Find the index of a Element in a list """
# ele = input().split()
# x = int(input())
# list = []
# list.append(ele)

# print(list.index(x))
#### Expert Solution ######
""" Brute Force approach
- We creat a variable 'index' with value to store the answer.
- We iterate the array forward and update the value of 'index' if an occurrence of x is found.
we break out of this loop.
- Finally, print the value of 'index'."""
# def firstIndex(list,n,target):
#     index = -1
#     for i in range(n):
#         if list[i] == target:
#             return i
#     return -1
# # length
# n = int(input())
# list = [int(i) for i in input().split()]
# target = int(input())
# print(firstIndex(list,n,target))

""" Find the last index of a Element in a list """
### My Solution ####
# def lastIndex(arr,n,target):
#     index = -1
#     for i in range(n,0,-1):
#         if arr[-i] == target:
#             return i
#     return -1
# n = int(input())
# arr = [int(i) for i in input().split()]
# target = int(input())
# print(lastIndex(arr,n,target))]
####### --------- Expert Solution -------------########
""" Brute Force Approach
-- We create a variable last with value -1 to store the answer.
-- We iterate the array backwards and update the value of last if an occurrence of x is found. We break out of this loop.
-- Finally, print the value of last."""
# def lastIndex(arr,n,target):
#     index = -1
#     for i in range(n-1,-1,-1):
#         if arr[i] == target:
#             index = i
#             break
#     return index
# n = int(input())
# arr = [int(i) for i in input().split()]
# target = int(input())
#
# print(lastIndex(arr,n,target))
""" Reverse a Array/List in Python """
# list = [1,2,3,4,5,6,7]
# # l1 = list[::-1]
#
# print(list[::-1],end=" ")
###----Expert Solution-----###


def reverseArray(arr, start, end, length):
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1


length = int(input())
arr = [int(i) for i in input().split()]

reverseArray(arr, 0, length - 1, length)
print(*arr)


