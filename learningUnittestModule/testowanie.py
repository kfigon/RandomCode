import unittest

class Foo:
    def exceptionThrower(self, argument):
        raise ValueError()

class Test(unittest.TestCase):
    def test(self):
        self.assertTrue(True)
        self.assertEqual(1, 1)

    def testException(self):
        f = Foo()
        argument = 123
        self.assertRaises(ValueError, f.exceptionThrower, argument)



if __name__ == '__main__':
    unittest.main()