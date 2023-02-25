a = "56"
b = "20"
print(a + b)  # You get an answer like 5620, it is because "a" and "b" both are Strings.

# Now to add "a" and "b" in mathematical order we have to change it's data type through type casting.
print(int(a)+int(b))
"""Now you must get the addition of "a" & "b". Because now we have changed it's data type in the
Print function."""

''' int()
    str()
    float()  '''

c = 45
d = 100

print(c+d)
print(10*c+d)  # Now it act as mathematical function.

# But if we try it with a string then it print the line that many times.

Add = c+d
print(str(Add))
print(10*str(Add))  # The Number must be printed 10 times.If we have to break the line we have to use"\n" tag.

Name1 = "Soumitra"
Name2 = "Soumitra\n"  # Run the code you will automatically understand the reason on adding \n at the end.

print(10*Name1)
print(10*Name2)


# ------------------ Input Function ---------------------#
print("Enter your 1st Number")
A = input()

print("Enter your 2nd Number")
B = input()
print("You just entered", int(A)+int(B))

'''------------ Calculator project-------------'''
print("You can Calculate any Number in here Just put the numbers down below.")
print("Enter your First Number =")
Frist = input()

# print("Enter what operation would you like to prefer. eg- +,-, \, *")
# Ope = input()
print("Enter your second Number =")
Second = input()

print("Your Result is")
# Result = int(Frist),Ope,int(Second)

print(int(Frist)+int(Second))
