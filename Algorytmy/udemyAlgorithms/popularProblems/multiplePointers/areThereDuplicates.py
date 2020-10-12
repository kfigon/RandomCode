from typing import List
# mozna tez podejscie frequencyCounter zrobic!

# check wheter there are duplicates in array

# O(nlogn)
def areThereDuplicates(tab: List[int]) -> bool:
    tab.sort()
    i = 0
    while(i < len(tab)-1):
        if tab[i] == tab[i+1]:
            return True
        i+=1
    return False

def areThereDuplicates2(tab: List[int]) -> bool:
    return len(set(tab)) != len(tab)

assert areThereDuplicates([1,2,3]) == False
assert areThereDuplicates([1,2,2]) == True
assert areThereDuplicates([1,2,3,1]) == True
assert areThereDuplicates([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]) == False
assert areThereDuplicates([1,2,3,4,5,6,7,8,9,10,11,12,13,14,6,15,16,17,18,19,20]) == True

assert areThereDuplicates2([1,2,3]) == False
assert areThereDuplicates2([1,2,2]) == True
assert areThereDuplicates2([1,2,3,1]) == True
assert areThereDuplicates2([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]) == False
assert areThereDuplicates2([1,2,3,4,5,6,7,8,9,10,11,12,13,14,6,15,16,17,18,19,20]) == True