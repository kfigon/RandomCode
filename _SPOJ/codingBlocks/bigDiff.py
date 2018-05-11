import unittest

'''
Given an array length 1 or more of ints, 
return the difference between the largest and 
smallest values in the array. 
Note: the built-in min(v1, v2) and max(v1, v2) functions 
return the smaller or larger of two values.
'''
def big_diff(tab):
    return max(tab) - min(tab)

class TestBigDiff(unittest.TestCase):
    def test0(self):
        self.assertEqual(7, big_diff([10, 3, 5, 6]))
    def test1(self):
        self.assertEqual(8, big_diff([7, 2, 10, 9]))
    def test2(self):
        self.assertEqual(8, big_diff([2, 10, 7, 2]))
    def test3(self):
        self.assertEqual(8, big_diff([2, 10]))
    def test4(self):
        self.assertEqual(8, big_diff([10, 2]))
    def test5(self):
        self.assertEqual(10, big_diff([10, 0]))
    def test6(self):
        self.assertEqual(1, big_diff([2, 3]))
    def test7(self):
        self.assertEqual(0, big_diff([2, 2]))
    def test8(self):
        self.assertEqual(0, big_diff([2]))
    def test9(self):
        self.assertEqual(8, big_diff([5, 1, 6, 1, 9, 9]))
    def test10(self):
        self.assertEqual(3, big_diff([7, 6, 8, 5]))
    def test11(self):
        self.assertEqual(3, big_diff([7, 7, 6, 8, 5, 5, 6]))
        
if __name__=='__main__':
    unittest.main()