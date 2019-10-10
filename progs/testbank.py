import unittest
import bank

class TestBank(unittest.TestCase):
    def test_sacreate(self):
        sa = bank.SA('Aditya')
        assert sa.b == 100, "US101: default balance is 100"
    def test_cacreate(self):
        ca = bank.CA('ABC Inc.')
        assert ca.b == 0, "US102: default balance is 0"
    def test_sacredit(self):
        sa = bank.SA('Aditya')
        sa.credit(100)
        assert sa.b == 200, "US101: default balance is 100"
    def test_cacredit(self):
        ca = bank.CA('ABC Inc.')
        ca.credit(100)
        assert ca.b == 100, "US102: default balance is 0"
    
    
    
# Auto discovery of test cases
unittest.main(verbosity=3)   