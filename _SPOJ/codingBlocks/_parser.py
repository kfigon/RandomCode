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



data = '''end_other('Hiabc', 'abc') → True	None	X	
end_other('AbC', 'HiaBc') → True	None	X	
end_other('abc', 'abXabc') → True	None	X	
end_other('Hiabc', 'abcd') → False	None	X	
end_other('Hiabc', 'bc') → True	None	X	
end_other('Hiabcx', 'bc') → False	None	X	
end_other('abc', 'abc') → True	None	X	
end_other('xyz', '12xyz') → True	None	X	
end_other('yz', '12xz') → False	None	X	
end_other('Z', '12xz') → True	None	X	
end_other('12', '12') → True	None	X	
end_other('abcXYZ', 'abcDEF') → False	None	X	
end_other('ab', 'ab12') → False	None	X	
end_other('ab', '12ab') → True	None	X	'''

robPlik(r'endOther.py', 'EndOther', data)