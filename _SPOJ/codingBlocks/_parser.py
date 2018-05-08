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



data = '''close_far(1, 2, 10) → True	None	X	
close_far(1, 2, 3) → False	None	X	
close_far(4, 1, 3) → True	None	X	
close_far(4, 5, 3) → False	None	X	
close_far(4, 3, 5) → False	None	X	
close_far(-1, 10, 0) → True	None	X	
close_far(0, -1, 10) → True	None	X	
close_far(10, 10, 8) → True	None	X	
close_far(10, 8, 9) → False	None	X	
close_far(8, 9, 10) → False	None	X	
close_far(8, 9, 7) → False	None	X	
close_far(8, 6, 9) → True	None	X'''

robPlik(r'test.py', 'TestCloseFar', data)