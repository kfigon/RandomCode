__author__ = 'kamil'

import unittest
from foo import foo

# W tablicy n liczb całkowitych dodatnich
# znajdź tę, której wartość jest najbliższa
# warości średniej z wszystkich liczb.
class MyTestCase(unittest.TestCase):
    def test_1(self):
        self.assertEqual(3, foo([4, 1, 2, 3, 4]))
    def test_2(self):
        self.assertEqual(3, foo([4, 4, 3, 2, 1]))
    def test_3(self):
        self.assertEqual(3, foo([4, 0, 3, 2, 4]))

if __name__ == '__main__':
    unittest.main()
