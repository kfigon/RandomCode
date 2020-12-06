from typing import List, Dict

# given an array of positive ints, some elements appear
# twice, others once. Find all elements that appear twice

# O(n)
def findAllDuplicates(ar: List[int]) -> List[int]:
    d: Dict[int, int] = {}
    for i in ar:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    
    out: List[int] = []
    for key in d:
        if d[key] == 2:
            out.append(key)
    return out

assert findAllDuplicates([4,3,2,7,8,2,3,1]) == [3,2]
assert findAllDuplicates([4,3,2,1,0]) == []
assert findAllDuplicates([4,3,2,1,0,1,2,3]) == [3,2,1]