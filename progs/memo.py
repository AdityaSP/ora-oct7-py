import time

#memoization
def memo(f):
    d = {}
    def wrapper(x):
        if x not in d:
            d[x] = f(x)
        return d[x]
#        if x in d:
#            return d[x]
#        else:
#            d[x] = f(x)
#            return d[x]
    return wrapper    
    
#def memo(f):
#    def wrapper(x):
#        return f(x)
#    return wrapper    
        
@memo
def calculate(x):
    time.sleep(5)
    return x ** 4
#d = {}   
s = time.time() 
print(calculate(4))  
#d = {4: 256}
print(calculate(4))    
#d = {4: 256}
print(calculate(4))    
#d = {4: 256}
print(calculate(5))
#d = {4: 256, 5:625}
print(calculate(5))
e = time.time()
print("Took:", e-s , "seconds")
