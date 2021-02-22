import unittest
from code import *

class TestParsing(unittest.TestCase):
    def test1(self):
        self.fail('todo')

class Test(unittest.TestCase):
    def test1(self):
        matrix = [[5,3,4],[1,5,8],[6,4,2]]
        got, cost = createMagicSquare(matrix)
        expectedMagicSquare = [[8,3,4],[1,5,9],[6,7,2]]
        expectedCost = 7
        self.assertEqual(cost, expectedCost)
        self.assertEqual(got, expectedMagicSquare)

if __name__ == '__main__':
    unittest.main()