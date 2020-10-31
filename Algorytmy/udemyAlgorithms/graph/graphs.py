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
            raise Exception(f'invalid node {nodeA}')

    def removeConnection(self, nodeA:str, nodeB:str):
        self._validate(nodeA, nodeB)
        self.data[nodeA].remove(nodeB)
        self.data[nodeB].remove(nodeA)

    def removeNode(self, nodeA: str):
        self._validateSingle(nodeA)
        while len(self.data[nodeA]) > 0:
            i = self.data[nodeA].pop()
            self.data[i].remove(nodeA)
            
        del self.data[nodeA]

    def dfs(self, startNode: str) -> List[str]:
        self._validateSingle(startNode)

        tracker = VisitedTracker()
        # this list can also be part of tracker object
        visitedNodes: List[str] = []

        def traverse(node: str):
            if len(self.data[node]) == 0:
                return
            
            tracker.markVisited(node)
            visitedNodes.append(node)
            
            for child in self.data[node]:
                if not tracker.wasVisited(child):
                    traverse(child)

        traverse(startNode)
        return visitedNodes

    def dfsIter(self, startNode: str) -> List[str]:
        self._validateSingle(startNode)
        stack: List[str] = []
        visitedNodes: List[str] = []
        tracker = VisitedTracker()

        stack.append(startNode)
        while len(stack) != 0:
            node = stack.pop()
            if tracker.wasVisited(node):
                continue

            tracker.markVisited(node)
            visitedNodes.append(node)
            for child in self.data[node]:
                if not tracker.wasVisited(child):
                    stack.append(child)

        return visitedNodes

class VisitedTracker:
    def __init__(self):
        self.data: Dict[str, bool] = {}
    def markVisited(self, vertex: str):
        self.data[vertex] = True
    def wasVisited(self, vertex: str):
        return (vertex in self.data) and (self.data[vertex] == True)

                