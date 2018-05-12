import unittest
from polirytm import GeneratorPolirytmow

class TestyGeneratora23(unittest.TestCase):
    def setUp(self):
        self.g = GeneratorPolirytmow(2,3)
    def test(self):
        exp = [['X','O','X'], ['O','X','O']]
        self.assertEqual(exp, self.g.generuj())
    def testStr(self):
        exp="X O X \nO X O \n"
        self.assertEqual(exp, str(self.g))

class TestyGeneratora34(unittest.TestCase):
    def setUp(self):
        self.g = GeneratorPolirytmow(3,4)
    def test(self):
        exp = [['X','O','O','X'], ['O','O','X','O'], ['O','X','O','O']]
        self.assertEqual(exp, self.g.generuj())
    def testStr(self):
        exp="X O O X \nO O X O \nO X O O \n"
        self.assertEqual(exp, str(self.g))

if __name__ == '__main__':
    unittest.main()
