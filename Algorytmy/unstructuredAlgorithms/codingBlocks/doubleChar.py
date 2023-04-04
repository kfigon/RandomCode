import unittest

# Given a string, return a string where for every char in the original, there are two chars.

def double_char(str):
    out = ""
    ile = 2
    for c in str:
        for _ in range(ile):
            out += c

    return out

class TestTestDoubleChar(unittest.TestCase):
    def test0(self):
        self.assertEqual('TThhee', double_char('The'))
    def test1(self):
        self.assertEqual('AAAAbbbb', double_char('AAbb'))
    def test2(self):
        self.assertEqual('HHii--TThheerree', double_char('Hi-There'))
    def test3(self):
        self.assertEqual('WWoorrdd!!', double_char('Word!'))
    def test4(self):
        self.assertEqual('!!!!', double_char('!!'))
    def test5(self):
        self.assertEqual('', double_char(''))
    def test6(self):
        self.assertEqual('aa', double_char('a'))
    def test7(self):
        self.assertEqual('..', double_char('.'))
    def test8(self):
        self.assertEqual('aaaa', double_char('aa'))

if __name__=='__main__':
    unittest.main()