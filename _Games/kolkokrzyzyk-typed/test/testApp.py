import unittest
from app import sayHello

class TestFoo(unittest.TestCase):
    def test0(self):
        self.assertEqual('hello andy', sayHello('andy'))

if __name__=='__main__':
    unittest.main()

