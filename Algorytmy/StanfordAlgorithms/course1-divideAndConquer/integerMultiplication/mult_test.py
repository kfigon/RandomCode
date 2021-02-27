import unittest
from typing import List


class Test(unittest.TestCase):
    def test(self):
        cases = [
            {'a' :"", 'b': "", 'exp': ""},
            {'a' :"1",'b': "", 'exp': ""},
            {'a' :"", 'b': "1",'exp': ""},
            {'a' :"2",'b': "3",'exp': "6"},
            {'a' :"12",'b': "3",'exp': "36"},
            {'a' :"3",'b': "12",'exp': "36"},
            {'a' :"9",'b': "12",'exp': "108"},
            {'a' :"12",'b': "9",'exp': "108"},
            {'a' :"1234",'b': "5678",'exp': "7006652"},
            {'a' :"5678",'b': "1234",'exp': "7006652"},
            {'a' :"798654",'b': "231456",'exp': "184853260224"},
            {'a' :"123432798654",'b': "231456",'exp': "28569261845260224"},
            {'a' :"231456",'b': "123432798654",'exp': "28569261845260224"},
            {'a' :"123654465789541326546231564",'b': "65432123101548589746541325456789564",'exp': "8090974227597496808946050339263853168202079858417041962598096"},
        ]
        for tc in cases:
            testName = tc['a'] + '*' +tc['b']
            with self.subTest(testName):
                res = multiply(tc['a'], tc['b'])
                self.assertEqual(tc['exp'], res)

def multiply(a: str, b: str) -> str:
    if len(a) == 0 or len(b) == 0:
        return ''

    partialResults: List[str] = []
    aIdx = 0
    while aIdx < len(a):
        charA = str(a[aIdx])
        out = calculateSingleRow(b, charA)
        partialResults.append(out)
        aIdx+=1

    print(f'{a}*{b} -> {partialResults}')
    return sumPartialResults(partialResults)

def sumPartialResults(partialResults: List[str]) -> str:
    return partialResults[0]

def calculateSingleRow(b: str, charA: str) -> str:
    out = ''
    carry = 0
    for charB in b:
        res = int(charA) * int(charB) + carry
        if res >= 10:
            carry = res // 10
        out += str(res % 10)

    if carry != 0:
        out += str(carry)
    return out


if __name__ == '__main__':
    unittest.main()
