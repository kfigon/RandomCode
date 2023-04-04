__author__ = 'kamil'

import unittest
# JGGHACK - Łamacz gg

# Jest rok 2005. Jasiowi udało się przekonać kilku kolegów,
# aby przesłali mu swoje pliki config.dat programu Gadu Gadu.
# Teraz, po znalezieniu potrzebnych informacji w Internecie,
# jest już gotowy do napisania własnego programu deszyfrującego...
# i w ten sposób będzie miał hasła dostępu do kont gadu gadu kolegów...

class LamaczGG:
    def deszyfruj(self, zaszyfrowane):
        out=""
        znakHelper = ZnakHelper()
        for i in range(0,len(zaszyfrowane), 2):
            pierwszyZnak = zaszyfrowane[i]
            drugiZnak = zaszyfrowane[i+1]
            numerPierwszego = znakHelper.numerPierwszegoZnaku(pierwszyZnak)
            numerDrugiego = znakHelper.numerDrugiegoZnaku(drugiZnak)

            out += chr(numerPierwszego+numerDrugiego)
        return out

class ZnakHelper:
    def numerPierwszegoZnaku(self, znak):
        numerZnaku = ord(znak)
        numerPierwszego = ord('A')
        return numerZnaku-numerPierwszego

    def numerDrugiegoZnaku(self, znak):
        numerPierwszego = self.numerPierwszegoZnaku(znak)
        return numerPierwszego*16

class TestyZnakHelpera(unittest.TestCase):
    def setUp(self):
        self.z = ZnakHelper()

    def testPierwszyZnak(self):
        self.assertEqual(0, self.z.numerPierwszegoZnaku('A'))
        self.assertEqual(1, self.z.numerPierwszegoZnaku('B'))
        self.assertEqual(2, self.z.numerPierwszegoZnaku('C'))
        self.assertEqual(3, self.z.numerPierwszegoZnaku('D'))
        self.assertEqual(4, self.z.numerPierwszegoZnaku('E'))
        self.assertEqual(5, self.z.numerPierwszegoZnaku('F'))
        self.assertEqual(6, self.z.numerPierwszegoZnaku('G'))
        self.assertEqual(7, self.z.numerPierwszegoZnaku('H'))
        self.assertEqual(8, self.z.numerPierwszegoZnaku('I'))
        self.assertEqual(9, self.z.numerPierwszegoZnaku('J'))
        self.assertEqual(10, self.z.numerPierwszegoZnaku('K'))
        self.assertEqual(11, self.z.numerPierwszegoZnaku('L'))
        self.assertEqual(12, self.z.numerPierwszegoZnaku('M'))
        self.assertEqual(13, self.z.numerPierwszegoZnaku('N'))
        self.assertEqual(14, self.z.numerPierwszegoZnaku('O'))
        self.assertEqual(15, self.z.numerPierwszegoZnaku('P'))

    def testDrugiZnak(self):
        self.assertEqual(0, self.z.numerDrugiegoZnaku('A'))
        self.assertEqual(16, self.z.numerDrugiegoZnaku('B'))
        self.assertEqual(32, self.z.numerDrugiegoZnaku('C'))
        self.assertEqual(48, self.z.numerDrugiegoZnaku('D'))
        self.assertEqual(64, self.z.numerDrugiegoZnaku('E'))
        self.assertEqual(80, self.z.numerDrugiegoZnaku('F'))
        self.assertEqual(96, self.z.numerDrugiegoZnaku('G'))
        self.assertEqual(112, self.z.numerDrugiegoZnaku('H'))
        self.assertEqual(128, self.z.numerDrugiegoZnaku('I'))
        self.assertEqual(144, self.z.numerDrugiegoZnaku('J'))
        self.assertEqual(160, self.z.numerDrugiegoZnaku('K'))
        self.assertEqual(176, self.z.numerDrugiegoZnaku('L'))
        self.assertEqual(192, self.z.numerDrugiegoZnaku('M'))
        self.assertEqual(208, self.z.numerDrugiegoZnaku('N'))
        self.assertEqual(224, self.z.numerDrugiegoZnaku('O'))
        self.assertEqual(240, self.z.numerDrugiegoZnaku('P'))

class TestyLamaczaGG(unittest.TestCase):
    def testySpoj1(self):
        lamacz = LamaczGG()
        self.assertEqual("abcdefghij", lamacz.deszyfruj("BGCGDGEGFGGGHGIGJGKG"))

    def testySpoj2(self):
        lamacz = LamaczGG()
        self.assertEqual("katastrofa", lamacz.deszyfruj("LGBGEHBGDHEHCHPGGGBG"))

    def testySpoj3(self):
        lamacz = LamaczGG()
        self.assertEqual("obozowisko", lamacz.deszyfruj("PGCGPGKHPGHHJGDHLGPG"))

    def testyPrzyklad(self):
        lamacz = LamaczGG()
        self.assertEqual("Error5", lamacz.deszyfruj("FECHCHPGCHFD"))

if __name__ == '__main__':
    unittest.main()
