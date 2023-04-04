import unittest

'''
For this problem, we'll round an int value up to the next multiple of 
10 if its rightmost digit is 5 or more, 
so 15 rounds up to 20. 

Alternately, round down to the previous
 multiple of 10 if its rightmost digit is less than 5, 
 so 12 rounds down to 10. Given 3 ints, a b c, return the sum of 
 their rounded values. To avoid code repetition, write a separate 
 helper "def round10(num):" and call it 3 times. 
 
 Write the helper entirely below and at the same indent level as round_sum().
'''

def zaokr(x):
    jednosc = x % 10
    if jednosc >= 5:
        return x + 10-jednosc
    else:
        return x -jednosc

def round_sum(a,b,c):
    vals = (a,b,c)
    sum = 0
    for i in vals:
        sum += zaokr(i)
    return sum

class TestTestRoundSum(unittest.TestCase):
    def test0(self):
        self.assertEqual(60, round_sum(16, 17, 18))
    def test1(self):
        self.assertEqual(30, round_sum(12, 13, 14))
    def test2(self):
        self.assertEqual(10, round_sum(6, 4, 4))
    def test3(self):
        self.assertEqual(20, round_sum(4, 6, 5))
    def test4(self):
        self.assertEqual(10, round_sum(4, 4, 6))
    def test5(self):
        self.assertEqual(10, round_sum(9, 4, 4))
    def test6(self):
        self.assertEqual(0, round_sum(0, 0, 1))
    def test7(self):
        self.assertEqual(10, round_sum(0, 9, 0))
    def test8(self):
        self.assertEqual(40, round_sum(10, 10, 19))
    def test9(self):
        self.assertEqual(90, round_sum(20, 30, 40))
    def test10(self):
        self.assertEqual(100, round_sum(45, 21, 30))
    def test11(self):
        self.assertEqual(60, round_sum(23, 11, 26))
    def test12(self):
        self.assertEqual(70, round_sum(23, 24, 25))
    def test13(self):
        self.assertEqual(80, round_sum(25, 24, 25))
    def test14(self):
        self.assertEqual(70, round_sum(23, 24, 29))
    def test15(self):
        self.assertEqual(70, round_sum(11, 24, 36))
    def test16(self):
        self.assertEqual(90, round_sum(24, 36, 32))
    def test17(self):
        self.assertEqual(50, round_sum(14, 12, 26))
    def test18(self):
        self.assertEqual(40, round_sum(12, 10, 24))
if __name__=='__main__':
    unittest.main()