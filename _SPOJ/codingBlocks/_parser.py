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



data = '''centered_average([1, 2, 3, 4, 100]) → 3	None	X	
centered_average([1, 1, 5, 5, 10, 8, 7]) → 5	None	X	
centered_average([-10, -4, -2, -4, -2, 0]) → -3	None	X	
centered_average([5, 3, 4, 6, 2]) → 4	None	X	
centered_average([5, 3, 4, 0, 100]) → 4	None	X	
centered_average([100, 0, 5, 3, 4]) → 4	None	X	
centered_average([4, 0, 100]) → 4	None	X	
centered_average([0, 2, 3, 4, 100]) → 3	None	X	
centered_average([1, 1, 100]) → 1	None	X	
centered_average([7, 7, 7]) → 7	None	X	
centered_average([1, 7, 8]) → 7	None	X	
centered_average([1, 1, 99, 99]) → 50	None	X	
centered_average([1000, 0, 1, 99]) → 50	None	X	
centered_average([4, 4, 4, 4, 5]) → 4	None	X	
centered_average([4, 4, 4, 1, 5]) → 4	None	X	
centered_average([6, 4, 8, 12, 3]) → 6	None	X	'''

robPlik(r'centeredAverage.py', 'CenteredAverage', data)