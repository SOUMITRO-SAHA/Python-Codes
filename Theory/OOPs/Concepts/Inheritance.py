class User:
    def login(self):
        print("Login")

    def register(self):
        print("Register")

class Student(User): # This line show Inheritance:
    def enroll(self):
        print("Enroll")

    def review(self):
        print("Review")

stu1 = Student() # Creating an Instance of a Class or Creating an Object of the Class...
stu1.login()
stu1.register()
stu1.enroll()
stu1.review()

# Types of Inheritance:
# - Single Level Inheritance
# - Multi-level Inheritance
# - hierarchical Inheritance
# - Multiple Inheritance [Not allowed in Java]
# - Hybrid Inheritance


# ==================== [MRO (Method Resolution Order)] ================= #
class Phone:
    def __init__(self, price, brand, camera):
        print("Inside Phone constructor")
        self.__price = price
        self.brand = brand
        self.camera = camera

    def buy(self):
        print("Buying a Phone")

class Product:
    def buy(self):
        print("Buying a Product")
class SmartPhone(Product, Phone): # Multiple Inheritance [Not allowed in Java], First Inherited from Product, then from Phone
    pass

s = SmartPhone(20000, "Apple", 14)
s.buy()

'''
Output:
Inside Phone constructor
Buying a Product
'''

class SmartPhone(Phone, Product): # Multiple Inheritance [Not allowed in Java], First Inherited from Phone, then from Product.
    pass

s = SmartPhone(20000, "Apple", 14)
s.buy()

'''
Output:
Inside Phone constructor
Buying a Phone
'''
# ==================== [Multiple Inheritance] ================= #
class A:
    def m1(self):
        return 20
    
class B(A):
    def m1(self):
        return 30

    def m2(self):
        return 40

class C(B):
    def m2(self):
        return 50
    
obj_1 = A()
obj_2 = B()
obj_3 = C()

print(obj_1.m1() + obj_2.m1() + obj_3.m2()) # 20 + 30 + 50.