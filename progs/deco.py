import time
import random

def timer(f):
	def wrapper():
		s = time.time()
		f()
		e = time.time()
		print("Took:", e-s, "secs")
	return wrapper

@timer
def heavyduty():
	time.sleep(random.randint(1,4))
    
    
heavyduty()
heavyduty()
heavyduty()
    