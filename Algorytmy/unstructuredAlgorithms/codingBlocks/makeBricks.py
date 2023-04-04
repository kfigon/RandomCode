'''
We want to make a row of bricks that is goal inches long. We have a number
 of small bricks (1 inch each) and big bricks (5 inches each). 
 Return True if it is possible to make the goal by choosing from the given bricks. 
 This is a little harder than it looks and can be done without any loops.

makeBricks(3, 1, 8) → True
makeBricks(3, 1, 9) → False
makeBricks(3, 2, 10) → True
'''


import unittest


def makeBricks(short, long, goal):
    ileDlugichTrzeba = goal//5
    if ileDlugichTrzeba >= long:
        return long*5 + short >= goal
    else:
        return ileDlugichTrzeba*5 + short >= goal


class TestTestBricks(unittest.TestCase):
    def test0(self):
        self.assertTrue(makeBricks(3, 1, 8))
    def test1(self):
        self.assertFalse(makeBricks(3, 1, 9))
    def test2(self):
        self.assertTrue(makeBricks(3, 2, 10))
    def test3(self):
        self.assertTrue(makeBricks(3, 2, 8))
    def test4(self):
        self.assertFalse(makeBricks(3, 2, 9))
    def test5(self):
        self.assertTrue(makeBricks(6, 1, 11))
    def test6(self):
        self.assertFalse(makeBricks(6, 0, 11))
    def test7(self):
        self.assertTrue(makeBricks(1, 4, 11))
    def test8(self):
        self.assertTrue(makeBricks(0, 3, 10))
    def test9(self):
        self.assertFalse(makeBricks(1, 4, 12))
    def test10(self):
        self.assertTrue(makeBricks(3, 1, 7))
    def test11(self):
        self.assertFalse(makeBricks(1, 1, 7))
    def test12(self):
        self.assertTrue(makeBricks(2, 1, 7))
    def test13(self):
        self.assertTrue(makeBricks(7, 1, 11))
    def test14(self):
        self.assertTrue(makeBricks(7, 1, 8))
    def test15(self):
        self.assertFalse(makeBricks(7, 1, 13))
    def test16(self):
        self.assertTrue(makeBricks(43, 1, 46))
    def test17(self):
        self.assertFalse(makeBricks(40, 1, 46))
    def test18(self):
        self.assertTrue(makeBricks(40, 2, 47))
    def test19(self):
        self.assertTrue(makeBricks(40, 2, 50))
    def test20(self):
        self.assertFalse(makeBricks(40, 2, 52))
    def test21(self):
        self.assertFalse(makeBricks(22, 2, 33))
    def test22(self):
        self.assertTrue(makeBricks(0, 2, 10))
    def test23(self):
        self.assertTrue(makeBricks(1000000, 1000, 1000100))
    def test24(self):
        self.assertFalse(makeBricks(2, 1000000, 100003))
    def test25(self):
        self.assertTrue(makeBricks(20, 0, 19))
    def test26(self):
        self.assertFalse(makeBricks(20, 0, 21))
    def test27(self):
        self.assertFalse(makeBricks(20, 4, 51))
    def test28(self):
        self.assertTrue(makeBricks(20, 4, 39))


if __name__ == '__main__':
    unittest.main()