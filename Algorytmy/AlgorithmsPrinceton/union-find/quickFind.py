from typing import List

class QuickFind:
    def __init__(self, rozmiar: int):
        self.tab : List[int] = [i for i in range(rozmiar)]

    def validate(self, p, q):
        length = len(self.tab)
        assert p < length and q < length, f"invalid idx, {p}, {q}, len: {length}"
        assert p >= 0 and q >=0, f"invalid idx, {p}, {q}, need to be >=0"


    def connected(self, p, q) -> bool:
        self.validate(p,q)
        return self.tab[p] == self.tab[q]

    def union(self, p,q):
        if self.connected(p, q):
            return

        finalIdx = self.tab[q]
        searchingIdx = self.tab[p]
        for i in range(len(self.tab)):
            if self.tab[i] == searchingIdx:
                self.tab[i] = finalIdx

    def getNumberOfConnectedComponents(self) -> int:
        uniqueIdxs : List[int] = []
        for i in self.tab:
            if i not in uniqueIdxs:
                uniqueIdxs.append(i)

        return len(uniqueIdxs)


if __name__ == "__main__":
    uf = QuickFind(10)
    uf.union(4,3)
    uf.union(3,8)
    uf.union(6,5)
    uf.union(9,4)
    uf.union(2,1)
    uf.union(8,9)
    uf.union(5,0)
    uf.union(7,2)
    uf.union(6,1)

    print(uf.tab)
