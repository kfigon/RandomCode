import unittest

'''
Return the sum of the numbers in the array, returning 0 for an empty array. 
Except the number 13 is very unlucky, so it does not count and 
numbers that come immediately after a 13 also do not count.
'''
def sum13(nums):
    suma = 0
    skipNext = False
    for i in nums:
        if skipNext:
            skipNext = False
        elif i == 13:
            skipNext = True
        else:
            suma +=i
    return suma

class TestSum13(unittest.TestCase):
    def test0(self):
        self.assertEqual(6, sum13([1, 2, 2, 1]))
    def test1(self):
        self.assertEqual(2, sum13([1, 1]))
    def test2(self):
        self.assertEqual(6, sum13([1, 2, 2, 1, 13]))
    def test3(self):
        self.assertEqual(4, sum13([1, 2, 13, 2, 1, 13]))
    def test4(self):
        self.assertEqual(3, sum13([13, 1, 2, 13, 2, 1, 13]))
    def test5(self):
        self.assertEqual(0, sum13([]))
    def test6(self):
        self.assertEqual(0, sum13([13]))
    def test7(self):
        self.assertEqual(0, sum13([13, 13]))
    def test8(self):
        self.assertEqual(0, sum13([13, 0, 13]))
    def test9(self):
        self.assertEqual(0, sum13([13, 1, 13]))
    def test10(self):
        self.assertEqual(14, sum13([5, 7, 2]))
    def test11(self):
        self.assertEqual(5, sum13([5, 13, 2]))
    def test12(self):
        self.assertEqual(0, sum13([0]))
    def test13(self):
        self.assertEqual(0, sum13([13, 0]))
if __name__=='__main__':
    unittest.main()