import unittest
import math

def reverseDigits(x: int) -> int:
    out = 0
    wasNegative = x < 0
    x = abs(x)
    while x != 0:
        dig = x % 10
        out = out*10 + dig
        x //= 10

    return -out if wasNegative else out

def isPalindrome(x: int) -> bool:
    if x < 0:
        return False
    elif x == 0:
        return True

    numerOfDigits = math.ceil(math.log10(x))
    for _ in range(numerOfDigits // 2):
        msd = x // 10**(numerOfDigits-1)
        lsd = x % 10
        if msd != lsd:
            return False
        x -= msd*(10**(numerOfDigits-1))
        x //= 10
        numerOfDigits -=2
    return True

class TestPrimitives(unittest.TestCase):
    def testReverseDigits(self):
        data = [
            (123, 321),
            (1, 1),
            (-987, -789),
            (123456789, 987654321),
        ]
        for d in data:
            with self.subTest(f'{d}'):
                self.assertEqual(d[0], reverseDigits(d[1]))
                self.assertEqual(d[1], reverseDigits(d[0]))

    def testIsPalindrome(self):
        data = [
            (123, False),
            (321, False),
            (-123, False),
            (-121, False),
            (21, False),
            (1321, False),
            (0, True),
            (1, True),
            (121, True),
            (22, True),
            (88, True),
            (12321, True),
            (1441, True),
            (123454321, True),
        ]
        for d in data:
            with self.subTest(f'{d}'):
                self.assertEqual(isPalindrome(d[0]), d[1])
                # self.assertEqual(reverseDigits(d[0]) == d[0], d[1]) # + acknowledge negative numbers

if __name__ == '__main__':
    unittest.main()