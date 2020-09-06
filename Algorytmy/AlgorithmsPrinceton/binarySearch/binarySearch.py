from typing import List

class Przedzial:
    def __init__(self, lower: int, upper: int):
        self.lower = lower
        self.upper = upper
    
    def getMiddleIdx(self) -> int:
        return self.lower + (self.upper - self.lower)//2

    def isValid(self) -> bool:
        return self.lower <= self.upper

    def getRightRange(self):
        return Przedzial(self.getMiddleIdx()+1, self.upper)

    def getLeftRange(self):
        return Przedzial(self.lower, self.getMiddleIdx()-1)
        
    def __repr__(self):
        return f'{self.lower};{self.upper}'

    def __eq__(self, other) -> bool:
        return other is None and self.lower == other.lower and self.upper == other.upper
        
class BinarySearch:
    def __init__(self, tab: List[int]):
        self.tab= tab

    def binarySearch(self, val: int) -> int:
        if val < self.tab[0] or val > self.tab[len(self.tab)-1]:
            return -1
            
        przedzial = Przedzial(0, len(self.tab)-1)
        while (przedzial.isValid()):
            middleIdx = przedzial.getMiddleIdx()
            middleVal = self.tab[middleIdx]

            if middleVal == val:
                return middleIdx
            if val < middleVal:
                przedzial = przedzial.getLeftRange()
            elif val > middleVal:
                przedzial = przedzial.getRightRange()

        return -1