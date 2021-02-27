# generate all possible arrangements
# order does matter

# a,b,c: (n!) - can be built with a tree
# [abc, acb, bac, bca, cab, cba]

#                []
#a              [a]
#b        [ba]      [ab]
#c    cba cba bac    cab acb abc


from typing import Set

def generatePermutation(chars: str) -> Set[str]:
    if len(chars) == 0:
        return set()
    return set()

def test(chars: str, expected: Set[str]):
    result = generatePermutation(chars)
    assert result == expected, f'{result} != {expected}'

test('',{''})
test('a',{'a'})
test('ab', {'ab', 'ba'})
test('abc', {'abc','acb','cab', 'bac','bca','cba'})
print('ok')