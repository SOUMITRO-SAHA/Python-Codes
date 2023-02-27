class Faction:
    def __init__(self,n,d):
        self.num = n
        self.den = d

    def __str__(self): # Same as .toString() in Java:
        return "{}/{}".format(self.num, self.den)