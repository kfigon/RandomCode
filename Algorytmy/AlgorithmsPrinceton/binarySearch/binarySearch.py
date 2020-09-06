from typing import List
import logging

class Przedzial:
    def __init__(self, lower: int, upper: int):
        assert lower <= upper, f'invalid values: low: {lower}, up: {upper}'
        self.lower = lower
        self.upper = upper
    
    def getMiddleIdx(self) -> int:
        return (self.lower+self.upper)//2

    def isSingle(self) -> bool:
        return self.lower == self.upper

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
            
        logging.info(f'starting to find {val}')
        przedzial = Przedzial(0, len(self.tab))
        while (True):
            middleIdx = przedzial.getMiddleIdx()
            middleVal = self.tab[middleIdx]
            if middleVal == val:
                logging.info(f'found! {middleIdx}')
                return middleIdx

            if przedzial.isSingle():
                return -1

            if val < middleVal:
                przedzial = przedzial.getLeftRange()
                logging.info(f'go left, new range: <{przedzial}> middle:{middleVal}, val: {val}')
            else:
                przedzial = przedzial.getRightRange()
                logging.info(f'go right, new range: <{przedzial}> middle:{middleVal}, val: {val}')

        raise Exception("something went wrong") 