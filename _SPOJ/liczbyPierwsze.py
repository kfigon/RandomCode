import unittest
from typing import List
import math

def isPrime(x: int) -> bool:
    if x < 2:
        raise Exception(f'invalid number {x}')

    sito : List[bool] = [True for _ in range(x+1)]
    sito[0] = False
    sito[1] = False
    
    boundary: float = math.sqrt(x)
    
    for j in range(int(boundary)+1):
        if sito[j] == False:
            continue
        for i in range(j, len(sito), j):
            sito[i] = False

    return sito[x]

class TestFoo(unittest.TestCase):
    def testPrime(self):
        case = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
        for c in case:
            with self.subTest(name=str(c)):
                self.assertTrue(isPrime(c))

    def testNotPrime(self):
        case = [4,6,8,9,10,12,14,15,16,18,20,21,22,24,25,26,27,28,30,32,33,34,35,36,38,39,40]
        for c in case:
            with self.subTest(name=str(c)):
                self.assertFalse(isPrime(c))

if __name__ == "__main__":
    unittest.main()