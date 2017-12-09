__author__ = 'kamil'

import unittest

# Multiples of 3 and 5
# Problem 1
#
# If we list all the natural numbers below 10 that are multiples of 3 or 5,
# we get 3, 5, 6 and 9. The sum of these multiples is 23.
#
# Find the sum of all the multiples of 3 or 5 below 1000.


def ileXWygenerowac(x, granica):
    ile = (int)((granica-1)/x)
    return ile

def foo(granica):
    ile3Wygenerowac = ileXWygenerowac(3, granica)
    ile5Wygenerowac = ileXWygenerowac(5, granica)

    suma=0
#     for i in range(granica):
#         if(i % 3 == 0 or i % 5==0):
#             suma += i

    # szereg arytmetyczny!
    suma3 =  3* ((ile3Wygenerowac+1)*ile3Wygenerowac)/2
    suma5 =  5* ((ile5Wygenerowac+1)*ile5Wygenerowac)/2

    return suma3+suma5

class TestyMult(unittest.TestCase):
    def test1(self):
        self.assertEqual(23, foo(10))

    def test2(self):
        self.assertEqual(33, foo(11))

    def test3(self):
        self.assertEqual(233168, foo(1000))

    def testGenerowania(self):
        self.assertAlmostEqual(9, ileXWygenerowac(1,10))
        self.assertAlmostEqual(4, ileXWygenerowac(2,10))
        self.assertAlmostEqual(3, ileXWygenerowac(3,10))
        self.assertAlmostEqual(2, ileXWygenerowac(4,10))
        self.assertAlmostEqual(1, ileXWygenerowac(5,10))
        self.assertAlmostEqual(2, ileXWygenerowac(5,14))
        self.assertAlmostEqual(2, ileXWygenerowac(5,15))
        self.assertAlmostEqual(3, ileXWygenerowac(5,16))
        self.assertAlmostEqual(1, ileXWygenerowac(8,10))
        self.assertAlmostEqual(1, ileXWygenerowac(9,10))
        self.assertAlmostEqual(0, ileXWygenerowac(10,10))

    def testGen2(self):
        self.assertAlmostEqual(333, ileXWygenerowac(3,1000))
        self.assertAlmostEqual(199, ileXWygenerowac(5,1000))

if __name__ == '__main__':
    unittest.main()
