import unittest

class IBaza:
    def foo(self):
        pass

class Lisc(IBaza):
    def __init__(self, nazwa):
        self.__nazwa = nazwa
    def foo(self):
        print("%s - lisc robi..." % self.__nazwa)

class Komponent(IBaza):
    def __init__(self, nazwa):
        self.__nazwaKomponentu = nazwa
        self.__komponenty=[] # typ IBaza

    def dodaj(self, ibaza):
        self.__komponenty.append(ibaza)
    def foo(self):
        print("%s robi:" % self.__nazwaKomponentu)
        for k in self.__komponenty:
            k.foo()
    
# cos takiego pozwala tworzyc drzewiaste struktury:
# komponent sklada sie z listy kolejnych komponentow
# lista komponentow zawiera komponenty lub list (end point, konczy drzewo)

# np. interfejs - strukturaMieszkalna
# komponent - pietro/budynek
# list - pokoj

# mozna zlozyc budynek (komponent), ktory ma komponenty - pietra i zwykle pokoje
# kazdy komponent na liscie tez ma subpietra i pokoje

# albo zbiory piosenek i piosenki


# w skrocie - komponent dziedziczy po interfejsie i trzyma liste tego samego
# do tego liscie

budynek = Komponent("budynek")
p1 = Komponent("pietro 1")
p1.dodaj(Lisc('asd'))
p1.dodaj(Lisc('sad'))

budynek.dodaj(p1)
budynek.dodaj(Lisc('luzny pokoj'))

budynek.foo()
