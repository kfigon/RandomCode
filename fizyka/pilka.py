from wektor import Wektor
from gui import Okno

class Pilka:
    def __init__(self):
        self.__location = Wektor(10,10)
        self.__velocity = Wektor(5,5)
    
    def update(self, w, h):
        loc = self.__location

        if(loc.x < 0 or loc.x >w):
            self.__velocity.odbijWPionie()
        if(loc.y < 0 or loc.y>h):
            self.__velocity.odbijWPoziomie()
        
        self.__location.dodajWektor(self.__velocity)

    def getLocation(self):
        return self.__location


class update:
    def __init__(self, cavas, pilka, w, h):
        self.canvas = cavas
        self.pilka=pilka
        self.w = w
        self.h = h

    def do(self):
        self.pilka.update(self.w, self.h)
        loc = self.pilka.getLocation()

        self.canvas.delete('all')        
        self.canvas.create_oval(loc.x, loc.y, 
        loc.x+5, 
        loc.y+5, fill='black')

o = Okno()
c = o.canvas
pilka = Pilka()
o.start(update(c, pilka, o.WIDTH, o.HEIGHT))