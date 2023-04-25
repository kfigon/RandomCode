import unittest
import math
from typing import List

class TestStr(unittest.TestCase):
    def testIntToStr(self):
        data = [
            (123, '123'),
            (2, '2'),
            (23, '23'),
            (12345, '12345'),
        ]
        for d in data:
            with self.subTest(d[0]):
                self.assertEqual(d[1], intToStr(d[0]))

    def testStrToInt(self):
            data = [
                (123, '123'),
                (2, '2'),
                (23, '23'),
                (12345, '12345'),
            ]
            for d in data:
                with self.subTest(d[0]):
                    self.assertEqual(d[0], strToInt(d[1]))

def intToStr(v: int) -> str:
    out = ''
    powerOfTen = int(math.log10(v))
    while v != 0:
        a = 10**powerOfTen
        msd = int(v/a)
        out += str(msd)
        v = v - msd*a
        powerOfTen-=1

    return out

def strToInt(v: str) -> int:
    out = 0
    powerOfTen = len(v)-1
    for d in v:
        out = out + int(d)*10**powerOfTen
        powerOfTen -= 1
    return out

if __name__ == '__main__':
    unittest.main()