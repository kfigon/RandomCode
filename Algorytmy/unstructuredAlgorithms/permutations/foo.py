# generate all possible arrangements
# order does matter

# a,b,c: (n!) - can be built with a tree
# [abc, acb, bac, bca, cab, cba]


from typing import List

def generatePermutation(chars: str) -> List[str]:
    if len(chars) == 0:
        return ['']
    return []

def test(chars: str, expected: List[str]):
    result = generatePermutation(chars)
    assert len(result) == len(expected), f'for {chars} got {len(result)}, exp {len(expected)}'
    for i in expected:
        assert i in result, f'error in {chars}, {i} not found in {result}'

test('',[''])
test('a',['','a'])
test('abc',['','a','b','c','ab','ac','bc','abc'])
print('ok')