import unittest

# Opis algorytmu
# Najprostsza wersja algorytmu rozpoczyna się od wybrania dwóch liczb naturalnych, dla których należy wyznaczyć 
# największy wspólny dzielnik. Następnie z tych dwóch liczb tworzymy nową parę: pierwszą z liczb jest liczba mniejsza, 
# natomiast drugą jest różnica liczby większej i mniejszej. Proces ten jest powtarzany aż obie liczby będą sobie równe 
# - wartość tych liczb to największy wspólny dzielnik wszystkich par liczb wcześniej wyznaczonych. Wadą tej wersji 
# algorytmu jest duża liczba operacji odejmowania, które należy wykonać w przypadku, gdy różnica pomiędzy liczbami z pary jest znacząca.

# Operacja odejmowania mniejszej liczby od większej może zostać zastąpiona przez wyznaczanie reszty z dzielenia. 
# W tej wersji nowa para liczb składa się z mniejszej liczby oraz reszty z dzielenia większej przez mniejszą. 
# Algorytm kończy się w momencie, w którym jedna z liczb jest równa zero - druga jest wtedy największym wspólnym dzielnikiem.


def tworzPare(a,b):
    wieksza = a
    mniejsza = b
    if(mniejsza > wieksza):
        wieksza,mniejsza = mniejsza, wieksza
    roznica = wieksza - mniejsza
    print(str(wieksza) +" > "+str(mniejsza) +" -> " + str(roznica))
    return (wieksza, mniejsza, roznica)

def euklides(a, b):
    wieksza, mniejsza, roznica = tworzPare(a,b)
    while(roznica != 0):
        wieksza, mniejsza, roznica = tworzPare(roznica, mniejsza)  
    return wieksza
    
class testEuklidesa(unittest.TestCase):
    def test1(self):
        self.assertEqual(51, euklides(1989, 867))
        self.assertEqual(51, euklides(867, 1989 ))

if __name__ == "__main__":
    unittest.main()
    
