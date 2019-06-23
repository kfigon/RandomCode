import unittest
from gameOfLife import *

# martwa i 3 sasiedzi - odzywa
# zywa i 2,3 sasiedzi - zyje dalej
# zywa i <2 lub >3 - umiera
class TestArea(unittest.TestCase):
    def setUp(self):
        self.size = 5
        self.a = Area(self.size)
        
    def testLonelyDead(self):
        #given
        self.a.killAll()
        self.a.getCell(0,0).live()
        #when
        self.a.tick()
        #then
        self.assertFalse(self.a.getCell(0,0).isAlive())
        self.assertFalse(self.a.getCell(0,1).isAlive())
        self.assertFalse(self.a.getCell(1,0).isAlive())
        self.assertFalse(self.a.getCell(1,1).isAlive())

    def testGettingAlive(self):
        #given
        self.a.killAll()
        self.a.getCell(0,1).live()
        self.a.getCell(1,0).live()
        self.a.getCell(1,1).live()
        #when
        self.a.tick()
        #then
        self.assertTrue(self.a.getCell(0,0).isAlive())
        self.assertTrue(self.a.getCell(0,1).isAlive())
        self.assertTrue(self.a.getCell(1,0).isAlive())
        self.assertTrue(self.a.getCell(1,1).isAlive())

    def testStillLives(self):
        #given
        self.a.killAll()
        self.a.getCell(0,0).live()
        self.a.getCell(0,1).live()
        self.a.getCell(1,0).live()
        #when
        self.a.tick()
        #then
        self.assertTrue(self.a.getCell(0,0).isAlive())
        self.assertTrue(self.a.getCell(0,1).isAlive())
        self.assertTrue(self.a.getCell(1,0).isAlive())
        
    def testDeadByOverpopulation(self):
        #given
        self.a.killAll()
        self.a.getCell(0,2).live()
        self.a.getCell(1,1).live()
        self.a.getCell(1,2).live()
        self.a.getCell(2,1).live()
        #when
        self.a.tick()
        #then
        self.assertTrue(self.a.getCell(0,2).isAlive())
        self.assertFalse(self.a.getCell(1,1).isAlive())
        self.assertTrue(self.a.getCell(1,2).isAlive())
        self.assertTrue(self.a.getCell(2,1).isAlive())


class TestMatrix(unittest.TestCase):
    def setUp(self):
        self.size = 5
        self.m = Matrix(self.size)

    def testMapTo2d(self):
        kejsy = [
            (0,0, 4, 0),
            (0,1, 4, 1),
            (0,2, 4, 2),
            (0,3, 4, 3),
            (1,0, 4, 4),
            (1,1, 4, 5),
            (1,2, 4, 6),
            (1,3, 4, 7)]
            
        for x,y,size, expected in kejsy:
            nazwa = "when {},{} size {} then {}".format(str(x),str(y), str(size), str(expected))
            with self.subTest(name=nazwa):
                self.assertEqual(expected, mapTo1d(x,y,size))
                
    def testEmpty(self):
        for w in range(self.size):
            for k in range(self.size):
                self.assertEqual(None, self.m.get(w,k))

    def testSetField(self):
        self.m.set(1,1, 12)
        self.assertEqual(12, self.m.get(1,1))
    
    def testOutOfBonds(self):
        self.assertRaises(IndexError, self.m.set, self.size, 1, 123)
        self.assertRaises(IndexError, self.m.get, self.size, 1)

    def populateMatrix(self):
        i=1
        for w in range(self.size):
            for k in range(self.size):
                self.m.set(w,k,i)
                i+=1
    #1  2  3  4  5
    #6  7  8  9  10
    #11 12 13 14 15
    #16 17 18 19 20
    #21 22 23 24 25
    def testGetNeighbours(self):
        self.populateMatrix()
        kejsy = [
            (0,0, [2,6,7]),
            (0,1, [1,3,6,7,8]),
            (1,3, [3,4,5,8,10,13,14,15]),
            (4,0, [16,17,22]),
            (4,2, [17,18,19,22,24]),
            (4,4, [19,20,24])
            ]
            
        for x,y, expected in kejsy:
            nazwa = "when {},{} then {}".format(str(x),str(y),str(expected))
            with self.subTest(name=nazwa):
                self.assertEqual(expected, self.m.getNeighbours(x,y))
        

if __name__ == '__main__':
    unittest.main()