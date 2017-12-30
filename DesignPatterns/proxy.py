import unittest

# 2 obiekty, komunikujace sie ze soba
# proxy to prostsza wersja jednego z nich
# proxy wrapuje oryginal

# proxy chroni oryginal
# ukrywa bebechy i wola do oryginalu
# proxy oszczedza zasoby - klient gada z proxy przez interfejs
# a nie z calym duzym magazynem

class Interfejs:
    def zamowienie(self):
        pass

class Magazyn(Interfejs):
    def zamowienie(self):
        print("magazyn - robie wlasciwe zamowienie...")

class Proksy(Interfejs):
    def __init__(self, magazyn):
        self.magazyn = magazyn # albo lista
        
    def zamowienie(self):
        print("proxy przygotowuje zamowienia, rutuje jesli trzeba, sprawdzam poprawnosc...")
        self.magazyn.zamowienie()
        


mag = Magazyn()
pr = Proksy(mag)

pr.zamowienie()
