# looking for substring
# count number of times smaller string appears in longer string

# Knuth-Morris-Pratt pattern search
# O(n)
def stringSearch(longer: str, substring: str) -> int:
    return 0

assert stringSearch('harold said haha in hamburg', 'ha') == 4
assert stringSearch('hharold said haha in hamburgh', 'ha') == 4
assert stringSearch('wowomgzomg', 'omg') == 2
assert stringSearch('wowomgzomg', 'wow') == 1
assert stringSearch('wowomgzomg', 'asd') == 0
assert stringSearch('wowomgzomgom', 'omg') == 2
assert stringSearch('aaaabaaa', 'aa') == 5
assert stringSearch('AABAACAADAABAABA', 'AABA') == 3
print('knp search ok')