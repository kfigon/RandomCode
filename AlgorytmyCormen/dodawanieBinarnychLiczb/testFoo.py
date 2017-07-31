__author__ = 'kamil'

import unittest
from foo import dodaj

class testyDodawaniaBinarnego(unittest.TestCase):

    def test1(self):
        a=[1,1,0]   # 6
        b = [0,0,1] # 1
        self.assertEqual([0,1,1,1], dodaj(a,b))

    def test2(self):
        a = [1,0,1]
        b = [0,1,1]

        self.assertEqual([1,0,0,0], dodaj(a,b))

    def test3(self):
        a = [1,1,1]
        b = [1,1,1]

        self.assertEqual([1,1,1,0], dodaj(a,b))


if __name__ == '__main__':
    unittest.main()
