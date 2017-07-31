__author__ = 'kamil'

import unittest
from foo import Board
from foo import Element
from foo import Game

class testGame(unittest.TestCase):

    def setUp(self):
        super().setUp()
        self.g = Game(6)

        tab = []
        tab.append(Element(0))
        tab.append(Element(2))
        tab.append(Element(1))
        tab.append(Element(0))
        tab.append(Element(2))
        tab.append(Element(1))
        self.g.getBoard().injectBoard(tab)

    def testZgadywania1(self):
        result = self.g.zgadnij(2,4) # tam sa ID 1 i 2
        self.assertFalse(result)
        el1 = self.g.getBoardElement(2)
        el2 = self.g.getBoardElement(4)
        self.assertFalse(el1.czyZgadniety())
        self.assertFalse(el2.czyZgadniety())
        self.assertFalse(self.g.czyWszystkieZgadniete())

    def testZgadywania2(self):
        result = self.g.zgadnij(0,1) # tam sa ID 0 i 2
        self.assertFalse(result)
        el1 = self.g.getBoardElement(0)
        el2 = self.g.getBoardElement(1)
        self.assertFalse(el1.czyZgadniety())
        self.assertFalse(el2.czyZgadniety())
        self.assertFalse(self.g.czyWszystkieZgadniete())

    def testZgadywania3(self):
        result = self.g.zgadnij(1,4) # tam sa ID 2
        self.assertTrue(result)
        el1 = self.g.getBoardElement(1)
        el2 = self.g.getBoardElement(4)
        self.assertTrue(el1.czyZgadniety())
        self.assertTrue(el2.czyZgadniety())
        self.assertFalse(self.g.czyWszystkieZgadniete())

    def testWszystkieZgadniete(self):
        self.assertTrue(self.g.zgadnij(0,3))
        self.assertTrue(self.g.zgadnij(5,2))
        self.assertTrue(self.g.zgadnij(4,1))
        self.assertTrue(self.g.czyWszystkieZgadniete())

class testPlanszy(unittest.TestCase):
    def setUp(self):
        super().setUp()
        self.b = Board(6)

    def testGenerowaniaListy(self):
        out = self.b.generateRandomList(6)
        notExpected=[0,1,2,3,4,5]
        self.assertNotEqual(notExpected, out)

    def testWygenerowanychElementow(self):
        tab = self.b.getData()

        for i in range(len(tab)):
            el = tab[i]
            ilePowtorzen = 0
            for j in range(len(tab)):
                if(el.getId() == tab[j].getId()):
                    ilePowtorzen+=1
            self.assertEqual(2, ilePowtorzen, "powtorzenia kazdego Id powinny byc dokladnie 2")


if __name__ == '__main__':
    unittest.main()
