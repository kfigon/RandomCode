import unittest
from graphs import Graph

class Test(unittest.TestCase):
    def testAddNode(self):
        g = Graph()
        g.addNode('foo')
        self.assertEqual(list(g.data.keys()), ['foo'])
        self.assertEqual(g.data['foo'], [])
        g.data['foo'].append('asd')
        g.addNode('foo')
        self.assertEqual(g.data['foo'], ['asd'])

    def testConnect(self):
        g = Graph()
        g.addNode('Tokyo')
        g.addNode('New York')
        g.addNode('Warsaw')

        g.connect('Tokyo', 'New York')
        self.assertTrue(g.areConnected('Tokyo', 'New York'))
        self.assertTrue(g.areConnected('New York', 'Tokyo'))
        self.assertFalse(g.areConnected('New York', 'Warsaw'))

    def testConnectNotExisting(self):
        g = Graph()
        g.addNode('Tokyo')
        self.assertRaises(Exception, g.connect, ('Tokyo', 'Warsaw'))

    def testRemoveConnection(self):
        g = Graph()
        g.addNode('Tokyo')
        g.addNode('New York')
        g.addNode('Warsaw')
        g.connect('Tokyo', 'New York')
        g.connect('Warsaw', 'New York')

        g.removeConnection('New York', 'Tokyo')

        self.assertFalse(g.areConnected('Tokyo', 'New York'))
        self.assertFalse(g.areConnected('New York', 'Tokyo'))
        self.assertTrue(g.areConnected('New York', 'Warsaw'))

    def testRemoveNode(self):
        g = Graph()
        g.addNode('Tokyo')
        g.addNode('New York')
        g.addNode('Warsaw')

        g.connect('Tokyo', 'New York')
        g.connect('Warsaw', 'New York')
        g.connect('Warsaw', 'Tokyo')

        g.removeNode('New York')

        self.assertRaises(Exception, g.areConnected, ('Tokyo', 'New York'))
        self.assertRaises(Exception, g.areConnected, ('New York', 'Tokyo'))
        self.assertRaises(Exception, g.areConnected, ('New York', 'Warsaw'))

        self.assertTrue(g.areConnected('Warsaw', 'Tokyo'))
        
        self.assertFalse('New York' in g.data)
        for k in g.data.keys():
            self.assertFalse('New York' in g.data[k], f'New York present in {k} -> {g.data[k]}')

class TestTraversal(unittest.TestCase):
    def setUp(self):
        self.g = Graph()
        
        #     A
        #   /    \
        # B        C
        # |         |
        # D  -----  E
        #   \     /
        #      F     
        nodes = ['A', 'B','C','D','E','F']
        connections=[
            ('A','B'), ('A','C'),
            ('B','D'),
            ('C','E'), 
            ('D','E'),
            ('D','F'),
            ('E','F')]
        self.buildGraph(self.g, nodes, connections)

    def buildGraph(self, g, nodes, connections):
        for n in nodes:
            g.addNode(n)
        for c in connections:
            g.connect(c[0], c[1])

    def testDfs(self):
        expectedNodes = ['A','B','D','E','C','F']
        self.assertEqual(self.g.dfs('A'), expectedNodes)
    
    def testDfsInter(self):
        expectedNodes = ['A','C','E','F','D','B']
        self.assertEqual(self.g.dfsIter('A'), expectedNodes)

    def testBfsIter(self):
        expectedNodes = ['A','B','C','D','E','F']
        self.assertEqual(self.g.bfs('A'), expectedNodes)

    def testBfsIter2(self):
        g = Graph()
        
        #      A
        #   /    \
        # B        E
        # | \     /|
        # C  \   /  F
        #   \ \ / /
        #      D     
        nodes = ['A', 'B','C','D','E','F']
        connections=[
            ('A','B'), ('A','E'),
            ('B','C'),('B','D'),
            ('E','F'), ('E','D'), 
            ('D','C'), ('D','F')]

        self.buildGraph(g, nodes, connections)
        expectedNodes = ['A','B','C','D','E','F']
        self.assertEqual(self.g.bfs('A'), expectedNodes)

if __name__ == "__main__":
    unittest.main()
