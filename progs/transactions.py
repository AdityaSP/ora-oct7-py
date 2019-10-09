import bank

ac1 = bank.Account('Aditya', 100, 'S')
print(ac1.n, ac1.b, ac1.t)
ac1.credit(100000)
print(ac1.n, ac1.b, ac1.t)
ac1.debit(100)
print(ac1.n, ac1.b, ac1.t)