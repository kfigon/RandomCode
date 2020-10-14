from typing import List

# given array and a number find
# maximum sum of subarray of length passed

# subarray must consist of consecutive elements

# O(n)
def maxSubarraySum(tab: List[int], x: int) -> int:
    if len(tab) < x:
        raise Exception(f'provided array {len(tab)}, wanted subArray: {x}')
    suma = 0
    for i in range(x):
        suma += tab[i]
    
    newSum = suma
    for i in range(x, len(tab)):
        newSum = newSum + tab[i] - tab[i-x]
        suma = max(newSum, suma)
    return suma

assert maxSubarraySum([1,2,3],3) == 6
assert maxSubarraySum([100,200,300,400],2) == 700
assert maxSubarraySum([1,4,2,10,23,3,1,0,20],4) == 39
assert maxSubarraySum([-3,4,0,-2,6,-1],2) == 5
assert maxSubarraySum([-3,-1,-2,-3],2) == -3
assert maxSubarraySum([3,-2,7,-4,1,-1,4,-2,1],2) == 5

try:
    maxSubarraySum([2,3], 3)
    assert False
except Exception:
    pass # ok