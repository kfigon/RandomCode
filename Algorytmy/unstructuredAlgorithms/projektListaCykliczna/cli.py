from lista import Lista

class Komenda:
    def __init__(self, lista, id):
        self.l = lista
        self.id = id
    
    def dajOpis(self):
        pass
    def robAkcje(self, args):
        pass
    def czyWymagaArgumentu(self):
        return False

class Wypisz(Komenda):
    def __init__(self, lista):
        super().__init__(lista, '1')

    def dajOpis(self):
        return "{}. Wypisz liste".format(self.id)
    def robAkcje(self, args):
        for i in range(self.l.getSize()):
            print("{} -> {} ".format(i, self.l.get(i)))
        input("wcisnij enter aby kontynuowac")

class DodajNaKoniec(Komenda):
    def __init__(self, lista):
        super().__init__(lista, '2')
    def dajOpis(self):
        return "{}. Dodaj na koniec".format(self.id)
    def robAkcje(self, args):
        try:
            self.l.add(args)
        except Exception as e:
            print("Blad! ", e)
    def czyWymagaArgumentu(self):
        return True

class WypiszElement(Komenda):
    def __init__(self, lista):
        super().__init__(lista, '3')
    def dajOpis(self):
        return "{}. Wypisz element o indeksie X".format(self.id)
    def robAkcje(self, args):
        try:
            print(self.l.get(int(args)))

        except Exception as e:
            print("Blad! ", e)
        finally:
            input("wcisnij enter aby kontynuowac")

    def czyWymagaArgumentu(self):
        return True
        
class CzyscListe(Komenda):
    def __init__(self, lista):
        super().__init__(lista, '4')
    def dajOpis(self):
        return "{}. Czysc liste".format(self.id)
    def robAkcje(self, args):
        self.l.clear()

class Wyjdz(Komenda):
    def __init__(self):
        super().__init__(None, 'q')
    def dajOpis(self):
        return "{}. Wyjdz".format(self.id)
    def robAkcje(self, args):
        pass

class Gui:
    def __init__(self):
        self.l = Lista()
        lista = self.l
        self.komendy = [Wypisz(lista),
            DodajNaKoniec(lista),
            WypiszElement(lista), 
            CzyscListe(lista),
            Wyjdz()] 
    
    def piszMenu(self):
        for _ in range(20):
            print("\n")

        for k in self.komendy:
            print(k.dajOpis())
    
    def wybierzOpcje(self):
        opcja = input("wybierz opcje > ")
        for k in self.komendy:
            if opcja == k.id:
                arg = None
                if k.czyWymagaArgumentu():
                    arg = input("podaj argument > ")
                k.robAkcje(arg)
        return opcja

def main():
    print("Witaj w programie!")
    g = Gui()
    wybrane = None
    while wybrane != 'q':
        g.piszMenu()
        wybrane = g.wybierzOpcje()

if __name__ == '__main__':
    main()