import unittest
from typing import List
from random import Random
from datetime import datetime

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


class Test(unittest.TestCase):
    def doTest(self, algorithm):
        res : List[int] = algorithm.findThreeSums([30,-40,-20,-10,40,0,10,5])
        self.assertEqual(4, len(res))
        for i in res:
            self.assertEqual(0, sum(i))

    def test1(self):
        self.doTest(BruteForce())


if __name__ == "__main__":
    unittest.main()

    def measure(algo: ThreeSumBase, inputTableSize: int):
        r = Random()
        tab: List[int] = [r.randint(-20, 20) for _ in range(inputTableSize)]
        
        start = datetime.now()
        res = algo.findThreeSums(tab)
        duration = datetime.now() - start

        print(f'took: {duration}')
        print(f'result size: {len(res)}')

    # measure(BruteForce(), 100)