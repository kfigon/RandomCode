from typing import List
from math import log10, floor

# best average compared to all sorts - but it's only for numbers

# only for integers, not using comparison
# radixSort uses special property of numbers

# if number has more digits - it's bigger

# create 10 buckets - each for each number in radix 10
# for every spot in each number e.g. 1556 - 6; 4-4 
# group them into buckets
# then sort by buckets (but not inside a bucket)
# repeat for next digit in number
# this implementation is only for positive numbers

# or we can use strings
def extractDigit(a: int, place: int) -> int:
    return (abs(a)//(10**place)) % 10

class Bucket:
    def __init__(self, idx: int):
        self.idx = idx
        self.nums: List[int] = []
    def add(self, num: int):
        self.nums.append(num)

def digitCount(x: int) -> int:
    return 1 if x==0 else floor(log10(abs(x))) + 1
    # i = 1
    # while True:
    #     if (x - 10**i) < 0:
    #         return i
    #     i += 1
    # return i

# O(nk) n - dlugosc arraya, k - ile cyfr 
def radixSort(tab: List[int]) -> List[int]:
    out: List[int] = [i for i in tab]
    maxRadix = max([digitCount(i) for i in tab])

    for radix in range(maxRadix):
        buckets: List[Bucket] = [Bucket(i) for i in range(10)]

        for i in out:
            dig = extractDigit(i, radix)
            buckets[dig].add(i)

        out.clear()
        for b in buckets:
            out += b.nums

    return out    

assert digitCount(1) == 1
assert digitCount(12) == 2
assert digitCount(123) == 3
assert digitCount(1234) == 4

assert extractDigit(19385, 0) == 5
assert extractDigit(19385, 1) == 8
assert extractDigit(19385, 2) == 3
assert extractDigit(19385, 3) == 9
assert extractDigit(19385, 4) == 1
assert extractDigit(19385, 5) == 0
assert extractDigit(19385, 6) == 0
assert extractDigit(-1234, 0) == 4
assert extractDigit(-1234, 1) == 3
assert extractDigit(-1234, 2) == 2
assert extractDigit(-1234, 3) == 1
assert extractDigit(-1234, 4) == 0

assert radixSort([1556,4,3556,593,408,4386,902,7,8157,9637,29]) == [4,7,29,408,593,902,1556,3556,4386,8157,9637]
assert radixSort([8,3,5,4,7,6,1,2]) == [1,2,3,4,5,6,7,8]
assert radixSort([5,3,4,2,6,1]) == [1,2,3,4,5,6]
assert radixSort([i for i in range(20)]) == [i for i in range(20)]
assert radixSort([i for i in range(30,-1,-1)]) == [i for i in range(31)]
assert radixSort([i for i in range(1000000,-1,-1)]) == [i for i in range(1000001)]
print('radix ok')