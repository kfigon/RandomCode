__author__ = 'kamil'

import unittest
from Decoder import DecoderX

class DecoderTester(unittest.TestCase):
    def test_1(self):
        decoder = DecoderX()
        result=""

        result += decoder.feed(18)
        result += decoder.feed(12312)
        result += decoder.feed(171)
        result += decoder.feed(763)
        result += decoder.feed(98423)
        result += decoder.feed(1208)

        result += decoder.feed(216)
        result += decoder.feed(11)
        result += decoder.feed(500)
        result += decoder.feed(18)
        result += decoder.feed(241)
        result += decoder.feed(0)
        result += decoder.feed(32)
        result += decoder.feed(20620)
        result += decoder.feed(27)
        result += decoder.feed(10)
        self.assertEqual("Right? Yes!", result)


if __name__ == '__main__':
    unittest.main()
