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

def isNiceString2(line: str) -> bool:
    assert line is not None
    assert len(line) != 0

    return False
# todo: https://adventofcode.com/2015/day/5#part2

# nice words
for i in ['ugknbfddgicrmopn', 'aaa']:
    assert isNiceString(i), f'{i} should be true'

# naughty words
for i in ['ab', 'cd', 'pq', 'xy', 'jchzalrnumimnmhp', 'haegwjzuvuyypxyu', 'dvszwmarrgswjxmb']:
    assert not isNiceString(i), f'{i} should be false'

for i in ['qjhvhtzxzqqjkmpb', 'xxyxx']:
    assert isNiceString2(i), f'{i} should be true'

for i in ['uurcxstgmygtbstg', 'ieodomkazucvgmuy']:
    assert not isNiceString2(i), f'{i} should be false'

with open('input.txt') as f:
    lines: List[str] = f.readlines()
    numberOfNiceOld = 0
    numberOfNiceNew = 0
    for l in lines:
        if isNiceString(l):
            numberOfNiceOld+=1
        if isNiceString2(l):
            numberOfNiceNew += 1

    print(f'nice {numberOfNiceOld}, niceNew: {numberOfNiceNew}')