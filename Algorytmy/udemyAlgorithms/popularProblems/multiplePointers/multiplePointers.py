from typing import List, Optional

# mamy plaska strukture (np. tablice)
# i szukamy 2 wartosci wg jakichs regul
# uzywamy wtedy 2 indeksow/pointerow i przesuwamy do srodka/konca

# sumZero
# input - sorted list of ints
# find first pair when the sum is 0

# wykorzystajmy ze sa posortowane i jedzmy od poczatku i od konca jednoczesnie
# O(n/2) -> O(n)
def sumZero(tab: List[int]) -> Optional[List[int]]:
    startIdx = 0
    endIdx = len(tab)-1
    while startIdx < endIdx:
        suma = tab[startIdx] + tab[endIdx]
        if suma > 0:
            endIdx-=1
        elif suma < 0:
            startIdx +=1
        else:
            return [tab[startIdx], tab[endIdx]]

    return None

# O(n^2) - prawie, bo kolejne iteracje sa skrocone. Ale nadal dlugo
def sumZeroBrute(tab: List[int]) -> Optional[List[int]]:
    for i in range(len(tab)):
        for j in range(i+1, len(tab)):
            if tab[i] + tab[j] == 0:
                return [tab[i], tab[j]]
    return None

assert sumZeroBrute([-3,-2,-1,0,1,2,3]) == [-3,3]
assert sumZeroBrute([-2,0,1,3]) == None
assert sumZeroBrute([1,2,3]) == None
assert sumZeroBrute([-4,-3,-2,-1,0,1,2,5]) == [-2,2]
assert sumZeroBrute([-4,-3,-2,-1,0,1,2,3,10]) == [-3,3]

assert sumZero([-3,-2,-1,0,1,2,3]) == [-3,3]
assert sumZero([-2,0,1,3]) == None
assert sumZero([1,2,3]) == None
assert sumZero([-4,-3,-2,-1,0,1,2,5]) == [-2,2]
assert sumZero([-4,-3,-2,-1,0,1,2,3,10]) == [-3,3]

print('ok')
