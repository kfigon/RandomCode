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

# list of building's heights facing west. Any buildings on easat with equal or greater height cant view the sunset
# return buildings that can see the sunset

# processing from right to left will require a stack of candidates, Stack is to acomodate the ordering
def buildingsWithSunsetView(buildings: List[int]) -> List[int]:
    maks = buildings[0]
    out = []
    out.append(buildings[0])

    for v in buildings[1:]:
        if v > maks:
            out.append(v)
        maks = max(maks, v)
    return out

class TestStack(unittest.TestCase):
    def testMatchingParenthesis(self):
        data = [
            ('[][]()(){}', True),
            ('[([])]', True),
            ('[({[]})]', True),
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

    def testBuildingHeights(self):
        data = [
            ([1,2,3], [1,2,3]),
            ([1,3,2], [1,3]),
            ([1,2,3,4,1], [1,2,3,4]),
            ([1,2,3,4,1,6], [1,2,3,4,6]),
            ([2,2,3,4,1,6], [2,3,4,6]),
            ([3,3,1,3,3], [3]),
        ]
        for d in data:
            with self.subTest(d[0]):
                self.assertEqual(d[1], buildingsWithSunsetView(d[0]))

if __name__ == "__main__":
    unittest.main()