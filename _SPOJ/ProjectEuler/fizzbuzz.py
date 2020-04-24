import unittest
from typing import List

def isDivisible(x: int, divisors: List[int]) -> bool:
    for div in divisors:
        if x % div == 0:
            return True
    return False

#extensible fizzbuzz
def fizzbuzz(x: int) -> str:
    out =''
    if isDivisible(x, [3]):
        out +='Fizz'
    if isDivisible(x, [5]):
        out += 'Buzz'
    
    if len(out) == 0:
        return str(x)

    return out

class FizzbuzzTest(unittest.TestCase):
    def test(self):
        case = [
            (1, '1'),
            (2, '2'),
            (3, 'Fizz'),
            (4, '4'),
            (5, 'Buzz'),
            (6, 'Fizz'),
            (7, '7'),
            (8, '8'),
            (9, 'Fizz'),
            (10, 'Buzz'),
            (11, '11'),
            (12, 'Fizz'),
            (13, '13'),
            (14, '14'),
            (15, 'FizzBuzz'),
            (16, '16'),
            (17, '17')
        ]
        for x in case:
            with self.subTest(name=str(x[0])):
                self.assertEqual(x[1], fizzbuzz(x[0]))

if __name__ == "__main__":
    unittest.main()