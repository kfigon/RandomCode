import unittest
# Given an array of ints, return True if the array contains a 2 next to a 2 somewhere.
def has22(nums):
    for i in range(len(nums)-1):
        if nums[i] == 2 and nums[i+1] == 2:
            return True
    return False

class TestHas22(unittest.TestCase):
    def test0(self):
        self.assertEqual(True, has22([1, 2, 2]))
    def test1(self):
        self.assertEqual(False, has22([1, 2, 1, 2]))
    def test2(self):
        self.assertEqual(False, has22([2, 1, 2]))
    def test3(self):
        self.assertEqual(True, has22([2, 2, 1, 2]))
    def test4(self):
        self.assertEqual(False, has22([1, 3, 2]))
    def test5(self):
        self.assertEqual(True, has22([1, 3, 2, 2]))
    def test6(self):
        self.assertEqual(True, has22([2, 3, 2, 2]))
    def test7(self):
        self.assertEqual(True, has22([4, 2, 4, 2, 2, 5]))
    def test8(self):
        self.assertEqual(False, has22([1, 2]))
    def test9(self):
        self.assertEqual(True, has22([2, 2]))
    def test10(self):
        self.assertEqual(False, has22([2]))
    def test11(self):
        self.assertEqual(False, has22([]))
    def test12(self):
        self.assertEqual(True, has22([3, 3, 2, 2]))
    def test13(self):
        self.assertEqual(False, has22([5, 2, 5, 2]))
if __name__=='__main__':
    unittest.main()