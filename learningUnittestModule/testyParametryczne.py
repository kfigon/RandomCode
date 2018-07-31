import unittest

def czyParzysta(x):
    return x % 2 == 0

class Test(unittest.TestCase):
    
    def testLiczbyParzystej(self):
        kejsy = [
            (0, True),
            (1, False),
            (2, True),
            (4, True),
            (6, True),
            (8, True)]
            
        for x, expectedResult in kejsy:
            nazwa = "when {} then {}".format(str(x), str(expectedResult))
            with self.subTest(name=nazwa):
                res = czyParzysta(x)
                self.assertEqual(expectedResult, res)

    def testyFailujace(self):
        for x, exp in [(1, True), (2, False)]:
            nazwa = "when {} then {}".format(x, exp)
            with self.subTest(nazwaTestu=nazwa):
                self.assertEqual(exp, czyParzysta(x))

    def testyOk(self):
        expectedOk = [2,4,6,2,0,8,10]
        for x in expectedOk:
            with self.subTest(x=str(x)):
                self.assertTrue(czyParzysta(x))

if __name__ == '__main__':
    unittest.main()