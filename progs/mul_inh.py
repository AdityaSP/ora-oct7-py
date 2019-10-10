class A():
    def f(self):
        print("From A")
class B(A):
    pass
class C(A):
    pass
class D(B, C):
    pass   


# Linearization of multi derived classes
# mro --> method resolution order
print(D.mro())

obj = D()
obj.f()

A.f(obj)

    