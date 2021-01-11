from typing import List, Set

# https://adventofcode.com/2015/day/5

def isNiceString(line: str) -> bool:
    assert line is not None
    assert len(line) != 0

    bannedSubstrings = ['ab','cd','pq','xy']
    for banned in bannedSubstrings:
        if banned in line:
            return False

    numberOfVowels = 0
    hasDoubledCharacter = False
    allowedVowels: Set[str] = {'a', 'e', 'i', 'o', 'u'}

    for idx in range(len(line)):
        c = line[idx]
        if c in allowedVowels:
            numberOfVowels += 1
        if idx+1 < len(line) and c == line[idx+1]:
            hasDoubledCharacter = True

    # print(f'{line} -> {numberOfVowels}, {hasDoubledCharacter}')
    return numberOfVowels >= 3 and hasDoubledCharacter


niceWords = [
    'ugknbfddgicrmopn', 'aaa'
]
naughtyWords = [
    'ab', 'cd', 'pq', 'xy',
    'jchzalrnumimnmhp', 'haegwjzuvuyypxyu', 'dvszwmarrgswjxmb'
]

for i in niceWords:
    assert isNiceString(i), f'{i} should be true'

for i in naughtyWords:
    assert not isNiceString(i), f'{i} should be false'

with open('input.txt') as f:
    lines: List[str] = f.readlines()
    numberOfNice = 0
    for l in lines:
        if isNiceString(l):
            numberOfNice+=1
    print(f'nice {numberOfNice}')