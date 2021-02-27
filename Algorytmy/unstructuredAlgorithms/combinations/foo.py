# generate all possible combinations
# order does not matter

# a,b,c: (2^n) - can be built with a tree
# [], [a], [b], [c], [a,b], [b,c], [a,c],[a,b,c]

#                      []
#a         []                      [a]
#b   []         [b]          [a]        [a,b]
#c  [] [c]    [b]  [bc]    [a] [ac]   [ab]   [abc

from typing import List

def generateCombination(chars: str) -> List[str]:
    return []

result = generateCombination('abc')
assert len(result) == 8
expectedCombinations = ['','a','b','c','ab','ac','bc','abc']
for i in expectedCombinations:
    assert i in result, i