# Exercise -2 Faulty calculator
# 45*3 = 555, 56+7= 77, 56/6 = 4
# Design a calculator which will correctly solve all the problems except
# the following one.


print("Welcome to Calculator: ")
n1 = int(input("Enter 1st No. - "))
n2 = int(input("Enter 2nd No. - "))
op = input("What operation would you perform : +, -, *, / ")
c1 = 45 * 3 == 135
if n1 == 45 and n2 == 3 and op == '*':
    print("555")
elif n1 == 56 and n2 == 9 and op == '+':
    print(77)
elif n1 == 56 and n2 == 6 and op == '/':
    print(4)
elif op == '+':
    print(n1 + n2)
elif op == '-':
    print(n1 - n2)
elif op == '*':
    print(n1 * n2)
elif op == '/':
    print(n1 / n2)
elif n1 == 45 and n2 == 3 and op == '*':
    print("555")
else:
    print("Out of range")
