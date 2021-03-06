import unittest
from typing import List


class Test(unittest.TestCase):
    def testMultiplication(self):
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
            {'a': "98745321456", 'b': "3", 'exp': "296235964368"},
            {'a': "123432798654", 'b': "1", 'exp': "123432798654"},
            {'a': "123432798654", 'b': "8", 'exp': "987462389232"},
            {'a' :"798654",'b': "231456",'exp': "184853260224"},
            {'a' :"123432798654",'b': "231456",'exp': "28569261845260224"},
            {'a' :"123432798654",'b': "6",'exp': "740596791924"},
            {'a' :"123432798654",'b': "56",'exp': "6912236724624"},
            {'a' :"123432798654",'b': "456",'exp': "56285356186224"},
            {'a' :"123432798654",'b': "1456",'exp': "179718154840224"},
            {'a' :"123432798654",'b': "31456",'exp': "3882702114460224"},
            {'a' :"12343",'b': "31456",'exp': "388261408"},
            {'a' :"231456",'b': "123432798654",'exp': "28569261845260224"},
            {'a' :"123654465789541326546231564",'b': "65432123101548589746541325456789564",'exp': "8090974227597496808946050339263853168202079858417041962598096"},
        ]
        for tc in cases:
            testName = tc['a'] + '*' +tc['b']
            with self.subTest(testName):
                res = multiply(tc['a'], tc['b'])
                self.assertEqual(tc['exp'], res)

    def testAddition(self):
        cases = [
            {'a' :"", 'b': "", 'exp': ""},
            {'a' :"1",'b': "", 'exp': "1"},
            {'a' :"", 'b': "1",'exp': "1"},
            {'a' :"2",'b': "3",'exp': "5"},
            {'a' :"12",'b': "3",'exp': "15"},
            {'a' :"3",'b': "12",'exp': "15"},
            {'a' :"9",'b': "12",'exp': "21"},
            {'a' :"12",'b': "9",'exp': "21"},
            {'a' :"1234",'b': "5678",'exp': "6912"},
            {'a' :"5678",'b': "1234",'exp': "6912"},
            {'a' :"798654",'b': "231456",'exp': "1030110"},
            {'a' :"231456",'b': "798654",'exp': "1030110"},
            {'a' :"123432798654",'b': "231456",'exp': "123433030110"},
            {'a' :"231456",'b': "123432798654",'exp': "123433030110"},
            {'a' :"123654465789541326546231564",'b': "65432123101548589746541325456789564",'exp': "65432123225203055536082652003021128"},
            {'a' :"94368",'b': "1258240",'exp': "1352608"},
            {'a' :"1352608",'b': "9436800",'exp': "10789408"},
            {'a' :"10789408",'b': "62912000",'exp': "73701408"},
            {'a' :"73701408",'b': "314560000",'exp': "388261408"},
            {'a' :"62912",'b': "943680",'exp': "1006592"},
            {'a' :"943680",'b': "62912",'exp': "1006592"},
        ]
        for tc in cases:
            testName = tc['a'] + '+' +tc['b']
            with self.subTest(testName):
                res = addNumbers(tc['a'], tc['b'])
                self.assertEqual(tc['exp'], res)

    def testPartialResults(self):
        partials = [94368, 1258240, 9436800, 62912000, 314560000]
        partialsStr = list(map(lambda x: str(x), partials))
        self.assertEqual(388261408, sum(partials))
        self.assertEqual('388261408', sumPartialResults(partialsStr))

def multiply(a: str, b: str) -> str:
    if len(a) == 0 or len(b) == 0:
        return ''

    partialResults: List[str] = []
    aIdx = len(a)-1
    iterationNum = 0
    while aIdx >= 0:
        charA = str(a[aIdx])
        out = calculateSingleRow(b, charA) + ('0'*iterationNum)
        partialResults.append(out)
        aIdx-=1
        iterationNum+=1

    print(f'{a}*{b} -> {partialResults}')
    return sumPartialResults(partialResults)

def calculateSingleRow(b: str, charA: str) -> str:
    out = ''
    carry = 0
    bIdx = len(b)-1
    while bIdx >= 0:
        res = int(charA) * int(b[bIdx]) + carry
        carry = res // 10
        out += str(res % 10)
        bIdx-=1

    if carry != 0:
        out += str(carry)
    return out[::-1]

def sumPartialResults(partialResults: List[str]) -> str:
    out = ''
    for p in partialResults:
        out = addNumbers(out, p)
    return out

def addNumbers(a: str, b:str) -> str:
    if len(a) == 0:
        return b
    elif len(b) == 0:
        return a

    carry = 0
    aIdx, bIdx = len(a)-1, len(b)-1
    out =''
    while aIdx >= 0 and bIdx >= 0:
        res = int(a[aIdx]) + int(b[bIdx]) + carry
        carry = res//10
        out += str(res%10)
        aIdx-=1
        bIdx-=1

    def appendRest(idx, tab, out, carry):
        while idx >= 0:
            res = int(tab[idx]) + carry
            out += str(res%10)
            carry = res//10
            idx-=1
        return out, carry

    out, carry = appendRest(aIdx, a, out, carry)
    out, carry = appendRest(bIdx, b, out, carry)

    if carry != 0:
        out += str(carry)

    returnStr = out[::-1]
    return returnStr


if __name__ == '__main__':
    unittest.main()
