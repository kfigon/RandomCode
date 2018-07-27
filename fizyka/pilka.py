from wektor import Wektor
from gui import Okno

class Pilka:
    def __init__(self):
        self.__location = Wektor(10,10)
        self.__velocity = Wektor(1,1)
    
    def update(self):
        self.__location.dodajWektor(self.__velocity)

    def getLocation(self):
        return self.__location


class update:
    def __init__(self, cavas, pilka):
        self.canvas = cavas
        self.pilka=pilka

    def do(self):
        self.pilka.update()
        loc = self.pilka.getLocation()

        self.canvas.delete('all')        
        self.canvas.create_oval(loc.x, loc.y, 
        loc.x+5, 
        loc.y+5, fill='black')

o = Okno()
c = o.canvas
pilka = Pilka()
o.start(update(c, pilka))