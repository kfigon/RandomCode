# generate all possible combinations
# order does not matter

# a,b,c: (2^n) - can be built with a tree
# [], [a], [b], [c], [a,b], [b,c], [a,c],[a,b,c]

#                      []
#a         []                      [a]
#b   []         [b]          [a]        [a,b]
#c  [] [c]    [b]  [bc]    [a] [ac]   [ab]   [abc

from typing import List

# O(2^n)
# space: O(n^2)
def generateCombination(chars: str) -> List[str]:
    if len(chars) == 0:
        return []

    firstEl = chars[0]
    rest = chars[1:]

    combinationForFirst: List[str] = []
    combinationsForRest =  generateCombination(rest)

    for i in combinationsForRest:
        combinationForFirst += [i + firstEl]

    return combinationsForRest + combinationForFirst

def test(chars: str, expected: List[str]):
    result = generateCombination(chars)
    assert len(result) == len(expected), f'for {chars} got {len(result)}, exp {len(expected)}'
    for i in expected:
        assert i in result, f'{chars} error, {i}'

test('',[''])
test('a',['','a'])
test('abc',['','a','b','c','ab','ac','bc','abc'])