import unittest

''' Return the number of times that the string "code" appears 
anywhere in the given string, except we'll accept
 any letter for the 'd', so "cope" and "cooe" count.'''

def count_code(str):
    ile = 0

    for i in range(len(str)-3):
        if(str[i] == 'c' and str[i+1] == 'o' and str[i+3] == 'e'):
            ile +=1

    return ile

class TestTestCountCode(unittest.TestCase):
    def test0(self):
        self.assertEqual(1, count_code('aaacodebbb'))
    def test1(self):
        self.assertEqual(2, count_code('codexxcode'))
    def test2(self):
        self.assertEqual(2, count_code('cozexxcope'))
    def test3(self):
        self.assertEqual(1, count_code('cozfxxcope'))
    def test4(self):
        self.assertEqual(1, count_code('xxcozeyycop'))
    def test5(self):
        self.assertEqual(0, count_code('cozcop'))
    def test6(self):
        self.assertEqual(0, count_code('abcxyz'))
    def test7(self):
        self.assertEqual(1, count_code('code'))
    def test8(self):
        self.assertEqual(0, count_code('ode'))
    def test9(self):
        self.assertEqual(0, count_code('c'))
    def test10(self):
        self.assertEqual(0, count_code(''))
    def test11(self):
        self.assertEqual(3, count_code('AAcodeBBcoleCCccoreDD'))
    def test12(self):
        self.assertEqual(2, count_code('AAcodeBBcoleCCccorfDD'))
    def test13(self):
        self.assertEqual(3, count_code('coAcodeBcoleccoreDD'))
if __name__=='__main__':
    unittest.main()