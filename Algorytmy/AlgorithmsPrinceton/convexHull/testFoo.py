import unittest
from convexHull import *

class Testy(unittest.TestCase):
    def testCounterClockwise(self):
        pts = [Point(, ), Point(, ),Point(, )]
        self.assertTrue(isCounterClockwise(*pts))

if __name__ == "__main__":
    unittest.main()