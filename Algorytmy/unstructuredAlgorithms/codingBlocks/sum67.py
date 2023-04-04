import unittest

'''
Return the sum of the numbers in the array, except ignore sections of 
numbers starting with a 6 and extending to the next 7 
(every 6 will be followed by at least one 7). Return 0 for no numbers.
'''
def sum67(nums):
    suma = 0
    skip = False
    for i in nums:
        if skip and i == 7:
            skip = False
            continue
        elif i == 6:
            skip = True
            
        if not skip:
            suma += i
    return suma

class TestSum67(unittest.TestCase):
    def test0(self):
        self.assertEqual(5, sum67([1, 2, 2]))
    def test1(self):
        self.assertEqual(5, sum67([1, 2, 2, 6, 99, 99, 7]))
    def test2(self):
        self.assertEqual(4, sum67([1, 1, 6, 7, 2]))
    def test3(self):
        self.assertEqual(2, sum67([1, 6, 2, 2, 7, 1, 6, 99, 99, 7]))
    def test4(self):
        self.assertEqual(2, sum67([1, 6, 2, 6, 2, 7, 1, 6, 99, 99, 7]))
    def test5(self):
        self.assertEqual(18, sum67([2, 7, 6, 2, 6, 7, 2, 7]))
    def test6(self):
        self.assertEqual(9, sum67([2, 7, 6, 2, 6, 2, 7]))
    def test7(self):
        self.assertEqual(8, sum67([1, 6, 7, 7]))
    def test8(self):
        self.assertEqual(8, sum67([6, 7, 1, 6, 7, 7]))
    def test9(self):
        self.assertEqual(0, sum67([6, 8, 1, 6, 7]))
    def test10(self):
        self.assertEqual(0, sum67([]))
    def test11(self):
        self.assertEqual(11, sum67([6, 7, 11]))
    def test12(self):
        self.assertEqual(22, sum67([11, 6, 7, 11]))
    def test13(self):
        self.assertEqual(11, sum67([2, 2, 6, 7, 7]))
if __name__=='__main__':
    unittest.main()