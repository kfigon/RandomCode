import unittest
from code import *

class TestParsing(unittest.TestCase):
	def test1(self):
		self.fail('todo')

class Test(unittest.TestCase):
	def test1(self):
		matrix = [[5,3,4],[1,5,8],[6,4,2]]
		got, _ = createMagicSquare(matrix)
		expectedMagicSquare = [[8,3,4],[1,5,9],[6,7,2]]
		self.assertEqual(got, expectedMagicSquare)

	def testCost(self):
		cases = [
			([[4,9,2], [3,5,7], [8,1,5]], 1),
			([[4,8,2], [4,5,7], [6,1,1]], 4),
			([[5,3,4],[1,5,8],[6,4,2]], 7),
		]
		for i,c in enumerate(cases):
			with self.subTest(i):
				got = createMagicSquare(c[0])
				self.assertEqual(got, c[1])

if __name__ == '__main__':
	unittest.main()