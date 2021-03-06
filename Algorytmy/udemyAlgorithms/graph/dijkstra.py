from typing import List, Tuple, Dict, Optional
from weightedGraph import Graph, Connection

class Previous:
    def __init__(self):
        self.data: Dict[str,str] = {}
    
    def markPrevious(self, nodeFrom: str, nodeTo: str):
        self.data[nodeFrom] = nodeTo
    def getConnections(self, nodeFrom: str, nodeTo: str) -> List[str]:
        out: List[str] = []
        n = nodeTo
        while n != nodeFrom and n in self.data:
            out.append(n)
            n = self.data[n]
        out.append(nodeFrom)
        return out

    def __repr__(self) -> str:
        return str(self.data)

class PathDiary:
    def __init__(self, nodes: List[str], startingNode: str):
        self.visited: List[str] = []

        self.data: Dict[str, Optional[int]] = {}
        for n in nodes:
            self.data[n] = None # infinity
        self.data[startingNode] = 0

    def wasWisited(self, node: str) -> bool:
        return node in self.visited

    def markAsVisited(self, node: str):
        self.visited.append(node)

    def findSmallest(self) -> Optional[str]:
        smallestDist = None
        smallestKey = None
        for key in self.data.keys():
            dist = self.data[key]
            if self.wasWisited(key) or dist is None:
                continue
            if smallestDist is None or dist < smallestDist:
                smallestDist = dist
                smallestKey = key
        
        return smallestKey
    
    def updatePath(self, node:str, path: int) -> bool:
        if self.data[node] is None or path < self.data[node]:
            self.data[node] = path
            return True
        return False

    def getCumulatedPath(self, node:str) -> int:
        if node not in self.data or self.data[node] is None:
            return 0
        return self.data[node]
        
class Dijkstra:
    def __init__(self, graph: Graph):
        self.graph = graph

    def findPath(self, nodeFrom: str, nodeTo: str) -> Tuple[List[str],int]:
        pathDiary = PathDiary(list(self.graph.data.keys()), nodeFrom)
        previousMap = Previous()

        analyzedNode = pathDiary.findSmallest()
        while analyzedNode is not None:
            # print()
            pathDiary.markAsVisited(analyzedNode)

            neighbours: List[Connection] = self.graph.data[analyzedNode]
            for n in neighbours:
                if pathDiary.wasWisited(n.name):
                    continue

                # print(f'analyzing {analyzedNode}, nei {n.name}')
                v = n.weight + pathDiary.getCumulatedPath(analyzedNode)
                if pathDiary.updatePath(n.name, v):
                    # print(f'found smaller path for him, update to {pathDiary.getCumulatedPath(n.name)}')
                    previousMap.markPrevious(n.name, analyzedNode)
            # print(previousMap)
            analyzedNode = pathDiary.findSmallest()

        print(previousMap)
        connectionsEndToStart = previousMap.getConnections(nodeFrom, nodeTo)
        accumulatedLen = pathDiary.getCumulatedPath(nodeTo)
        return list(reversed(connectionsEndToStart)), accumulatedLen


if __name__ == "__main__":
    nodes = ['A','B','C','D','E','F']
    connections =[
            ('A','B',4),
            ('A','C',2), 
            ('B','E',3), 
            ('C','D',2), 
            ('C','F',4), 
            ('D','E',3), 
            ('D','F',1),
            ('F','E',1)
    ]
    g =  Graph.createGraph(nodes, connections)
    d = Dijkstra(g)
    print(d.findPath('E','A'))