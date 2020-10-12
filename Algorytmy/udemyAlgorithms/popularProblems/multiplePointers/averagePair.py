from typing import List, Callable

# given sorted array of ints and target average
# determine if there is a pair of values that average equals target average

# O(n)
def averagePair(tab: List[int], av: float) -> bool:
    i = 0
    end = len(tab) - 1
    
    while i < end:
        currentAvg = (tab[i] + tab[end])/2
        if currentAvg < av:
            i+=1
        elif currentAvg > av:
            end-=1
        else:
            return True
    return False


def averagePair2(tab: List[int], av: float) -> bool:
    toFind :Callable[[float], float] = lambda x: 2*av - x
    for i in tab:
        if toFind(i) in tab:
            return True
    return False

# O(n^2)
def averagePairBrute(tab: List[int], av: float) -> bool:
    for i in range(len(tab)):
        for j in range(i+1, len(tab)):
            if (tab[i] + tab[j])/2 == av:
                return True
    return False

assert averagePairBrute([1,2,3], 2.5) == True
assert averagePairBrute([1,2,3,4,5,6], 3.5) == True
assert averagePairBrute([1,3,3,5,6,7,10,12,19], 8) == True
assert averagePairBrute([-1,0,3,4,5,6], 4.1) == False
assert averagePairBrute([1,1,1,1,1,1,1,1,1,1,1,19], 2) == False
assert averagePairBrute([1,1,1,1,1,1,1,1,1,1,1,19], 1) == True
assert averagePairBrute([1,1,1,1,1,1,1,1,1,1,1,19], 10) == True
assert averagePairBrute([], 4) == False

assert averagePair2([1,2,3], 2.5) == True
assert averagePair2([1,2,3,4,5,6], 3.5) == True
assert averagePair2([1,3,3,5,6,7,10,12,19], 8) == True
assert averagePair2([-1,0,3,4,5,6], 4.1) == False
assert averagePair2([1,1,1,1,1,1,1,1,1,1,1,19], 2) == False
assert averagePair2([1,1,1,1,1,1,1,1,1,1,1,19], 1) == True
assert averagePair2([1,1,1,1,1,1,1,1,1,1,1,19], 10) == True
assert averagePair2([], 4) == False

assert averagePair([1,2,3], 2.5) == True
assert averagePair([1,2,3,4,5,6], 3.5) == True
assert averagePair([1,3,3,5,6,7,10,12,19], 8) == True
assert averagePair([-1,0,3,4,5,6], 4.1) == False
assert averagePair([1,1,1,1,1,1,1,1,1,1,1,19], 2) == False
assert averagePair([1,1,1,1,1,1,1,1,1,1,1,19], 1) == True
assert averagePair([1,1,1,1,1,1,1,1,1,1,1,19], 10) == True
assert averagePair([], 4) == False

print('ok')