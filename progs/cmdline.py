def add(x,y):
    return x + y

import sys
print(sys.argv)
print(add(int(sys.argv[1]), int(sys.argv[2])))