import time
from threading import Thread

def somework(x):
    print("Start", x)
    time.sleep(5)
    print("End", x)

#for i in range(5):
#    somework(i)   # blocking calls / sync calls

for i in range(5):
    t = Thread(target=somework, args=[i])
    t.start()     # async calls
    
    
# print statement of python 2.x is not thread  safe
# print function in python 3.x is thread safe

# print start, 0 , \n    
# print start, 1 , \n    
# print start, 2 , \n    
# print start, 3 , \n    
# print start, 4 , \n    
#console
