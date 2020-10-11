from typing import List, Dict

# return true if every value in the array has it's corresponding value
# squared in the second array
# frequency of values must be the same

def howMany(val: int, b: List[int]) -> int:
    return len(list(filter(lambda x: x == val, b)))

# O(n^3)
def sameBrute(a: List[int], b: List[int]) -> bool:
    for i in range(len(a)):
        if howMany(a[i], a) != howMany(a[i]**2, b):
            return False
    return True

# lepsze - mniej petli
# O(n^2)
def sameBrute2(a: List[int], b: List[int]) -> bool:
    for i in range(len(a)):
        if (a[i]**2) not in b:
            return False
        b.remove(a[i]**2)
    return True

def countFreq(a: List[int]) -> Dict[int, int]:
    out : Dict[int, int] = {}
    for i in a:
        out[i] = 1 if i not in out else out[i] + 1
    return out

# 2 petle sa lepsze niz nested!
# O(3n) -> O(n)
def same(a: List[int], b: List[int]) -> bool:
    if len(a) != len(b):
        return False
    freqA = countFreq(a)
    freqB = countFreq(b)

    for key in freqA:
        # search for key is fast!
        if key**2 not in freqB:
            return False

        vA = freqA[key]
        vB = freqB[key**2]
        if vA != vB:
            return False
    return True
        

assert howMany(1, [1,2,3]) == 1
assert howMany(2, [1,2,3]) == 1
assert howMany(1, [1,2,1]) == 2

assert sameBrute([1,2,3], [4,1,9]) == True
assert sameBrute([1,2,3], [1,9]) == False
assert sameBrute([1,2,1], [4,4,1]) == False
assert sameBrute([1,2,1], [4,1,1]) == True
assert sameBrute([1,2,3,2], [9,1,4,4]) == True

assert sameBrute2([1,2,3], [4,1,9]) == True
assert sameBrute2([1,2,3], [1,9]) == False
assert sameBrute2([1,2,1], [4,4,1]) == False
assert sameBrute2([1,2,1], [4,1,1]) == True
assert sameBrute2([1,2,3,2], [9,1,4,4]) == True

assert same([1,2,3], [4,1,9]) == True
assert same([1,2,3], [1,9]) == False
assert same([1,2,1], [4,4,1]) == False
assert same([1,2,1], [4,1,1]) == True
assert same([1,2,3,2], [9,1,4,4]) == True



