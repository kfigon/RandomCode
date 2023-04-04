import unittest

'''
Return the "centered" average of an array of ints, 
which we'll say is the mean average of the values, 
except ignoring the largest and smallest values 
in the array. If there are multiple copies of 
the smallest value, ignore just one copy, and 
likewise for the largest value. 
Use int division to produce the final average. 
You may assume that the array is length 3 or more.
'''
def centered_average(tab):
    tab.sort()
    suma = sum(tab[1:len(tab)-1])
    return suma//(len(tab)-2)

class TestCenteredAverage(unittest.TestCase):
    def test0(self):
        self.assertEqual(3, centered_average([1, 2, 3, 4, 100]))
    def test1(self):
        self.assertEqual(5, centered_average([1, 1, 5, 5, 10, 8, 7]))
    def test2(self):
        self.assertEqual(-3, centered_average([-10, -4, -2, -4, -2, 0]))
    def test3(self):
        self.assertEqual(4, centered_average([5, 3, 4, 6, 2]))
    def test4(self):
        self.assertEqual(4, centered_average([5, 3, 4, 0, 100]))
    def test5(self):
        self.assertEqual(4, centered_average([100, 0, 5, 3, 4]))
    def test6(self):
        self.assertEqual(4, centered_average([4, 0, 100]))
    def test7(self):
        self.assertEqual(3, centered_average([0, 2, 3, 4, 100]))
    def test8(self):
        self.assertEqual(1, centered_average([1, 1, 100]))
    def test9(self):
        self.assertEqual(7, centered_average([7, 7, 7]))
    def test10(self):
        self.assertEqual(7, centered_average([1, 7, 8]))
    def test11(self):
        self.assertEqual(50, centered_average([1, 1, 99, 99]))
    def test12(self):
        self.assertEqual(50, centered_average([1000, 0, 1, 99]))
    def test13(self):
        self.assertEqual(4, centered_average([4, 4, 4, 4, 5]))
    def test14(self):
        self.assertEqual(4, centered_average([4, 4, 4, 1, 5]))
    def test15(self):
        self.assertEqual(6, centered_average([6, 4, 8, 12, 3]))
if __name__=='__main__':
    unittest.main()