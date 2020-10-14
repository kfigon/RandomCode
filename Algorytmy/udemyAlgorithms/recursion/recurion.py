from typing import List

# take a problem and solve for smaller set
# until you hit some base condition

# check if any of number is odd
def isAnyOdd(tab: List[int]) -> bool:
    if len(tab) == 1:
        return tab[0] % 2 == 1
    return (tab[0] % 2 == 1) or isAnyOdd(tab[1:])

assert isAnyOdd([1,2,3,4,5])
assert not isAnyOdd([2,4,6,0])
assert isAnyOdd([22,2,4,4,1])
assert isAnyOdd([22,2,1,4,4])


def countDown(num: int):
    if num <= 0:
        print(num)
        return
    print(num)
    num-=1
    countDown(num)

def sumRange(num: int) -> int:
    if num == 1:
        return 1
    return num + sumRange(num-1)

assert sumRange(5) == 15
assert sumRange(4) == 10
assert sumRange(3) == 6
assert sumRange(30) == 465


def factorial(num: int) -> int:
    if num == 1:
        return 1
    return num * factorial(num-1)

assert factorial(1) == 1
assert factorial(2) == 2
assert factorial(3) == 6
assert factorial(4) == 24
assert factorial(5) == 120

# with closure to store data
def collectOdd(tab: List[int]) -> List[int]:
    out: List[int] = []

    def collectOddInternal(x: List[int]):
        if len(x) == 0:
            return
        if x[0] % 2 == 1:
            out.append(x[0])
        collectOddInternal(x[1:])
    
    collectOddInternal(tab)
    return out

assert collectOdd([1,2,3,4,5,6]) == [1,3,5]

def collectOddPure(tab: List[int]) -> List[int]:
    newArray = []
    if len(tab) == 0:
        return newArray
    if tab[0] % 2 == 1:
        newArray.append(tab[0])
    
    # concat
    return newArray + collectOddPure(tab[1:])

print(collectOddPure([1,2,3,4,5,6,7]))