# Polymorphism :
# Can be achieved through the:
# - Method Overriding
# - Method Overloading
# - Operator Overloading

# ================ [Method Overriding] =================== # 
# Studied in Java.

# ================ [Method Overloading] =================== # 
# Note: Technically Method Overloading is not allowed in Python. But we can tweak a little to make it work.
""" 
class Quadrilateral:
    def area(self, side):
        return side * side # Area of a Square.
    
    def area(self, l, b):
        return l * b # Area of a Rectangle.
    
    def area(self, l, b, h):
        return l * b * h # Area of a Cuboid.
    
rec = Quadrilateral()
print(rec.area(2)) # We can not access this method anymore.
print(rec.area(2,3)) # We can not access this method anymore.
print(rec.area(2,3,5)) # This is the final Method. The can be access.

# This code is not gonna work in Python. Because, we can not write two different methods with the same name.
"""
# But, With some tweaking We can active out objective.
class Quadrilateral:
    def area(self, l, b = 0):
        if b == 0:
            return l * l # Area of a Square
        return l * b # Area of a Rectangle.
    
rec = Quadrilateral()
print(rec.area(2))      # This is going to work in Python.
print(rec.area(2,5))    # This is going to work in Python.


# ================ [Operator Overloading] =================== # 
