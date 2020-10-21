__author__ = 'kamil'

import unittest
from foo import foo
from foo import dopiszDoKoncaStringa
from foo import iteracjaMnozenia
from foo import sumujWynikiCzastkowe

class testMult(unittest.TestCase):
    def test_none(self):
        self.assertEqual("0", foo("", ""))

    def test_1_2(self):
        self.assertEqual("2", foo("1","2"))
        self.assertEqual("2", foo("2","1"))

    def test_1_123(self):
        self.assertEqual("123", foo("1", "123"))
        self.assertEqual("123", foo("123", "1"))

    def test_123_2(self):
        self.assertEqual("246", foo("123", "2"))
        self.assertEqual("246", foo("2", "123"))

    def test_3_123(self):
        self.assertEqual("369", foo("123", "3"))
        self.assertEqual("369", foo("3", "123"))

    def test_4_123(self):
        self.assertEqual("492", foo("123", "4"))
        self.assertEqual("492", foo("4", "123"))

    def test_3_5(self):
        self.assertEqual("15", foo("3","5"))
        self.assertEqual("15", foo("5","3"))

    def test_10_123(self):
        self.assertEqual("1230", foo("123","10"))
        self.assertEqual("1230", foo("10","123"))

class testDopisywacza(unittest.TestCase):
    def test_basic(self):
        self.assertEqual("1", dopiszDoKoncaStringa("","1"))
    def test_11(self):
        self.assertEqual("11",dopiszDoKoncaStringa("1","1"))
    def test_12(self):
        self.assertEqual("12",dopiszDoKoncaStringa("2","1"))
    def test_123(self):
        self.assertEqual("123",dopiszDoKoncaStringa("23","1"))
    def test_123_2(self):
        self.assertEqual("123",dopiszDoKoncaStringa("3","12"))

class testIteracjiMnozenia(unittest.TestCase):
    def test_basic(self):
        jednosci, przeniesienie = iteracjaMnozenia(1,1, 0)
        self.assertEqual(1, jednosci)
        self.assertEqual(0, przeniesienie)

    def test_3_2(self):
        jednosci, przeniesienie = iteracjaMnozenia(3,2, 0)
        self.assertEqual(6, jednosci)
        self.assertEqual(0, przeniesienie)

    def test_3_4(self):
        jednosci, przeniesienie = iteracjaMnozenia(3,4, 0)
        self.assertEqual(2, jednosci)
        self.assertEqual(1, przeniesienie)

    def test_4_5_przeniesienie(self):
        jednosci, przeniesienie = iteracjaMnozenia(4,5, 1)
        self.assertEqual(1, jednosci)
        self.assertEqual(2, przeniesienie)

    def test_7_8_przeniesienie(self):
        jednosci, przeniesienie = iteracjaMnozenia(7,8, 1)
        self.assertEqual(7, jednosci)
        self.assertEqual(5, przeniesienie)

    def test_7_8(self):
        jednosci, przeniesienie = iteracjaMnozenia(7,8, 0)
        self.assertEqual(6, jednosci)
        self.assertEqual(5, przeniesienie)

# class testySumyWynikowCzastkowych(unittest.TestCase):
#     def test_basic(self):
#         self.assertEqual("123", sumujWynikiCzastkowe(["123"]))
#
#     def test_1_2(self):
#         self.assertEqual("3", sumujWynikiCzastkowe(["1","2"]))
#
#      def test_123_321(self):
#         self.assertEqual("444", sumujWynikiCzastkowe(["123","321"]))


if __name__ == '__main__':
    unittest.main()
