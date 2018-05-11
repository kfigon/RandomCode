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



data = '''xyz_there('abcxyz') → True	None	X	
xyz_there('abc.xyz') → False	None	X	
xyz_there('xyz.abc') → True	None	X	
xyz_there('abcxy') → False	None	X	
xyz_there('xyz') → True	None	X	
xyz_there('xy') → False	None	X	
xyz_there('x') → False	None	X	
xyz_there('') → False	None	X	
xyz_there('abc.xyzxyz') → True	None	X	
xyz_there('abc.xxyz') → True	None	X	
xyz_there('.xyz') → False	None	X	
xyz_there('12.xyz') → False	None	X	
xyz_there('12xyz') → True	None	X	
xyz_there('1.xyz.xyz2.xyz') → False	None	X'''

robPlik(r'xyzThere.py', 'XyzThere', data)