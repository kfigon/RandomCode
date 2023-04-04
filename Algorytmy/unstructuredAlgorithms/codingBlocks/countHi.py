import unittest

# Return the number of times that the string "hi" appears anywhere in the given string.

def count_hi(str):
    # return str.count("hi")
    
    ile = 0
    dl = len(str)
    for i in range(dl-1):
        if(str[i] == 'h' and str[i+1] == 'i'):
            ile+=1

    return ile

class TestTestCountHi(unittest.TestCase):
    def test0(self):
        self.assertEqual(1, count_hi('abc hi ho'))
    def test1(self):
        self.assertEqual(2, count_hi('ABChi hi'))
    def test2(self):
        self.assertEqual(2, count_hi('hihi'))
    def test3(self):
        self.assertEqual(2, count_hi('hiHIhi'))
    def test4(self):
        self.assertEqual(0, count_hi(''))
    def test5(self):
        self.assertEqual(0, count_hi('h'))
    def test6(self):
        self.assertEqual(1, count_hi('hi'))
    def test7(self):
        self.assertEqual(0, count_hi('Hi is no HI on ahI'))
    def test8(self):
        self.assertEqual(2, count_hi('hiho not HOHIhi'))
if __name__=='__main__':
    unittest.main()