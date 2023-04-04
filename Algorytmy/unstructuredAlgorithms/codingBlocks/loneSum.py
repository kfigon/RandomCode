'''

Given 3 int values, a b c, return their sum. However, if one of the values 
is the same as another of the values, it does not count towards the sum.


lone_sum(1, 2, 3) → 6
lone_sum(3, 2, 3) → 2
lone_sum(3, 3, 3) → 0
lone_sum(1, 2, 3) → 6
lone_sum(3, 2, 3) → 2
lone_sum(3, 3, 3) → 0
lone_sum(9, 2, 2) → 9
lone_sum(2, 2, 9) → 9
lone_sum(2, 9, 2) → 9
lone_sum(2, 9, 3) → 14
lone_sum(4, 2, 3) → 9
lone_sum(1, 3, 1) → 3
'''

import unittest


def loneSum(a,b,c):
    vals = (a,b,c)
    sum = 0
    for i in vals:
        ile = vals.count(i)
        if(ile == 1):
            sum += i

    return sum

class Test(unittest.TestCase):
    def test1(self):
        self.assertEqual(6, loneSum(1,2,3))
    
    def test2(self):
        self.assertEqual(2, loneSum(3,2,3))
    
    def test3(self):
        self.assertEqual(0, loneSum(3,3,3))

    def test4(self):
        self.assertEqual(9, loneSum(9,2,2))

    def test5(self):
        self.assertEqual(9, loneSum(2,2,9))

    def test6(self):
        self.assertEqual(14, loneSum(2,9,3))

    def test7(self):
        self.assertEqual(9, loneSum(4,2,3))

    def test8(self):
        self.assertEqual(3, loneSum(1,3,1))

if __name__ == '__main__':
    unittest.main()