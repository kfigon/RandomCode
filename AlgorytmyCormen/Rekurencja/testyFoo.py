__author__ = 'kamil'

import unittest
import math
from foo import silnia
from foo import fibonacci
from foo import fibonacciX
from foo import potega
from foo import ciag
from foo import konwersjaNaBinarna

class testySilni(unittest.TestCase):
    def test1(self):
        self.assertEqual(math.factorial(1),silnia(1))

    def test2(self):
        self.assertEqual(math.factorial(2),silnia(2))

    def test3(self):
        self.assertEqual(math.factorial(3),silnia(3))

    def test4(self):
        self.assertEqual(math.factorial(4),silnia(4))

    def test5(self):
        self.assertEqual(math.factorial(5),silnia(5))

    def test6(self):
        self.assertEqual(math.factorial(6),silnia(6))

    def test7(self):
        self.assertEqual(math.factorial(7),silnia(7))

    def test8(self):
        self.assertEqual(math.factorial(8),silnia(8))

    def test9(self):
        self.assertEqual(math.factorial(9),silnia(9))

    def test10(self):
        self.assertEqual(math.factorial(10),silnia(10))

    def test11(self):
        self.assertEqual(math.factorial(11),silnia(11))

class testyFibonacciego(unittest.TestCase):
    def test0(self):
        self.assertEqual(0, fibonacci(0))

    def test1(self):
        self.assertEqual(1, fibonacci(1))

    def test2(self):
        self.assertEqual(1, fibonacci(2))

    def test3(self):
        self.assertEqual(2, fibonacci(3))

    def test4(self):
        self.assertEqual(3, fibonacci(4))

    def test5(self):
        self.assertEqual(5, fibonacci(5))

    def test6(self):
        self.assertEqual(8, fibonacci(6))

    def test7(self):
        self.assertEqual(13, fibonacci(7))

    def test8(self):
        self.assertEqual(21, fibonacci(8))

    def test9(self):
        self.assertEqual(34, fibonacci(9))

    def test10(self):
        self.assertEqual(55, fibonacci(10))

    def test11(self):
        self.assertEqual(89, fibonacci(11))

    def test12(self):
        self.assertEqual(144, fibonacci(12))

    def test15(self):
        self.assertEqual(610, fibonacci(15))

    def test19(self):
        self.assertEqual(4181, fibonacci(19))

class testyFibonacciegoBezRekurencji(unittest.TestCase):
    def test0(self):
        self.assertEqual(0, fibonacciX(0))

    def test1(self):
        self.assertEqual(1, fibonacciX(1))

    def test2(self):
        self.assertEqual(1, fibonacciX(2))

    def test3(self):
        self.assertEqual(2, fibonacciX(3))

    def test4(self):
        self.assertEqual(3, fibonacciX(4))

    def test5(self):
        self.assertEqual(5, fibonacciX(5))

    def test6(self):
        self.assertEqual(8, fibonacciX(6))

    def test7(self):
        self.assertEqual(13, fibonacciX(7))

    def test8(self):
        self.assertEqual(21, fibonacciX(8))

    def test9(self):
        self.assertEqual(34, fibonacciX(9))

    def test10(self):
        self.assertEqual(55, fibonacciX(10))

    def test11(self):
        self.assertEqual(89, fibonacciX(11))

    def test12(self):
        self.assertEqual(144, fibonacciX(12))

    def test15(self):
        self.assertEqual(610, fibonacciX(15))

    def test19(self):
        self.assertEqual(4181, fibonacciX(19))

class testyPotegowania(unittest.TestCase):
    def test2_0(self):
        self.assertEqual(math.pow(2, 0), potega(2,0))
    def test2_1(self):
        self.assertEqual(math.pow(2, 1), potega(2,1))
    def test2_2(self):
        self.assertEqual(math.pow(2, 2), potega(2,2))
    def test2_3(self):
        self.assertEqual(math.pow(2, 3), potega(2,3))
    def test2_4(self):
        self.assertEqual(math.pow(2, 4), potega(2,4))

    def test4_3(self):
        self.assertEqual(math.pow(4,3), potega(4,3))
    def test4_4(self):
        self.assertEqual(math.pow(4,4), potega(4,4))
    def test4_5(self):
        self.assertEqual(math.pow(4,5), potega(4,5))
    def test4_6(self):
        self.assertEqual(math.pow(4,6), potega(4,6))

    def test6_3(self):
        self.assertEqual(math.pow(6,3), potega(6,3))
    def test6_5(self):
        self.assertEqual(math.pow(6,5), potega(6,5))
    def test8_5(self):
        self.assertEqual(math.pow(8,5), potega(8,5))

class testyCiagu(unittest.TestCase):
    def test1(self):
        self.assertEqual(-1, ciag(1))

    def test2(self):
        self.assertEqual(-1, ciag(2))

    def test3(self):
        self.assertEqual(0, ciag(3))

    def test4(self):
        self.assertEqual(-3, ciag(4))

    def test5(self):
        self.assertEqual(12, ciag(5))

class testyKonwersjiBinarnej(unittest.TestCase):
    def test5(self):
        self.assertEqual("101", konwersjaNaBinarna(5))
    def test8(self):
        self.assertEqual("1000", konwersjaNaBinarna(8))
    def test53(self):
        self.assertEqual("110101", konwersjaNaBinarna(53))

if __name__ == '__main__':
    unittest.main()
