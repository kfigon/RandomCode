from wektor import Wektor
from gui import Okno

class Pilka:
    def __init__(self):
        self.location = Wektor(50,0)
        self.velocity = Wektor(0,0)
        self.acceleration = Wektor(0,0)

    def update(self, w, h):
        loc = self.location
        if(loc.y >= h):
            self.location = Wektor(50,0)
            self.velocity = Wektor(0,0)
            # self.acceleration = Wektor(0,0)
            return        
            # F = m*a
            # sila (wektor) zmienia szybkosc, szybkosc zmienia polozenie
        self.velocity.dodajWektor(self.acceleration)
        self.location.dodajWektor(self.velocity)

    def zaaplikujSile(self, sila):
        self.acceleration.dodajWektor(sila)

class update:
    def __init__(self, cavas, pilka, w, h):
        self.canvas = cavas
        self.pilka=pilka
        self.w = w
        self.h = h

    def do(self):
        self.pilka.update(self.w, self.h)
        loc = self.pilka.location

        self.canvas.delete('all')        
        self.canvas.create_oval(loc.x, loc.y, 
        loc.x+10, 
        loc.y+10, fill='black')


o = Okno(50)
c = o.canvas
pilka = Pilka()

grawitacja = Wektor(0,0.3)
pilka.zaaplikujSile(grawitacja)


o.start(update(c, pilka, o.WIDTH, o.HEIGHT))