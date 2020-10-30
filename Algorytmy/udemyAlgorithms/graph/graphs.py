from typing import List, Optional, Dict

# adjacencyList
# undirected graph
class Graph:
    def __init__(self):
        self.data: Dict[str,List[str]] = {}

# todo - toupper?
    def addNode(self, name: str):
        if name not in self.data:
            self.data[name] = []

    def connect(self, nodeA: str, nodeB: str):
        self._validate(nodeA, nodeB)

        self.data[nodeA].append(nodeB)
        self.data[nodeB].append(nodeA) # undirected part
        
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
        self._validateSingle(nodeA)
        self._validateSingle(nodeB)
    
    def _validateSingle(self, nodeA: str):
        if self.data[nodeA] is None:
            raise Exception(f'invalid nodes {nodeA}')

    def removeConnection(self, nodeA:str, nodeB:str):
        self._validate(nodeA, nodeB)
        self.data[nodeA].remove(nodeB)
        self.data[nodeB].remove(nodeA)

    def removeNode(self, nodeA: str):
        self._validateSingle(nodeA)
        del self.data[nodeA]
        
        for k in self.data.keys():
            if nodeA in self.data[k]:
                self.data[k].remove(nodeA)
                