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
        return {''}

    charToMove = chars[0]
    rest = chars[1:]
    permutationsWithoutFirst = generatePermutation(rest)
    out = set()
    for perm in permutationsWithoutFirst:
        for i in range(len(perm)+1):
            out.add(perm[:i] + charToMove + perm[i:])
    return out

def test(chars: str, expected: Set[str]):
    result = generatePermutation(chars)
    assert result == expected, f'for "{chars}" -> {result} != {expected}'

test('',{''})
test('a',{'a'})
test('ab', {'ab', 'ba'})
print(generatePermutation('abcdef'))
print('ok')
