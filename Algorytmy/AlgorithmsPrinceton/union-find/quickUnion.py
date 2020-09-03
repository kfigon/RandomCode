from typing import List

class QuickUnion:
    def __init__(self, rozmiar: int):
        self.tab : List[int] = [i for i in range(rozmiar)]

    def connected(self, p, q) -> bool:
        self.validate(p,q)
        return self.getRoot(p) == self.getRoot(q)

    def isRoot(self, p) -> bool:
        return p == self.tab[p]

    def getRoot(self, p) -> int:
        rootCandidate = self.tab[p]
        while not self.isRoot(rootCandidate):
            rootCandidate = self.tab[rootCandidate]
        return rootCandidate

    
    def validate(self, p, q):
        length = len(self.tab)
        assert p < length and q < length
        assert p >= 0 and q >= 0

    def union(self, p,q):
        self.validate(p,q)
        rootP = self.getRoot(p)
        rootQ = self.getRoot(q)
        self.tab[rootP] = rootQ

    def getNumberOfConnectedComponents(self) -> int:
        out = 0
        for i in range(len(self.tab)):
            if self.tab[i] == i:
                out +=1

        return out

if __name__ == "__main__":
    pass