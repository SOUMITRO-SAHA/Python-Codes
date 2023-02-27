# Python Arithmetic operations:
# x = 20
# y = 10

# print(x+y) # 30
# print(x-y) # 10
# print(x*y) # 200
# print(x/y) # 2.0 => Decimal Value
# print(x%y) # 0 => Modulo Operator.
# print(x**y) # 20^10 => Power Operator.
# print(x//y) # 20/10 => Floor Value only.[aka, Floor Division]

# Python Assignment operations:

# a = 10
# a &= 3 # 2

# b = 5 
# b |= 3 # 7

# c = 10
# c ^= 3 # 9

# d = 10
# d >>= 3 # 1

# e = 10
# e <<= 3 # 80
# print(a)
# print(b)
# print(c)
# print(d)
# print(e)

# Python Identity Operators:

# x = ["apple", "banana"]
# y = ["apple", "banana"]
# z = x

# print(x is z)

# # returns True because z is the same object as x

# print(x is y)

# # returns False because x is not the same object as y, even if they have the same content

# print(x == y)

# # to demonstrate the difference betweeen "is" and "==": this comparison returns True because x is equal to y

# '''
# Output:
# True
# False
# True
# '''

# print(x is not z)

# # returns False because z is the same object as x

# print(x is not y)

# # returns True because x is not the same object as y, even if they have the same content

# print(x != y)

# # to demonstrate the difference betweeen "is not" and "!=": this comparison returns False because x is equal to y

# '''
# Output:
# False
# True
# False
# '''

# Python Membership Operators:

x = ["apple", "banana"]

print("banana" in x) # True
# returns True because a sequence with the value "banana" is in the list

print("pineapple" not in x) # False
# returns True because a sequence with the value "pineapple" is not in the list