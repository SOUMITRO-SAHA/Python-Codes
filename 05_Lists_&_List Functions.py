grocery = ["Harpic", "Vim bar", "Deodrant", "Soap", "Phenyl"]  # This is a list
grocery1 = ["Harpic", "Vim bar", "Deodrant", "Soap", "Phenyl", 100]  # This is a mixed list

print(grocery)
print(grocery1)

""" ------------------- Accessing the list items ------------------------"""
print(grocery[0])  # The counting of list items will start from "Zero [0]"
print(grocery[1])
print(grocery[2])
print(grocery[3])
print(grocery[4])
# print(grocery[5])   # It shows an IndexError because there are no item left which indicates 5th Item.
# print(grocery[6])

"""-------------------- Now List for Numbers ------------"""
num = [1, 5, 6, 9, 2, 4, 7]
print(num)  # It will print the list as it is
# From Now on the magic of programming will happen.Let see What I am talking about

# num.sort()  # It will sort the numbers in ascending order just writing one line of code.
# print(num)
#
# num.reverse()   # It will sort the numbers in descending order
# print(num)

""" We also access the list like just before """
print(num[4])  # the counting will start from 0 and will carry on to the last number.
""" Slicing of the list """
print(num[0:6])  # '''It is the default value we also can write "print(num[:])" '''
# Extended Slicing
print(num[::2])
print(num[::-3])  # Do not take -Ve no. less than -1 because it most of the time gives blank list
print(num[0:5:-2])  # that what I am talking about. so don't take value less then -1.

""" ------ Some other functions ----------"""
# print(len(num))
# print(max(num))
# print(min(num))
""" ########## Let's learn some other cool things with a new list ##########"""
no = [2, 6, 7, 9, 0, 1]

# no.append(8)  # It will add 8 at the end of the list.
# no.insert(2,69)  # It will insert 69 at 2th place.
# no.remove(0)  # It will remove 0 from the list
# no.pop()  # It will remove the last no. form the list.
# print(no)

""" New Topic"""
no[1] = 23  # It will change the 1th place no. to 23.
print(no)
# Mutable = Can change {by default avery list is mutable}
# Immutable = Cannot change. {tuple}
tp = (1,4,7)  # it is a tuple and it's an Immutable object and we can not change it's value

"""tp[1] = 8  # It will show error massage like ""'tuple' object does not support item assignment"" """
# If we assign only one value in tuple it has to be like,
tp1 = (1,)  # we have to add an extra , at the end. Otherwise it will not act as a tuple
tp2 = (4)  # It will act as normal container.
print(tp)
print(tp1)
print(tp2)

""" Interchange between two numbers """
a = 4
b = 9
"""# Traditional method in other Languages
# temp = a
# a = b
# b = temp
# print(a,b)  # It will surely be invert the no. but lets see in Python"""

a,b = b,a
print(a,b)  # and that's it.
