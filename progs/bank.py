class Account():
    def __init__(self, n, b, t):
        self.n = n
        self.b = b
        self.t = t
    def credit(self, amount):
        self.b += amount
    def debit(self, amount):
        self.b -= amount


ac1 = Account('Aditya', 100, 'S')
print(ac1.n, ac1.b, ac1.t)
ac1.credit(100000)
print(ac1.n, ac1.b, ac1.t)
ac1.debit(100)
print(ac1.n, ac1.b, ac1.t)


