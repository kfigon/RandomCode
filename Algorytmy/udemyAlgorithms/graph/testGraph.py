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

if __name__ == "__main__":
    unittest.main()
