import sys
import unittest
if len(sys.argv) != 2:
    print("Usage: main.py <test config.csv>")
    print("Exiting...")
    exit(-1)
    
ts = unittest.TestSuite()
fh = open(sys.argv[1], 'rt')
for line in fh:
    tc = line.strip().split(',')
    if "module" in tc or tc[-1] not in 'yY01':
        continue
    #tc is a list of ['TestBank', 'test_sacreate', 'y']
    #import TestBank
    exec('import ' + tc[0])
    ts.addTest(eval("{}.{}('{}')".format(tc[0],tc[1],tc[2])))
    
r = unittest.TextTestRunner(verbosity = 3)
r.run(ts)
    
    
