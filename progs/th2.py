import time
from threading import Thread, Event

a = 0

def consumer():
    for i in range(5):
        time.sleep(3)
        e.wait()
        print(a)
        e.clear()
    
def producer():
    global a
    for i in range(5):
        time.sleep(5)
        a +=100
        e.set()
        

e = Event()
p = Thread(target=producer)
c = Thread(target=consumer)

p.start()
c.start()
        