# SA -> t = 'S', b cannot be -ve, b = 100
# CA -> t = 'C', b can be -ve, b = 0
# DRY --> Dont Repeat Yourself
class SA():
    def __init__(self, n, b=100):
        self.n = n
        self.b = b
        self.t = 'S'
    def credit(self, amount):
        self.b += amount
    def debit(self, amount):
        if self.b < amount:
            print("Insufficient Balance")
        else :
            self.b -= amount
class CA():
    def __init__(self, n, b=0):
        self.n = n
        self.b = b
        self.t = 'C'
    def credit(self, amount):
        self.b += amount
    def debit(self, amount):
        self.b -= amount





