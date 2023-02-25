# Creating a function:
def fun():
    print("Hello, world!")

# Calling a function:
fun()

# Argument Passing:
def functionDemo( *args):
    for i in range(len(args)):
        print(args[i])

functionDemo('a','b','c','d', 1, 2, 3, 4, 5)

'''
Output:
a
b
c
d
1
2
3
4
5
'''

# Default Parameter Value:
def my_function(country = "Norway"): # (country = "Norway"), This is the default parameter.
    print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")

# Passing a List as an Argument:
def my_function(food):
    for x in food:
        print(x)

fruits = ["apple", "banana", "cherry"]

my_function(fruits)

# Return Values:
def my_function(x):
    return 5 * x

print(my_function(3))
print(my_function(5))
print(my_function(9))