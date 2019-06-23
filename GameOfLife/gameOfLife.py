import random
import time
from tkinter import *

class Cell:
    def __init__(self):
        self.x=0
        self.y=0
        self.alive = False

    def setLocation(self, x,y):
        self.x=x
        self.y=y
        
    def kill(self):
        self.alive=False
    def live(self):
        self.alive=True
    def isAlive(self):
        return self.alive

# martwa i 3 sasiedzi - odzywa
# zywa i 2,3 sasiedzi - zyje dalej
# zywa i <2 lub >3 - umiera
class Area:
    THRESHOLD = 17 # im wiecej tym mniej komorek, do 20
    def __init__(self, size, threshold = THRESHOLD):
        self.matrix= Matrix(size)
        
        for w in range(size):
            for k in range(size):
                c = Cell()
                if random.randint(0,20) > self.THRESHOLD:
                    c.live()
                self.matrix.set(w,k, c)
                
    def getCell(self, x,y):
        return self.matrix.get(x,y)

    def __getNumberOfAliveNeighbours(self, w,k):
        nei = self.matrix.getNeighbours(w,k)
        alive = 0
        for c in nei:
            if c.isAlive():
                alive+=1
        return alive

    def size(self):
        return self.matrix.size
    
    def killAll(self):
         for w in range(self.matrix.size):
            for k in range(self.matrix.size):
                self.getCell(w,k).kill()
                
    def tick(self):
        for w in range(self.matrix.size):
            for k in range(self.matrix.size):
                c = self.getCell(w,k)
                aliveNei = self.__getNumberOfAliveNeighbours(w,k)
                if c.isAlive():
                    if aliveNei <2 or aliveNei>3:
                        c.kill()
                else:
                    if aliveNei == 3:
                        c.live()

class Matrix:
    def __init__(self, size):
        self.size = size
        self.tab = [None]*(size**2)

    def get(self, x,y):
        self.__assertSize(x,y)
        return self.tab[mapTo1d(x,y,self.size)]
    
    def set(self, x,y, val):
        self.__assertSize(x,y)
        self.tab[mapTo1d(x,y,self.size)] = val
    
    def __assertSize(self, x,y):
        if x >= self.size or y>=self.size:
            raise IndexError('size: ' + str(self.size) + 'x,y='+str(x) +str(y))

    def getNeighbours(self,w,k):
        candidatePairs = [(w-1, k-1),(w-1, k), (w-1, k+1),
                          (w, k-1), (w, k+1),
                          (w+1, k-1), (w+1,k), (w+1,k+1)]

        bounds = lambda v: v >=0 and v < self.size
        candidatePairs = list(filter(lambda pair: bounds(pair[0]) and bounds(pair[1]), candidatePairs))
        
        candidateIdxs = [mapTo1d(x,y, self.size) for x,y in candidatePairs]
        return [self.tab[i] for i in candidateIdxs]
        
def mapTo1d(x,y,size):
    return x*size + y


class Widok:
    def __init__(self, root):
        self.__rozmiarPlanszy = 20
        self.__area = Area(self.__rozmiarPlanszy)

        szerKlocka, wysKlocka = self.getWymiaryKlocka()
        szerokoscPola = szerKlocka*self.__rozmiarPlanszy
        wysokoscPola = wysKlocka*self.__rozmiarPlanszy + 40 # gorka na przycisk i label

        self.__buton = Button(root, text = 'resetuj', command=self.__resetuj)
        self.__buton2 = Button(root, text = 'tick', command=self.rysuj)
        self.__plotno = Canvas(root, width = szerokoscPola, height = wysokoscPola)
        self.__plotno.pack()
        self.__buton.pack()
        self.__buton2.pack()

    def __resetuj(self):
        self.__area = Area(self.__rozmiarPlanszy)
        self.rysuj()

    def getWymiaryKlocka(self):
        return 15,15

    def rysuj(self):
        self.__area.tick()
        self.__plotno.delete("all")
        wymiary = self.getWymiaryKlocka()

        for w in range(self.__area.size()):
            for k in range(self.__area.size()):
                c=self.__area.getCell(w,k)
                color = 'black' if c.isAlive() else 'white'

                x1 = k*wymiary[0]
                y1 = w*wymiary[1]
                x2 = x1 + wymiary[0]-1
                y2 = y1 + wymiary[1]-1
                self.__plotno.create_rectangle(x1,y1,x2,y2, fill=color)

if __name__ == '__main__':
    root = Tk()
    w = Widok(root)
    w.rysuj()
    root.mainloop()
    