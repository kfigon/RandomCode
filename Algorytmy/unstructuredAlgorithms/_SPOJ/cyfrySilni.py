import unittest
from typing import List, Tuple

def factorial(x: int) -> int:
    if x == 0:
        return 1
    return x * factorial(x-1)

def factorialIter(x: int) -> int:
    if x < 2:
        return 1
    out = 1
    for i in range(1,x+1):
        out *= i
    return out

# zwroc cyfre dziesiatek i cyfre jednosci z silni
def factorialDigits(x: int)-> Tuple[int, int]:
    fact = factorialIter(x)
    jednosci = fact % 10
    dziesiatki = ((fact - jednosci)//10) % 10
    return (dziesiatki, jednosci)

def factorialDigitsClever(x: int) -> Tuple[int, int]:
    lookup = [(0,1),(0,1),(0,2),(0,6),(2,4),(2,0), (2,0),(4,0),(2,0),(8,0)]
    if x < len(lookup):
        return lookup[x]
    return (0,0) 

class TestFoo(unittest.TestCase):
    def testFactorial(self):
        case = [(0,1),(1,1), (2,2),(3,6),(4,24),(5,120),(6,720),(7,5040),(8,40320),(9,362880),(10,3628800),(11,39916800), (20, 2432902008176640000)]
        for c in case:
            with self.subTest(name=str(c)):
                self.assertEqual(c[1], factorial(c[0]))
                self.assertEqual(c[1], factorialIter(c[0]))

    def testDigitsOfFactorial(self):
        case = [(0,(0,1)), (1,(0,1)), (2,(0,2)),(3,(0,6)),
        (4,(2,4)),(5,(2,0)), (6,(2,0)), (7,(4,0)),
        (8,(2,0)), (9,(8,0)), (10,(0,0)), (11,(0,0)),
        (12, (0,0)), (13, (0,0)), (14, (0,0)), (15, (0,0)),
        (16, (0,0)), (17, (0,0)),
        (18, (0,0)), (19, (0,0)),(20, (0,0))]
        for c in case:
            with self.subTest(name=str(c)):
                self.assertEqual(c[1], factorialDigits(c[0]))
                self.assertEqual(c[1], factorialDigitsClever(c[0]))


if __name__ == "__main__":
    unittest.main()