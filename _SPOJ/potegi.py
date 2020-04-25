# Dla danych dwóch liczb naturalnych a i b, wyznaczyć ostatnią cyfrę liczby a^b.
import unittest

def exponential(a: int, b:int) -> int:
    return (a**b) % 10

def cleverExp(a:int, b:int)-> int:
    jednosc = a % 10
    if jednosc == 0 or jednosc == 1 or jednosc == 5 or jednosc == 6:
        return jednosc

    lookups = {2: [2,4,8,6],
    3: [3,9,7,1],
    4: [4,6],
    7: [7,9,3,1],
    8: [8,4,2,6],
    9: [9,1]}
    lookup = lookups[jednosc]
    idx = (b-1) % len(lookup)
    return lookup[idx]

class TestFoo(unittest.TestCase):
    def test(self):
        case = [(1,2,1), (2,2,4), (2,3,8),(3,3,7),(4,2,6),(8,4,6),(9,3,9)]
        for c in case:
            with self.subTest(name=str(c)):
                self.assertEqual(c[2], exponential(c[0],c[1]))
                self.assertEqual(c[2], cleverExp(c[0],c[1]))

    def testStress(self):
        for a in range(1, 101):
            for b in range(1, 101):
                self.assertEqual(exponential(a,b), cleverExp(a,b))
                
if __name__ == "__main__":
    unittest.main()
