import unittest
from code import *

class Test(unittest.TestCase):
	def testCost(self):
		cases = [
			([[4,9,2], [3,5,7], [8,1,5]], 1),
			([[4,8,2], [4,5,7], [6,1,1]], 9),
			([[5,3,4],[1,5,8],[6,4,2]], 7),
			([[4,5,8],[2,4,1],[1,9,7]], 14),
		]

		for i,c in enumerate(cases):
			with self.subTest(i):
				got = createMagicSquare(c[0])
				self.assertEqual(got, c[1])

if __name__ == '__main__':
	unittest.main()