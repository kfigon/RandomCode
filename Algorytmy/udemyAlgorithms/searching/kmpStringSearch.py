from typing import List

# looking for substring
# count number of times smaller string appears in longer string
# https://www.baeldung.com/cs/knuth-morris-pratt
# https://en.wikipedia.org/wiki/Knuth%E2%80%93Morris%E2%80%93Pratt_algorithm
# Knuth-Morris-Pratt pattern search
# O(n+m)
# https://www.youtube.com/watch?v=GTJr8OvyEVQ

# same as naive, but first calculate a helper array, so in case of mismatch we don't
# have to start from beginning. Based on helper array we can move few indexes at the same time, so we end up in linear complexity

def calculateLps(pattern: str) -> List[int]:
    return out

def stringSearch(longer: str, substring: str) -> int:
    return 0

assert calculateLps('') == [-1]
assert calculateLps('ABCDABD') == [-1, 0, 0,0,-1,0,2,0]
assert calculateLps('ABACABABC') == [-1,0,-1,1,-1,0,-1,3,2,0]
assert calculateLps('ABACABABA') == [-1,0,-1,1,-1,0,-1,3,-1,3]
assert calculateLps('PARTICIPATE IN PARACHUTE') == [-1,0,0,0,0,0,0,-1,0,2,0,0,0,0,0,-1,0,0,3,0,0,0,0,0,0]
assert calculateLps('aabaaba') == [-1, 0, 1, 0, 1, 2,3,4]

assert stringSearch("ABC ABCDAB ABCDABCDABDE", "ABCDABD") == 1
assert stringSearch('harold said haha in hamburg', 'ha') == 4
assert stringSearch('hharold said haha in hamburgh', 'ha') == 4
assert stringSearch('wowomgzomg', 'omg') == 2
assert stringSearch('wowomgzomg', 'wow') == 1
assert stringSearch('wowomgzomg', 'asd') == 0
assert stringSearch('wowomgzomgom', 'omg') == 2
assert stringSearch('aaaabaaa', 'aa') == 5
assert stringSearch('AABAACAADAABAABA', 'AABA') == 3
print('knp search ok')