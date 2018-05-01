'''
Given 3 int values, a b c, return their sum. However, if one of the values is 13 then it does 
not count towards the sum and values to its right do not count. So for example, if b is 13, then both b and c do not count.


lucky_sum(1, 2, 3) → 6
lucky_sum(1, 2, 13) → 3
lucky_sum(1, 13, 3) → 1
'''
import unittest

def lucky_sum(a,b,c):
    vals = (a,b,c)
    suma =0
    for v in vals:
        if v == 13:
            break
        suma += v
    return suma

class TestTestLuckySum(unittest.TestCase):
    def test0(self):
        self.assertEqual(6, lucky_sum(1, 2, 3))
    def test1(self):
        self.assertEqual(3, lucky_sum(1, 2, 13))
    def test2(self):
        self.assertEqual(1, lucky_sum(1, 13, 3))
    def test3(self):
        self.assertEqual(1, lucky_sum(1, 13, 13))
    def test4(self):
        self.assertEqual(13, lucky_sum(6, 5, 2))
    def test5(self):
        self.assertEqual(0, lucky_sum(13, 2, 3))
    def test6(self):
        self.assertEqual(0, lucky_sum(13, 2, 13))
    def test7(self):
        self.assertEqual(0, lucky_sum(13, 13, 2))
    def test8(self):
        self.assertEqual(13, lucky_sum(9, 4, 13))
    def test9(self):
        self.assertEqual(8, lucky_sum(8, 13, 2))
    def test10(self):
        self.assertEqual(10, lucky_sum(7, 2, 1))
    def test11(self):
        self.assertEqual(6, lucky_sum(3, 3, 13))
    def test12(self):
        self.assertEqual(0, lucky_sum(13, 1, 2))

if __name__=='__main__':
    unittest.main()