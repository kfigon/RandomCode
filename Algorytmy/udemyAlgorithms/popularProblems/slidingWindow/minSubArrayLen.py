from typing import List

# array of positive ints and positive int
# return minimal length of contiguous subarray
# which the sum is greater or equal to provided integer
# if no - return 0

# O(n)
def minSubArrayLen(tab: List[int], desiredSum:int) -> int:
    startIdx = 0
    stopIdx = 1
    suma = tab[startIdx] + tab[stopIdx]
    minSubArray = len(tab)
    while stopIdx < len(tab):
        if suma < desiredSum:
            stopIdx += 1
            if stopIdx < len(tab):
                suma += tab[stopIdx]
        else:
            minSubArray = min(minSubArray, (stopIdx-startIdx+1))
            suma = suma - tab[startIdx]
            startIdx+=1

    return 0 if minSubArray==len(tab) else minSubArray

assert minSubArrayLen([2,3,1,2,4,3], 7) == 2
assert minSubArrayLen([2,1,6,5,4], 9) == 2
assert minSubArrayLen([2,3,1,2,4,3], 5) == 2
assert minSubArrayLen([3,1,7,11,2,9,8,21,62,33,19], 52) == 1
assert minSubArrayLen([1,4,16,22,5,7,8,9,10], 39) == 3
assert minSubArrayLen([1,4,16,22,5,7,8,9,10], 55) == 5
assert minSubArrayLen([4,3,3,8,1,2,3], 11) == 2
assert minSubArrayLen([1,4,16,22,5,7,8,9,10], 95) == 0
