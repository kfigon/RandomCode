from typing import List, Optional, Dict

# adjacencyList
# undirected graph
class Graph:
    def __init__(self):
        self.data: Dict[str,List[str]] = {}

    def addNode(self, name: str):
        if name not in self.data:
            self.data[name] = []

    def connect(self, nodeA: str, nodeB: str):
        self._validate(nodeA, nodeB)

        self.data[nodeA].append(nodeB)
        self.data[nodeB].append(nodeA)
        
    def areConnected(self, nodeA: str, nodeB: str) -> bool:
        self._validate(nodeA, nodeB)
        for i in self.data[nodeA]:
            if i == nodeB:
                return True
        for i in self.data[nodeB]:
            if i == nodeA:
                return True
        return False

    def _validate(self, nodeA: str, nodeB: str):
        if self.data[nodeA] is None or self.data[nodeB] is None:
            raise Exception(f'invalid nodes {nodeA}:{nodeB}')