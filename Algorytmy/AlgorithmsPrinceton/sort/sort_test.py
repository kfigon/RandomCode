import unittest
from typing import List

class BaseSort:
    def sort(self, tab: List[int]) -> List[int]:
        raise Exception('not implemented')
    
class SelectionSort(BaseSort):
    def sort(self, tab: List[int]) -> List[int]:
        # quadratic performance - always!
        dl = len(tab)
        for i in range(dl):
            smallestIdx = i
            for j in range(smallestIdx+1, dl):
                if tab[j] < tab[smallestIdx]:
                    smallestIdx = j

            tmp = tab[i]
            tab[i] = tab[smallestIdx]
            tab[smallestIdx] = tmp
        return tab

class InsertionSort(BaseSort):
    def sort(self, tab: List[int]) -> List[int]:
        # liniowo gdy juz posortowana!
        for i in range(len(tab)):
            j = i
            prev = j-1
            while (j > 0 and tab[j] < tab[prev]):
                tab[j], tab[prev] = tab[prev], tab[j]
                j -= 1
                prev-=1

        return tab

class ShellSort(BaseSort):
    def sort(self, tab: List[int]) -> List[int]:
        return tab

class SortTest(unittest.TestCase):

    def doSort(self, bs: BaseSort):
        for ar in self.getTestArrays():
            ar, exp = ar
            res: List[int] = bs.sort(ar)
            self.assertEqual(exp, res)

    def getTestArrays(self):
        return[
            ([7, 10, 5,3,8,4,2,9,6], [2,3,4,5,6,7,8,9,10]),
            ([20,7,2, 10, 5,3,-1,8,4,3,2,9,6,20], [-1,2,2,3,3,4,5,6,7,8,9,10,20,20])
        ]

    def testSelection(self):
        self.doSort(SelectionSort())
    
    def testInsertionSort(self):
        self.doSort(InsertionSort())

    def testShellSort(self):
        self.doSort(ShellSort())

if __name__ == "__main__":
    unittest.main()