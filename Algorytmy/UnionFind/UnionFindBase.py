class UnionFindBase:
    def __init__(self, rozmiarTablicy):
        self._tab = [0]*rozmiarTablicy
        self.clear()

    def clear(self):
        for i in range(len(self._tab)):
            self._tab[i]=i

    def areConnected(self, p, q):
        pass

    def union(self,p,q):
        pass

    def getConnectedComponents(self):
        pass