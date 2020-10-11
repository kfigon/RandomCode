from typing import Dict, List
import random
import string
import time

def getRandom(length: int) -> str:
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))

# O(n)
def countCharsSimple(input: str) -> Dict[str, int]:
    out : Dict[str, int] = {}
    for i in input:
        out[i] = 1 if i not in out else out[i] + 1
    return out

# not so pro - sorting introduces more time
# O(n logn) ?
def countCharsPro(input: str) -> Dict[str, int]:
    sort : List[str] = sorted(input)
    out : Dict[str, int] = {}
    counter = 0
    i = 1
    prevChar=''

    while(i<len(sort)):
        prevChar = sort[i-1]
        char=sort[i]
        counter += 1
        if prevChar != char:
            out[prevChar] = counter
            counter = 0
        i+=1
            
    out[sort[-1]] = counter+1
    return out

assert countCharsSimple('missisipi') == countCharsPro('missisipi')
assert countCharsSimple('falanga') == countCharsPro('falanga')
assert countCharsSimple('johndoe') == countCharsPro('johndoe')
assert countCharsSimple('johndoee') == countCharsPro('johndoee')

print('generating')
words = [getRandom(1000) for i in range(10000)]
    
print('tests and timing')
results = {'simple':0, 'pro':0}
for i in words:
    start = time.time_ns()
    sResult = countCharsSimple(i)
    results['simple'] += time.time_ns()-start

    start2 = time.time_ns()
    pResult = countCharsPro(i)
    results['pro'] += time.time_ns()-start2
    assert sResult == pResult

print(f"simple version: {results['simple']/len(words)} ms")
print(f"pro version: {results['pro']/len(words)} ms")