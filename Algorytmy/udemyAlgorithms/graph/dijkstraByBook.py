# implementation by book
from typing import List, Optional, Tuple, Dict
from weightedGraph import Graph, Connection
import math

class PriorityQueue:
    def __init__(self):
        self.vals: List[Tuple[str, int]] = []
    def enqueue(self, value: str, priority: int):
        self.vals.append((value, priority))
        self.vals.sort(key=lambda x: x[1])
    def dequeue(self) -> Tuple[str,int]:
        v = self.vals[0]
        self.vals.remove(v)
        return v
    def empty(self) -> bool:
        return len(self.vals) == 0

class Dijkstra:
    def __init__(self, graph: Graph):
        self.g=graph

    def findPath(self, nodeStart: str, nodeEnd: str) -> List[str]:
        queue = PriorityQueue()
        previous: Dict[str, Optional[str]] = {}
        distances: Dict[str, int] = {}

        # init
        for node in self.g.data.keys():
            if node != nodeStart:
                distances[node] = math.inf
            else:
                distances[node] = 0
            queue.enqueue(node, distances[node])
            previous[node] = None

        while not queue.empty():
            smallest = queue.dequeue()[0]
            
            if smallest == nodeEnd:
                path: List[str] = []
                while previous[smallest]:
                    path.append(smallest)
                    smallest = previous[smallest]
                
                path.append(smallest)
                return list(reversed(path))

            if not smallest and distances[smallest] == math.inf:
                continue

            for nei in self.g.data[smallest]:
                candidate = distances[smallest] + nei.weight
                if candidate < distances[nei.name]:
                    distances[nei.name] = candidate
                    previous[nei.name] = smallest
                    queue.enqueue(nei.name, candidate)
                
        return []

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
    print(d.findPath('A','B'))

