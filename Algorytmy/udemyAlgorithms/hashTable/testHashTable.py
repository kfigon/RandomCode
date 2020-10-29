import unittest
from hashTable import HashTable, myHashFun, myBetterHashFun

class TestHashTable(unittest.TestCase):
    def test(self):
        h = HashTable()
        h.put('pink' ,'123')
        h.put('foo' ,'bar')
        self.assertEqual(h.get('pink'), '123')
        self.assertEqual(h.get('foo'), 'bar')
        self.assertRaises(Exception, h.get, 'cyan')
        self.assertRaises(Exception, h.put, 'pink')

        self.assertEqual(h.tab[15][0][0], 'pink')
        self.assertEqual(h.tab[15][0][1], '123')

    def testWithCollision(self):
        h = HashTable(4)
        h.put('pink' ,'123')
        h.put('blue' ,'asd')
        h.put('orange' ,'sad')
        self.assertEqual(h.get('pink'), '123')
        self.assertEqual(h.get('blue'), 'asd')
        self.assertEqual(h.get('orange'), 'sad')
        
        self.assertEqual(h.tab[2][0][0], 'pink')
        self.assertEqual(h.tab[2][0][1], '123')
        
        self.assertEqual(h.tab[2][1][0], 'blue')
        self.assertEqual(h.tab[2][1][1], 'asd')
        
        self.assertEqual(h.tab[2][2][0], 'orange')
        self.assertEqual(h.tab[2][2][1], 'sad')

    def testKeysValues(self):
        h = HashTable()
        h.put('pink' ,'123')
        h.put('blue' ,'asd')
        h.put('orange' ,'123')

        self.assertEqual(h.keys(), ['blue','orange','pink'])
        self.assertEqual(h.values(), ['asd','123'])

class TestHashFun(unittest.TestCase):
    def test1(self):
        self.assertEqual(myHashFun('abc', 20), 6)
        self.assertEqual(myHashFun('pink', 10), 0)
        self.assertEqual(myHashFun('blue', 10), 0)
        self.assertEqual(myHashFun('orange', 10), 0)
        self.assertEqual(myHashFun('orangered', 10), 7)
        self.assertEqual(myHashFun('cyan', 10), 3)

    def test2(self):
        self.assertEqual(myBetterHashFun('hello', 13), 7)
        self.assertEqual(myBetterHashFun('goodbye', 13), 9)
        self.assertEqual(myBetterHashFun('hi', 13), 10)
        self.assertEqual(myBetterHashFun('cyan', 13), 5)
        self.assertEqual(myBetterHashFun('pink', 13), 5)
        

if __name__ == "__main__":
    unittest.main()