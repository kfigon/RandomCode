from typing import List
import logging

class Przedzial:
    def __init__(self, lower: int, upper: int):
        self.lower = lower
        self.upper = upper
    
    def getMiddleIdx(self) -> int:
        return (self.lower+self.upper)//2

    def isSingle(self) -> bool:
        return self.lower == self.upper

    def getRightRange(self):
        return Przedzial(self.getMiddleIdx(), self.upper)

    def getLeftRange(self):
        return Przedzial(self.lower, self.getMiddleIdx())
        
    def __repr__(self):
        return f'{self.lower};{self.upper}'
        
class BinarySearch:
    def __init__(self, tab: List[int]):
        self.tab= tab

    def binarySearch(self, val: int) -> int:
        logging.info(f'starting to find {val}')
        przedzial = Przedzial(0, len(self.tab))
        while (True):
            if przedzial.isSingle():
                return -1

            middleIdx = przedzial.getMiddleIdx()
            middleVal = self.tab[middleIdx]
            if middleVal == val:
                logging.info(f'found! {middleIdx}')
                return middleIdx
            elif val < middleVal:
                logging.info(f'go left middle:{middleVal}, val: {val}')
                przedzial = przedzial.getLeftRange()
            else:
                logging.info(f'go right middle:{middleVal}, val: {val}')
                przedzial = przedzial.getRightRange()

        raise Exception("something went wrong") 