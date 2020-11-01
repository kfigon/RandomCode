from typing import List, Optional, Dict, Callable, Tuple

# adjacencyList
# undirected, weighted graph

class Connection:
    def __init__(self, name:str, weigth: int):
        self.weight=weigth
        self.name=name
    def __eq__(self, other):
        return (self.name == other.name) and (self.weight == other.weight)

class Graph:
    def __init__(self):
        self.data: Dict[str,List[Connection]] = {}

    def addNode(self, name: str):
        if name not in self.data:
            self.data[name] = []

    def connect(self, nodeA: str, nodeB: str, weigth: int):
        self._validateSingle(nodeA)
        self._validateSingle(nodeB)

        self.data[nodeA].append(Connection(nodeB, weigth))
        self.data[nodeB].append(Connection(nodeA, weigth))
    
    def _validateSingle(self, nodeA: str):
        if self.data[nodeA] is None:
            raise Exception(f'invalid node {nodeA}')                

    @staticmethod
    def createGraph(nodes: List[str], connections:List[Tuple[str,str,int]]):
        g = Graph()
        for n in nodes:
            g.addNode(n)
        for c in connections:
            g.connect(c[0],c[1],c[2])
        return g