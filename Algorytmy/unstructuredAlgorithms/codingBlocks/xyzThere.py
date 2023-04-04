import unittest

'''
Return True if the given string contains an appearance of "xyz" 
where the xyz is not directly preceeded by a period (.). 
So "xxyz" counts but "x.xyz" does not.
'''

def xyz_there(str):
    for i in reversed(range(len(str))):
        if(str[i] =='z' and str[i-1]=='y' and str[i-2]=='x' and str[i-3] != '.'):
            return True
    return False

class TestXyzThere(unittest.TestCase):
    def test0(self):
        self.assertEqual(True, xyz_there('abcxyz'))
    def test1(self):
        self.assertEqual(False, xyz_there('abc.xyz'))
    def test2(self):
        self.assertEqual(True, xyz_there('xyz.abc'))
    def test3(self):
        self.assertEqual(False, xyz_there('abcxy'))
    def test4(self):
        self.assertEqual(True, xyz_there('xyz'))
    def test5(self):
        self.assertEqual(False, xyz_there('xy'))
    def test6(self):
        self.assertEqual(False, xyz_there('x'))
    def test7(self):
        self.assertEqual(False, xyz_there(''))
    def test8(self):
        self.assertEqual(True, xyz_there('abc.xyzxyz'))
    def test9(self):
        self.assertEqual(True, xyz_there('abc.xxyz'))
    def test10(self):
        self.assertEqual(False, xyz_there('.xyz'))
    def test11(self):
        self.assertEqual(False, xyz_there('12.xyz'))
    def test12(self):
        self.assertEqual(True, xyz_there('12xyz'))
    def test13(self):
        self.assertEqual(False, xyz_there('1.xyz.xyz2.xyz'))
if __name__=='__main__':
    unittest.main()