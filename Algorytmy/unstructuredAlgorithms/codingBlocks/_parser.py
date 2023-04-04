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



data = '''has22([1, 2, 2]) → True	None	X	
has22([1, 2, 1, 2]) → False	None	X	
has22([2, 1, 2]) → False	None	X	
has22([2, 2, 1, 2]) → True	None	X	
has22([1, 3, 2]) → False	None	X	
has22([1, 3, 2, 2]) → True	None	X	
has22([2, 3, 2, 2]) → True	None	X	
has22([4, 2, 4, 2, 2, 5]) → True	None	X	
has22([1, 2]) → False	None	X	
has22([2, 2]) → True	None	X	
has22([2]) → False	None	X	
has22([]) → False	None	X	
has22([3, 3, 2, 2]) → True	None	X	
has22([5, 2, 5, 2]) → False	None	X'''

robPlik(r'asdads.py', 'Has22', data)