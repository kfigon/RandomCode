from typing import Tuple

class Num:
    def __init__(self, n: str):
        assert len(n) >= 1
        self.n = n
        self.idx = len(self.n)-1

    def nextInt(self) -> int:
        if self.idx < 0:
            return 0
        toRet = int(self.n[self.idx])
        self.idx-=1
        return toRet

    def hasNext(self) -> bool:
        return self.idx >= 0

class Carry:
    def __init__(self, v: int = 0):
        self.carry = v

    def getForRegularUsage(self) -> int:
        return self.carry

    def getForRest(self) -> int:
        toRet = self.carry
        if self.carry != 0:
            self.carry = 0
        return toRet

def extractDigitAndCarry(num: int) -> Tuple[int, Carry]:
    return num % 10, Carry(num // 10)

def add(a: str, b: str) -> str:
    out = ''
    aNum, bNum = Num(a), Num(b)
    carry = Carry()
    while aNum.hasNext() and bNum.hasNext():
        res = aNum.nextInt() + bNum.nextInt() + carry.getForRegularUsage()
        
        digRes,carry = extractDigitAndCarry(res)
        out += str(digRes)

    def addRest(num: Num, out: str, carr: Carry) -> str:
        while num.hasNext():
            out += str(num.nextInt() + carr.getForRest())
        return out

    out = addRest(aNum, out, carry)
    out = addRest(bNum, out, carry)

    out = out[::-1] # reverse string
    print(f'{a} + {b} = {out}')
    return out

assert add('123', '1') == '124'
assert add('123', '5') == '128'
assert add('123', '9') == '132'
assert add('123', '12') == '135'
assert add('123', '645') == '768'
assert add('123', '698') == '821'
assert add('123', '1698') == '1821'
assert add('9876541564', '21456654132') == str(9876541564 + 21456654132)

print('all gut')