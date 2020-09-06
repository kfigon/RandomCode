import unittest
from typing import List
from random import Random
from datetime import datetime
from binarySearch.binarySearch import BinarySearch

class ThreeSumBase:
    def findThreeSums(self, tab: List[int]) -> List[List[int]]:
        raise Exception('Not implemented')


class BruteForce(ThreeSumBase):
    def findThreeSums(self, tab: List[int]) -> List[List[int]]:
        out: List[List[int]] = []
        # kombinacja bez powtorzen
        for i in range(len(tab)):
            for j in range(i+1, len(tab)):
                for k in range(j+1, len(tab)):
                    if tab[i] + tab[j] + tab[k] == 0:
                        out.append([tab[i],tab[j], tab[k]])
        return out

class SortingSolution(ThreeSumBase):
    def findThreeSums(self, tab: List[int]) -> List[List[int]]:
        out: List[List[int]] = []
        tab.sort()
        bs = BinarySearch(tab)
        for i in range(len(tab)):
            for j in range(len(tab)):
                if i == j:
                    continue

                toSearch: int = -(tab[i]+tab[j])
                idx = bs.binarySearch(toSearch)
                # might double output
                if idx != -1 and idx != i and idx != j:
                    out.append([tab[i], tab[j], tab[idx]])
        return out

class Test(unittest.TestCase):
    def doTest(self, algorithm):
        res : List[int] = algorithm.findThreeSums([30,-40,-20,-10,40,0,10,5])
        for i in res:
            self.assertEqual(0, sum(i))

    def test1(self):
        self.doTest(BruteForce())

    def test2(self):
        self.doTest(SortingSolution())

if __name__ == "__main__":
    unittest.main()

    def measure(algo: ThreeSumBase, tab: List[int]):
        start = datetime.now()
        res = algo.findThreeSums(tab)
        duration = datetime.now() - start

        print(f'{type(algo).__name__} -> took: {duration}')
        print(f'result size: {len(res)}')

    inputTableSize = 100
    r = Random()
    tab: List[int] = [r.randint(-20, 20) for _ in range(inputTableSize)]

    measure(BruteForce(), tab)
    measure(SortingSolution(), tab)