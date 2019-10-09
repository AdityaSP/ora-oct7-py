def f(n):
    li = [1,2,3]
    li[n]
    1/n

f(1)

try:
    f(5)
except IndexError as err:
    print("Please check the index")
try:    
    f(0)
except ZeroDivisionError as err:
    print("Cannot divide by zero")

try:
    n = int(input("Enter a number: "))
    f(n)
except IndexError as err:
    print("Please check the index")
except ZeroDivisionError as err:
    print("Cannot divide by zero")
except Exception as err:
    print("Oops. Was not expecting this")
    

print("End of Program")
