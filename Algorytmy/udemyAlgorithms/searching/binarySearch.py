from typing import List, TypeVar, Optional

T=TypeVar('T')

states: List[str] = ['Alabama', 'Alaska', 'American Samoa', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware', 'District Of Columbia', 'Federated States Of Micronesia', 'Florida', 'Georgia', 'Guam', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Marshall Islands', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey', 'New Mexico', 'New York', 'North Carolina', 'North Dakota', 'Northern Mariana Islands', 'Ohio', 'Oklahoma', 'Oregon', 'Palau', 'Pennsylvania', 'Puerto Rico', 'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virgin Islands', 'Virginia', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming']

# O(logn)
# must be sorted!
# go in the middle, go left or right if < or > and repeat
# log2(n) - when we double number of elements
# we need to do one more additional step
def binarySearch(tab: List[T], searching: T) -> Optional[int]:
    start = 0
    stop = len(tab)-1
    while start <= stop:
        middle = (stop+start)//2
        # middle = start + (stop-start)//2
        if tab[middle] == searching:
            return middle
        elif tab[middle] > searching:
            stop = middle-1
        else:
            start = middle+1
    return None

assert binarySearch([1,2,3,5,6,7], 4) == None
assert binarySearch([1,2,3,5,6,7], 9) == None
assert binarySearch([1,2,3,5,6,7], -1) == None
assert binarySearch([1,2,3,5,6,7], 2) == 1
assert binarySearch([1,2,3,5,6,7], 3) == 2
assert binarySearch([1,2,3,5,6,7], 5) == 3
assert binarySearch([1,2,3,5,6,7], 6) == 4
assert binarySearch([1,2,3,5,6,7], 7) == 5
assert binarySearch([1,2,3,5,6,7], 1) == 0

assert binarySearch([1,2,3,5,6,7,8], 5) == 3
assert binarySearch([1,2,3,5,6,7,8], 6) == 4
assert binarySearch([1,2,3,5,6,7,8], 8) == 6
assert binarySearch([1,2,3,5,6,7,8], 2) == 1
assert binarySearch([1,2,3,5,6,7,8], 1) == 0
assert binarySearch([1,2,3,5,6,7,8], 11) == None
assert binarySearch([1,2,3,5,6,7,8], -1) == None

assert binarySearch(states, 'Alabama') == 0
assert binarySearch(states, 'foo') == None
assert binarySearch(states, 'Arizona') == 3

print('binary search ok!')