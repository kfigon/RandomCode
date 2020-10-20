from typing import List, TypeVar, Optional
from random import randint

T=TypeVar('T')

states: List[str] = ['Alabama', 'Alaska', 'American Samoa', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware', 'District Of Columbia', 'Federated States Of Micronesia', 'Florida', 'Georgia', 'Guam', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Marshall Islands', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey', 'New Mexico', 'New York', 'North Carolina', 'North Dakota', 'Northern Mariana Islands', 'Ohio', 'Oklahoma', 'Oregon', 'Palau', 'Pennsylvania', 'Puerto Rico', 'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virgin Islands', 'Virginia', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming']

def shuffle(tab: List[str]) -> List[str]:
    out: List[str] = [i for i in tab]
    for i in range(len(tab)):
        toChange = randint(i, len(tab)-1)
        out[i],out[toChange] = out[toChange], out[i]
    return out

# simpliest way, O(n) - go element by element 
# and check if it's the element
def linearSearch(tab: List[T], searching: T) -> Optional[int]:
    for i,v in enumerate(tab):
        if v == searching:
            return i
    return None

assert linearSearch(states, 'Alabama') == 0
assert linearSearch(states, 'foo') == None
assert linearSearch(states, 'Arizona') == 3
assert linearSearch([3,5,6,3,2,5], 4) == None
assert linearSearch([3,5,6,3,2,5], 6) == 2

print('linear search ok!')