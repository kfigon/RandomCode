import unittest
from lista import Lista

class TestListy(unittest.TestCase):
    def setUp(self):
        self.l=Lista()

    def tearDown(self):
        self.l.clear()

    def testPusta(self):
        self.assertTrue(self.l.isEmpty())
        self.assertEqual(0, self.l.getSize())

    def testAdd(self):
        self.l.add(5)

        self.assertFalse(self.l.isEmpty())
        self.assertEqual(1, self.l.getSize())
        self.assertEqual(5, self.l.get(0))
        self.assertRaises(IndexError, self.l.get, 1)

    def testAddFew(self):
        self.l.add(5)
        self.l.add(1)
        self.l.add(0)

        self.assertFalse(self.l.isEmpty())
        self.assertEqual(3, self.l.getSize())
        self.assertEqual(5, self.l.get(0))
        self.assertEqual(1, self.l.get(1))
        self.assertEqual(0, self.l.get(2))
        self.assertRaises(IndexError, self.l.get, 3)

    def testClearWhenEmpty(self):
        self.l.clear()
        self.assertTrue(self.l.isEmpty())
        self.assertEqual(0, self.l.getSize())
        self.assertRaises(IndexError, self.l.get, 0)

    def testClearNotEmpty2(self):
        self.l.add(5)
    
        self.l.clear()
        self.assertTrue(self.l.isEmpty())
        self.assertEqual(0, self.l.getSize())
        self.assertRaises(IndexError, self.l.get, 0)
        self.assertRaises(IndexError, self.l.get, 1)

    def testClearNotEmpty3(self):
        self.l.add(5)
        self.l.add(3)        

        self.l.clear()
        self.assertTrue(self.l.isEmpty())
        self.assertEqual(0, self.l.getSize())
        self.assertRaises(IndexError, self.l.get, 0)
        self.assertRaises(IndexError, self.l.get, 1)

if __name__ == '__main__':
    unittest.main()