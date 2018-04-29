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



data = '''lucky_sum(1, 2, 3) → 6	None	X	
lucky_sum(1, 2, 13) → 3	None	X	
lucky_sum(1, 13, 3) → 1	None	X	
lucky_sum(1, 13, 13) → 1	None	X	
lucky_sum(6, 5, 2) → 13	None	X	
lucky_sum(13, 2, 3) → 0	None	X	
lucky_sum(13, 2, 13) → 0	None	X	
lucky_sum(13, 13, 2) → 0	None	X	
lucky_sum(9, 4, 13) → 13	None	X	
lucky_sum(8, 13, 2) → 8	None	X	
lucky_sum(7, 2, 1) → 10	None	X	
lucky_sum(3, 3, 13) → 6	None	X'''

robPlik(r'C:\Users\Kamil\Desktop\skrypty\RandomCode\_SPOJ\codingBlocks\test.py', 'TestLuckySum', data)