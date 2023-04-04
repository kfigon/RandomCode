# jesli w ciagu sa wiecej niz 2 takie same litery, to piszemy LITERALICZBA
# OPSS -> OPSS
# ABCDEF -> ABCDEF
# ABBCCCDDDDEEEEEFGGHIIJKKKL -> ABBC3D4E5FGGHIIJK3L
# AAAAAAAAAABBBBBBBBBBBBBBBB -> A10B16

import unittest
from typing import List

def compress(x: str) -> str:
    out = ''
    i = 0
    while i < len(x):
        currentChar = x[i]
        
        howManySameCharsAhead = 0
        for idx in range(i+1, len(x)):
            if x[idx] == currentChar:
                howManySameCharsAhead +=1
                
        out += currentChar
        if howManySameCharsAhead >= 2:
            out+=str(howManySameCharsAhead+1)
            i+=howManySameCharsAhead+1
        else:
            i+=1

    return out

class TestFoo(unittest.TestCase):
    def test(self):
        case = [("OPSS", "OPSS"),
        ("ABCDEF","ABCDEF"),
        ("ABBCCCDDDDEEEEEFGGHIIJKKKL","ABBC3D4E5FGGHIIJK3L"),
        ("AAAAAAAAAABBBBBBBBBBBBBBBB","A10B16")]
        for c in case:
            with self.subTest(name=str(c)):
                self.assertEqual(c[1], compress(c[0]))

if __name__ == "__main__":
    unittest.main()
