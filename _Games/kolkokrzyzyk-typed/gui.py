import tkinter as tk
from typing import List, Tuple, Callable, Dict, Optional
import logging
from app import TicTacToe, GameResult, Field
from ai import RandomOpponentStrategy

def isInside(start: Tuple[int,int], point :Tuple[int,int], size: int) -> bool:
    x,y=point
    sX,sY = start
    return x >= sX  and x < (sX+size) and y >= sY and y < (sY+size)

class Gui:
    def __init__(self):
        self.root = tk.Tk()
        self.plotno = tk.Canvas(self.root, width=300, height=300)
        self.plotno.bind('<Button-1>', self.click)
        
        tk.Button(self.root, text='Reset', command=self.resetGame).pack()
        self.plotno.pack()
        
        self.__fieldLen = 50
        self.__lineCoordinates :Dict[str,Tuple[int,int]]= {
            'H1': (70,70), 'H2': (70,120),
            'V1': (120,20), 'V2': (170,20)
        }
        
        self.__fieldCoordinates :Dict[int,Tuple[int,int]]= {
            0: (self.__lineCoordinates['H1'][0], self.__lineCoordinates['V1'][1]), 
            1: (self.__lineCoordinates['V1'][0], self.__lineCoordinates['V1'][1]), 
            2: (self.__lineCoordinates['V2'][0], self.__lineCoordinates['V2'][1]),
            
            3: (self.__lineCoordinates['H1'][0], self.__lineCoordinates['H1'][1]),
            4: (self.__lineCoordinates['V1'][0], self.__lineCoordinates['H1'][1]),
            5: (self.__lineCoordinates['V2'][0], self.__lineCoordinates['H1'][1]),

            6: (self.__lineCoordinates['H2'][0], self.__lineCoordinates['H2'][1]),
            7: (self.__lineCoordinates['V1'][0], self.__lineCoordinates['H2'][1]),
            8: (self.__lineCoordinates['V2'][0], self.__lineCoordinates['H2'][1]),
        }
        self.game :TicTacToe = TicTacToe()
        self.opponentStrategy = RandomOpponentStrategy()

    def start(self) -> None:
        self.root.mainloop()

    def resetGame(self):
        self.game = TicTacToe()
        self.refreshBoard()

    def clearAll(self):
        self.plotno.delete('all')

    def drawGameField(self) -> None:
        lineLength: int = self.__fieldLen*3
        horizontal : Callable[[Tuple[int, int]], Tuple[Tuple[int, int], Tuple[int, int]]] = lambda p: (p, (p[0]+lineLength, p[1])) 
        vertical : Callable[[Tuple[int, int]], Tuple[Tuple[int, int], Tuple[int, int]]] = lambda p: (p, (p[0], p[1]+lineLength)) 

        lines : List[Tuple[Tuple[int, int], Tuple[int, int]]] = [
            horizontal(self.__lineCoordinates['H1']),
            horizontal(self.__lineCoordinates['H2']),
            vertical(self.__lineCoordinates['V1']),
            vertical(self.__lineCoordinates['V2'])
        ]

        for line in lines:
            x1,y1 = line[0]
            x2,y2 = line[1]
            self.plotno.create_line(x1,y1, x2, y2, width=2, fill='black')

    def drawCircle(self, idx: int):
        startX, startY = self.__fieldCoordinates[idx]
        self.plotno.create_oval(startX, startY, startX+self.__fieldLen-5, startY+self.__fieldLen-5, width=2, outline='blue')

    def drawCross(self, idx: int):
        startX, startY = self.__fieldCoordinates[idx]
        startX +=2
        startY += 2
        self.plotno.create_line(startX, startY, startX+self.__fieldLen-5, startY+self.__fieldLen-5, width=2, fill='red')
        self.plotno.create_line(startX+self.__fieldLen-5, startY, startX, startY+self.__fieldLen-5, width=2, fill='red')

    def refreshBoard(self):
        self.clearAll()
        self.drawGameField()
        for i,f in enumerate(self.game.gameArea):
            if f == Field.O:
                self.drawCircle(i)
            elif f == Field.X:  
                self.drawCross(i)

    def mapPointToIdx(self, p:Tuple[int,int]) -> Optional[int]:
        for key in self.__fieldCoordinates:
            field = self.__fieldCoordinates[key]
            if isInside(field, p, self.__fieldLen):
                return key
        return None

    def click(self, event) -> None:
        if self.game.getStatus() != GameResult.PENDING:
            logging.info("it's over, go away")
            return

        p = (event.x, event.y)
        logging.debug(f'clicked at {p}')
        idx : Optional[int] = self.mapPointToIdx(p)
        if idx is None:
            return
        logging.info(f'clicked {idx}')

        try:
            self.playerMove(idx)
            self.refreshBoard()
        except Exception:
            logging.info('invalid move!')
            return
        
        self.opponentMove()
        self.refreshBoard()
        logging.info(f'round result: {self.game.getStatus()}')
    
    def playerMove(self, idx: int) -> None:
        if self.game.getStatus() == GameResult.PENDING:
            self.game.move(idx)

    def opponentMove(self) -> None:
        if self.opponentStrategy != None and self.game.getStatus() == GameResult.PENDING:
            opponentMove: int = self.opponentStrategy.doAction(self.game)
            self.game.move(opponentMove)

    
if __name__=='__main__':
    logging.basicConfig(level=logging.INFO)
    g=Gui()
    g.refreshBoard()
    g.start()
