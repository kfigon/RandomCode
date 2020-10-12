from typing import List

# input - ciagle dane
# szukamy subsetu (ciaglego) w zbiorze
# przesuwamy okno w zaleznosci od warunku

def subSum(tab: List[int], start: int, end: int) -> int:
    suma = 0
    for i in range(start, end):
        suma += tab[i]
    return suma

# max sum of n consecutive elements
# O(n)
def maxSubarraySum(tab: List[int], n: int) -> int:
    if n > len(tab):
        return 0

    suma = subSum(tab, 0, n)
    prevSuma = suma
    for i in range(n, len(tab)):
        prevSuma = prevSuma + tab[i] - tab[i-n]
        suma = max(prevSuma, suma)
    return suma

assert maxSubarraySum([1,2,5,2,8,1,5],2) == 10
assert maxSubarraySum([1,2,5,2,8,1,5],4) == 17
assert maxSubarraySum([2,6,9,2,1,8,5,6,3],3) == 19
assert maxSubarraySum([4,2,1,6],1) == 6
assert maxSubarraySum([4,2,1,6],4) == 13
assert maxSubarraySum([-4,-2,-1,-6],4) == -13
assert maxSubarraySum([],4) == 0
