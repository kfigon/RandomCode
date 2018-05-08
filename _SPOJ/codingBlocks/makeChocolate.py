import unittest

'''
We want make a package of goal kilos of chocolate. 
We have small bars (1 kilo each) and big bars (5 kilos each). 
Return the number of small bars to use, assuming we always use big
 bars before small bars. Return -1 if it can't be done.
'''

def make_chocolate(small, big, goal):
    ileDuzychTrzeba = goal//5
    if ileDuzychTrzeba <= big:
        if ileDuzychTrzeba*5 + small >= goal:
            return goal - ileDuzychTrzeba*5
        else:
            return -1

    elif big*5 + small >= goal:
        return goal - big*5
        
    return -1

class TestTestMakeChocolate(unittest.TestCase):
    def test0(self):
        self.assertEqual(4, make_chocolate(4, 1, 9))
    def test1(self):
        self.assertEqual(-1, make_chocolate(4, 1, 10))
    def test2(self):
        self.assertEqual(2, make_chocolate(4, 1, 7))
    def test3(self):
        self.assertEqual(2, make_chocolate(6, 2, 7))
    def test4(self):
        self.assertEqual(0, make_chocolate(4, 1, 5))
    def test5(self):
        self.assertEqual(4, make_chocolate(4, 1, 4))
    def test6(self):
        self.assertEqual(4, make_chocolate(5, 4, 9))
    def test7(self):
        self.assertEqual(3, make_chocolate(9, 3, 18))
    def test8(self):
        self.assertEqual(-1, make_chocolate(3, 1, 9))
    def test9(self):
        self.assertEqual(-1, make_chocolate(1, 2, 7))
    def test10(self):
        self.assertEqual(1, make_chocolate(1, 2, 6))
    def test11(self):
        self.assertEqual(0, make_chocolate(1, 2, 5))
    def test12(self):
        self.assertEqual(5, make_chocolate(6, 1, 10))
    def test13(self):
        self.assertEqual(6, make_chocolate(6, 1, 11))
    def test14(self):
        self.assertEqual(-1, make_chocolate(6, 1, 12))
    def test15(self):
        self.assertEqual(-1, make_chocolate(6, 1, 13))
    def test16(self):
        self.assertEqual(0, make_chocolate(6, 2, 10))
    def test17(self):
        self.assertEqual(1, make_chocolate(6, 2, 11))
    def test18(self):
        self.assertEqual(2, make_chocolate(6, 2, 12))
    def test19(self):
        self.assertEqual(50, make_chocolate(60, 100, 550))
    def test20(self):
        self.assertEqual(6, make_chocolate(1000, 1000000, 5000006))
    def test21(self):
        self.assertEqual(7, make_chocolate(7, 1, 12))
    def test22(self):
        self.assertEqual(-1, make_chocolate(7, 1, 13))
    def test23(self):
        self.assertEqual(3, make_chocolate(7, 2, 13))
if __name__=='__main__':
    unittest.main()