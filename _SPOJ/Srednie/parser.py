def parsujLinijke(linijka):
    frazy = linijka.split(' → ')
    logic = frazy[1].split('\t')[0]
    return ('self.assert{}({})'.format(logic, frazy[0]))
    
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
        
        plik.write("if _name__=='__main_':\n")
        plik.write("    unittest.main()")



data = '''make_bricks(3, 1, 8) → True	None	X	
make_bricks(3, 1, 9) → False	None	X	
make_bricks(3, 2, 10) → True	None	X	
make_bricks(3, 2, 8) → True	None	X	
make_bricks(3, 2, 9) → False	None	X	
make_bricks(6, 1, 11) → True	None	X	
make_bricks(6, 0, 11) → False	None	X	
make_bricks(1, 4, 11) → True	None	X	
make_bricks(0, 3, 10) → True	None	X	
make_bricks(1, 4, 12) → False	None	X	
make_bricks(3, 1, 7) → True	None	X	
make_bricks(1, 1, 7) → False	None	X	
make_bricks(2, 1, 7) → True	None	X	
make_bricks(7, 1, 11) → True	None	X	
make_bricks(7, 1, 8) → True	None	X	
make_bricks(7, 1, 13) → False	None	X	
make_bricks(43, 1, 46) → True	None	X	
make_bricks(40, 1, 46) → False	None	X	
make_bricks(40, 2, 47) → True	None	X	
make_bricks(40, 2, 50) → True	None	X	
make_bricks(40, 2, 52) → False	None	X	
make_bricks(22, 2, 33) → False	None	X	
make_bricks(0, 2, 10) → True	None	X	
make_bricks(1000000, 1000, 1000100) → True	None	X	
make_bricks(2, 1000000, 100003) → False	None	X	
make_bricks(20, 0, 19) → True	None	X	
make_bricks(20, 0, 21) → False	None	X	
make_bricks(20, 4, 51) → False	None	X	
make_bricks(20, 4, 39) → True	None'''

robPlik(r'C:\Users\Kamil\Desktop\skrypty\RandomCode\_SPOJ\Srednie\bricks\test.py', 'TestBricks', data)