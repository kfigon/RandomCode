import unittest

class TestMapy(unittest.TestCase):
    
    def test1(self):
        tab = [1,2,3,4,5]
        expKwadraty = [1,4,9,16,25]

        self.assertEqual(expKwadraty, list(map(lambda x: x**2, tab)))

    def testFiltra18(self):
        wiek=[1,13,54,12,4,19,25]
        exp=[54,19,25]

        self.assertEqual(exp, list(filter(lambda x: x>=18, wiek)))

    def testLambdaTenary(self):

        foo = lambda x: 'tak' if x >=18 else 'nie'
        self.assertEqual('tak', foo(18))
        self.assertEqual('tak', foo(19))
        self.assertEqual('tak', foo(20))

        self.assertEqual('nie', foo(7))
        self.assertEqual('nie', foo(17))
        self.assertEqual('nie', foo(1))

    def testTenary(self):
        def signum(x):
            return 1 if x>=0 else 0
        
        self.assertEqual(1, signum(1))
        self.assertEqual(1, signum(2))
        self.assertEqual(1, signum(3))

        self.assertEqual(0, signum(-1))
if __name__ == '__main__':
    unittest.main()