def parsujLinijke(linijka):
    frazy = linijka.split(' → ')
    logic = frazy[1].split('\t')[0]
    return ('self.assertEqual({}, {})'.format(logic, frazy[0]))
    
def parser(napis):
    out = []
    linijki = napis.split('\n')
    for i in linijki:
        out.append(parsujLinijke(i))
    return out

def robPlik(nazwaPliku, nazwaTestu, napis):
    with open(nazwaPliku, mode='w') as plik:
        plik.write('import unittest\n')
        plik.write('class Test'+nazwaTestu+"(unittest.TestCase):\n")
        testKejsy = parser(napis)
        for i,t in enumerate(testKejsy):
            plik.write('    def test'+str(i)+'(self):\n')
            plik.write('        '+t+'\n')
        
        plik.write("if __name__=='__main__':\n")
        plik.write("    unittest.main()")



data = '''cat_dog('catdog') → True	None	X	
cat_dog('catcat') → False	None	X	
cat_dog('1cat1cadodog') → True	None	X	
cat_dog('catxxdogxxxdog') → False	None	X	
cat_dog('catxdogxdogxcat') → True	None	X	
cat_dog('catxdogxdogxca') → False	None	X	
cat_dog('dogdogcat') → False	None	X	
cat_dog('dogogcat') → True	None	X	
cat_dog('dog') → False	None	X	
cat_dog('cat') → False	None	X	
cat_dog('ca') → True	None	X	
cat_dog('c') → True	None	X	
cat_dog('') → True	None	X	'''

robPlik(r'countCatDog.py', 'TestCatDog', data)