import unittest

'''
Given three ints, a b c, return True if 
one of b or c is "close" (differing from a by at most 1), 
while the other is "far", differing from both 
other values by 2 or more. Note: abs(num) 
computes the absolute value of a number.
'''

def isOk(compared, compared2, loose):
    isFar = lambda x, y: abs(x-y) >= 2
    return not isFar(compared, compared2) and isFar(compared2, loose) and isFar(loose, compared)

def close_far(a,b,c):
    return isOk(b,a,c) or isOk(c,a,b)


class TestTestCloseFar(unittest.TestCase):
    def test0(self):
        self.assertEqual(True, close_far(1, 2, 10))
    def test1(self):
        self.assertEqual(False, close_far(1, 2, 3))
    def test2(self):
        self.assertEqual(True, close_far(4, 1, 3))
    def test3(self):
        self.assertEqual(False, close_far(4, 5, 3))
    def test4(self):
        self.assertEqual(False, close_far(4, 3, 5))
    def test5(self):
        self.assertEqual(True, close_far(-1, 10, 0))
    def test6(self):
        self.assertEqual(True, close_far(0, -1, 10))
    def test7(self):
        self.assertEqual(True, close_far(10, 10, 8))
    def test8(self):
        self.assertEqual(False, close_far(10, 8, 9))
    def test9(self):
        self.assertEqual(False, close_far(8, 9, 10))
    def test10(self):
        self.assertEqual(False, close_far(8, 9, 7))
    def test11(self):
        self.assertEqual(True, close_far(8, 6, 9))
if __name__=='__main__':
    unittest.main()