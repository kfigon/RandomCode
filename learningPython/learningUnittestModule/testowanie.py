import unittest

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

    def testRegex(self):
        self.assertRegex('some random text', 'same')

if __name__ == '__main__':
    unittest.main()