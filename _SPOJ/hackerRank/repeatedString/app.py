# https://www.hackerrank.com/challenges/repeated-string/problem

from typing import Set

# find 'a'
def repeatedStr(pattern: str, limit: int) -> int:
    ids: Set[int] = set()
    for i,c in enumerate(pattern):
        if c == 'a':
            ids.add(i)

    totalPatternsInLimit = limit//len(pattern)
    remainderIdx = (limit % len(pattern)) -1
    howManyIdxsCought = 0
    for i in ids:
        if i <= remainderIdx:
            howManyIdxsCought += 1
    result = totalPatternsInLimit*len(ids) + howManyIdxsCought
    print(f'{pattern} * {limit} -> {result}')
    return result

assert repeatedStr('abcac', 1) == 1
assert repeatedStr('abcac', 2) == 1
assert repeatedStr('abcac', 3) == 1
assert repeatedStr('abcac', 4) == 2
assert repeatedStr('abcac', 5) == 2
assert repeatedStr('abcac', 6) == 3
assert repeatedStr('abcac', 10) == 4
assert repeatedStr('aba', 10) == 7
assert repeatedStr('a', 1000000000000) == 1000000000000

print('oks')