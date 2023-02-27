class Fraction:
    def __init__(self,n,d):
        self.num = n
        self.den = d

    def __add__(self,other):
        self.den = self.den * other.den
        self.num = (other.den)*(self.num) + (self.den)*(other.num)

    def __str__(self): # Same as .toString() in Java:
        return "{}/{}".format(self.num, self.den)
    
