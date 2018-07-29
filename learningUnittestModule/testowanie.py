import unittest
from unittest.mock import MagicMock

class Foo:
    def exceptionThrower(self, argument):
        raise ValueError()

class Test(unittest.TestCase):

    def setUp(self):
        pass
    def tearDown(self):
        pass
    def test(self):
        self.assertTrue(True)
        self.assertEqual(1, 1)

    def testException(self):
        f = Foo()
        argument = 123
        self.assertRaises(ValueError, f.exceptionThrower, argument)
    
    @unittest.expectedFailure
    def testException2(self):
        f = Foo()
        f.exceptionThrower(123)

    @unittest.skip("something wrong!")
    def testSkip(self):
        self.assertTrue(False)


class TestMockowania(unittest.TestCase):
    def testReturna(self):
        mok = MagicMock(return_value = 3)
        self.assertEqual(3, mok())
    
    def testWywolania(self):
        mok = MagicMock(return_value = 3)
        mok(1,3,43, 'jakis parameter')
        mok.assert_called_with(1, 3, 43, 'jakis parameter')

    def testWyjatku(self):
        mok = MagicMock(side_effect=ValueError('oooo'))
        self.assertRaises(ValueError, mok)
    
    def testPodmiany(self):
        mok = MagicMock(side_effect = (lambda x: x.append(123)))
        tab = [1,2,3]

        mok(tab)
        self.assertEqual([1,2,3,123], tab)

    def testPodmiany2(self):
        f = Foo()
        f.exceptionThrower = MagicMock(side_effect = (lambda x: x))
        f.exceptionThrower(123)


if __name__ == '__main__':
    unittest.main()