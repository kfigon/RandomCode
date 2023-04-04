import unittest

class TestFoo(unittest.TestCase):
    def testBar(self):
        self.assertTrue(True)

if __name__ == 'main':
    unittest.main()