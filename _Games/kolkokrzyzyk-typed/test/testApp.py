import unittest
from app import sayHello, sayAgain

class TestFoo(unittest.TestCase):
    def test0(self):
        self.assertEqual('hello andy!', sayHello('andy'))
    
    def test1(self):
        self.assertEqual('hello andy!', sayAgain('andy'))

if __name__=='__main__':
    unittest.main()

