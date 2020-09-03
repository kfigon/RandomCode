from typing import List

class QuickFind:
    def __init__(self, rozmiar: int):
        self.tab : List[int] = [i for i in range(rozmiar)]

    def connected(self, p, q) -> bool:
        return False

    def union(self, p,q):
        pass

    def getNumberOfConnectedComponents(self) -> int:
        pass