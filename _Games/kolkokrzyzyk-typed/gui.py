import tkinter as tk
from typing import List, Tuple, Callable, Dict, Optional
import logging


def isInside(start: Tuple[int,int], point :Tuple[int,int], size: int) -> bool:
    x,y=point
    sX,sY = start
    return x >= sX  and x < (sX+size) and y >= sY and y < (sY+size)

class Gui:
    def __init__(self):
        self.root = tk.Tk()
        self.plotno = tk.Canvas(self.root, width=300, height=300)
        self.plotno.bind('<Button-1>', self.click)
        
        tk.Button(self.root, text='czysc', command=self.czysc).pack()
        tk.Button(self.root, text='rysuj', command=self.draw).pack()
        tk.Button(self.root, text='zamknij', command=self.end).pack()
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


    def czysc(self):
        self.plotno.delete('all')

    def draw(self) -> None:
        lineLength = self.__fieldLen*3
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


    def start(self) -> None:
        self.root.mainloop()

    def mapPointToIdx(self, p:Tuple[int,int]) -> Optional[int]:
        for key in self.__fieldCoordinates:
            field = self.__fieldCoordinates[key]
            if isInside(field, p, self.__fieldLen):
                return key
        return None

    def click(self, event) -> None:
        p = (event.x, event.y)
        logging.debug(f'clicked at {p}')
        idx = self.mapPointToIdx(p)
        if idx is not None:
            logging.info(f'mapped to {idx}')

            
    def end(self) -> None:
        self.root.destroy()

if __name__=='__main__':
    logging.basicConfig(level=logging.DEBUG)
    g=Gui()
    g.draw()
    g.start()