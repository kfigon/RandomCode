__author__ = 'kamil'

class KalkulatorWspolrzednych:
    # rozmiary planszy w 'klockach'
    # a klocka w pixelach
    def __init__(self, wysokoscPlanszy, szerokoscPlanszy, wysokoscKlocka, szerokoscKlocka):
        self.__wysokoscPlanszy = wysokoscPlanszy
        self.__szerokoscPlanszy = szerokoscPlanszy
        self.__wysokoscKlocka = wysokoscKlocka
        self.__szerokoscKlocka = szerokoscKlocka

    # wpolrzedne poczatku i konca - po przekatnej
    def get(self, idx):
        wiersz,kolumna = self.mapTo2D(idx)

        x = kolumna*self.__szerokoscKlocka
        y = wiersz*self.__wysokoscKlocka
        dx = x + self.__szerokoscKlocka-1
        dy = y + self.__wysokoscKlocka-1
        return (x,y,dx,dy)

    def mapTo2D(self, i):
        w = int(i/self.__wysokoscPlanszy)
        k = i - (self.__szerokoscPlanszy*w)

        return (w,k)
