import unittest

# return true if 'cat' and 'dog' are present same number of times in str
def cat_dog(str):
    return str.count('cat') == str.count('dog')

class TestTestCatDog(unittest.TestCase):
    def test0(self):
        self.assertEqual(True, cat_dog('catdog'))
    def test1(self):
        self.assertEqual(False, cat_dog('catcat'))
    def test2(self):
        self.assertEqual(True, cat_dog('1cat1cadodog'))
    def test3(self):
        self.assertEqual(False, cat_dog('catxxdogxxxdog'))
    def test4(self):
        self.assertEqual(True, cat_dog('catxdogxdogxcat'))
    def test5(self):
        self.assertEqual(False, cat_dog('catxdogxdogxca'))
    def test6(self):
        self.assertEqual(False, cat_dog('dogdogcat'))
    def test7(self):
        self.assertEqual(True, cat_dog('dogogcat'))
    def test8(self):
        self.assertEqual(False, cat_dog('dog'))
    def test9(self):
        self.assertEqual(False, cat_dog('cat'))
    def test10(self):
        self.assertEqual(True, cat_dog('ca'))
    def test11(self):
        self.assertEqual(True, cat_dog('c'))
    def test12(self):
        self.assertEqual(True, cat_dog(''))
if __name__=='__main__':
    unittest.main()