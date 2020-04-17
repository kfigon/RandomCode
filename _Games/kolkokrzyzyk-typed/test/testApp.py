import unittest
import logging
from app import TicTacToe, Field, GameResult

class TestFoo(unittest.TestCase):
    def setUp(self):
        logging.basicConfig(level=logging.INFO)
        self.g = TicTacToe()

    def testStart(self):
        self.assertEqual([Field.EMPTY]*9, self.g.gameArea)
        self.assertEqual(Field.X, self.g.currentPlayer)
        self.assertEqual(GameResult.PENDING, self.g.getStatus())

    def testIsOver2(self):
        self.g.move(0)
        self.assertEqual(Field.O, self.g.currentPlayer)
        self.assertEqual(GameResult.PENDING, self.g.getStatus())
    
    def testMoveToInvalid(self):
        case = [-2, -1, 9, 10, 11]
        for x in case:
            with self.subTest(name=f'when {x} then throw'):
                self.assertRaises(ValueError, self.g.move, x)

    def testGameResult(self):
        case = [
            {'result': GameResult.PENDING, 'steps':[0,1,3]},
            {'result': GameResult.PENDING, 'steps':[4,3,1,7]},
            {'result': GameResult.PENDING, 'steps':[0,4,2,3,6]},

            {'result': GameResult.TIE, 'steps':[4,0,6,2,1,7,3,5,8]},

            {'result': GameResult.X_WIN, 'steps':[0,4,1,3,2 ]},
            {'result': GameResult.X_WIN, 'steps':[3,1,4,2,5 ]},
            {'result': GameResult.X_WIN, 'steps':[6,1,7,2,8 ]},

            {'result': GameResult.X_WIN, 'steps':[0,1,3,2,6 ]},
            {'result': GameResult.X_WIN, 'steps':[1,0,4,2,7 ]},
            {'result': GameResult.X_WIN, 'steps':[2,1,5,4,8 ]},

            {'result': GameResult.X_WIN, 'steps':[0,1,4,2,8 ]},
            {'result': GameResult.X_WIN, 'steps':[2,1,4,7,6 ]},
        ]
        for x in case:
            self.g = TicTacToe()
            with self.subTest(name=f'steps: {x["steps"]}'):
                for s in x['steps']:
                    self.g.move(s)
                self.assertEqual(x['result'], self.g.getStatus())


if __name__=='__main__':
    unittest.main()

