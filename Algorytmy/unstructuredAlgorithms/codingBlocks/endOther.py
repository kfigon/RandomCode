import unittest

'''
Given two strings, return True if either of the strings appears at 
the very end of the other string, ignoring upper/lower case differences 
(in other words, the computation should not be "case sensitive"). 
Note: s.lower() returns the lowercase version of a string.
'''
def end_other(a, b):
    return a[(len(a)-len(b)):].lower() == b.lower() or b[(len(b)-len(a)):].lower() == a.lower()

class TestEndOther(unittest.TestCase):
    def test0(self):
        self.assertEqual(True, end_other('Hiabc', 'abc'))
    def test1(self):
        self.assertEqual(True, end_other('AbC', 'HiaBc'))
    def test2(self):
        self.assertEqual(True, end_other('abc', 'abXabc'))
    def test3(self):
        self.assertEqual(False, end_other('Hiabc', 'abcd'))
    def test4(self):
        self.assertEqual(True, end_other('Hiabc', 'bc'))
    def test5(self):
        self.assertEqual(False, end_other('Hiabcx', 'bc'))
    def test6(self):
        self.assertEqual(True, end_other('abc', 'abc'))
    def test7(self):
        self.assertEqual(True, end_other('xyz', '12xyz'))
    def test8(self):
        self.assertEqual(False, end_other('yz', '12xz'))
    def test9(self):
        self.assertEqual(True, end_other('Z', '12xz'))
    def test10(self):
        self.assertEqual(True, end_other('12', '12'))
    def test11(self):
        self.assertEqual(False, end_other('abcXYZ', 'abcDEF'))
    def test12(self):
        self.assertEqual(False, end_other('ab', 'ab12'))
    def test13(self):
        self.assertEqual(True, end_other('ab', '12ab'))
if __name__=='__main__':
    unittest.main()