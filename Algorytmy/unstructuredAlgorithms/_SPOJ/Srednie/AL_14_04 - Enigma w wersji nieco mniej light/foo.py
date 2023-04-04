__author__ = 'kamil'

import unittest

def enigmaLight(napis):
    out = ""
    for i in range(0, len(napis), 2):
        pierwszy = napis[i]
        drugi=""
        if(i < len(napis)-1):
            drugi = napis[i+1]
        out+=drugi+pierwszy
    return out

class TestDeszyfratora1(unittest.TestCase):
    def test1(self):
        self.assertEqual("ALA MA KOTA", enigmaLight("LA AAMK TOA"))
    def test2(self):
        self.assertEqual("BOLEK I LOLEK", enigmaLight("OBEL K IOLELK"))
    def test3(self):
        self.assertEqual("ENIGMA W WERSJI LIGHT", enigmaLight("NEGIAMW W REJS IILHGT"))
    def test4(self):
        self.assertEqual("SPRYCIARZ Z CIEBIE JASIU", enigmaLight("PSYRICRA Z ZICBEEIJ SAUI"))

def enigmaMniejLight(napis):
    return napis

class TestDeszyfratora2(unittest.TestCase):
    def test1(self):
        self.assertEqual("ALA MA KOTA", enigmaMniejLight("AL AM OKATA"))
    def test2(self):
        self.assertEqual("BOLEK I LOLEK", enigmaMniejLight("BEL KI OLELOK"))
    def test3(self):
        self.assertEqual("ENIGMA W WERSJI NIECO MNIEJ LIGHT", enigmaMniejLight("INAGM  WEWIRSJ INEOC IMNE JILEGHT"))

if __name__ == '__main__':
    unittest.main()
