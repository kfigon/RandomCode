import unittest
from weightedGraph import Graph
from dijkstra import Dijkstra

class Test(unittest.TestCase):
    def setUp(self):
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
        g = Graph.createGraph(nodes, connections)
        self.d = Dijkstra(g)

    def test1(self):
        self.assertEqual(self.d.findPath('A', 'E'), (['A','C','D','F','E'],6))
        self.assertEqual(self.d.findPath('A', 'D'), (['A','C','D'],4))
        self.assertEqual(self.d.findPath('F', 'C'), (['F','D','C'],3))
        self.assertEqual(self.d.findPath('F', 'B'), (['F','E','B'],4))

if __name__ == "__main__":
    unittest.main()