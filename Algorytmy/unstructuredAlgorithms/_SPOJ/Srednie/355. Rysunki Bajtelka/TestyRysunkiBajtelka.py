from RysunkiBajtelka import liczWszystko

__author__ = 'kamil'

import unittest


class Rysunki(unittest.TestCase):
    def test1(self):
        czarne = [1, 2, 2, 1, 2, 2, 1, 2]
        szare = [0, 2, 3, 0, 2, 3, 0, 2]
        self.assertEqual(liczWszystko(czarne, szare), 23)

    def test2(self):
        czarne = [2, 3, 5, 2, 3, 3, 5, 4, 2, 3]
        szare = [1, 5, 1, 3, 5, 0, 3, 2, 5, 1,
                 6, 2, 4, 3, 6, 3, 6, 4, 7, 4,
                 7, 1, 6, 1, 6, 0, 8, 0, 8, 5,
                 1, 5]
        self.assertEqual(liczWszystko(czarne, szare), 139)

if __name__ == '__main__':
    unittest.main()
