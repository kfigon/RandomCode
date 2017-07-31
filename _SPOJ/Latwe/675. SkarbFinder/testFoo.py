__author__ = 'kamil'

import unittest
from foo import foo
from foo import punktNaInstrukcje
from foo import Punkt

class MyTestCase(unittest.TestCase):
    def test_1(self):
        self.assertEqual(
            [
            [0, 1],
            [3, 1]
            ],
            foo([
            [1, 1],
            [0, 2],
            [3, 1],
        ]))
    def test_2(self):
        self.assertEqual("studnia",
                        foo([
                        [0, 1],
                        [2, 1],
                        [1, 1],
                        [3, 1]]))

    def test_3(self):
        self.assertEqual([[0,3]],
                                foo([
                                [0, 1],
                                [0, 2]]))

    def test_translacji_2_2(self):
        self.assertEqual([
            [0, 2],
            [3, 2]],
            punktNaInstrukcje(Punkt(2, 2)))
if __name__ == '__main__':
    unittest.main()
