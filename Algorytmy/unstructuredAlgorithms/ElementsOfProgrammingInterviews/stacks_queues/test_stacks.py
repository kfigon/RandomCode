import unittest
from typing import List

def matchingParents(parents: str) -> bool:
    stak = []
    closing = {
        '{': '}',
        '(': ')',
        '[': ']',
    }
    for c in parents:
        if c in closing:
            stak.append(c)
        elif len(c) == 0 or closing[stak.pop()] != c:
            return False
    return len(stak) == 0

def normalisePath(inpt: str) -> str:
    stak: List[str] = []
    for token in inpt.split('/'):
        if token == '' or token =='.':
            continue
        elif token == '..':
            stak.pop()
        else:
            stak.append(token)
    
    return '/'.join(stak)

class TestStack(unittest.TestCase):
    def testMatchingParenthesis(self):
        data = [
            ('[][]()(){}', True),
            ('[([])]', True),
            ('[()[()]([])]', True),
            ('{[(())}', False),
            ('{', False),
            ('[[))', False),
            ('[[}', False),
            ('{[((])}', False),
            ('{[((])', False),
            ('{[(()])}', False),
        ]
        for d in data:
            with self.subTest(d[0]):
                self.assertEqual(d[1], matchingParents(d[0]))

    def testNormalisePath(self):
        data = [
            ('usr/lib/../bin/gcc', 'usr/bin/gcc'),
            ('scripts//./../scripts/awk/././', 'scripts/awk'),
            ('sc//./../tc/awk/././', 'tc/awk'),
        ]
        for d in data:
            with self.subTest(d[0]):
                self.assertEqual(d[1], normalisePath(d[0]))

if __name__ == "__main__":
    unittest.main()