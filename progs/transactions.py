import bank


sa = bank.SA('Aditya')
print(sa.n, sa.b, sa.t)
sa.credit(100)
print(sa.n, sa.b, sa.t)
sa.debit(2000)

ca = bank.CA('ABC Inc')
print(ca.n, ca.b, ca.t)
ca.credit(100)
print(ca.n, ca.b, ca.t)
ca.debit(2000)
print(ca.n, ca.b, ca.t)
