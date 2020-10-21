# looking for substring
# count number of times smaller string appears in longer string

# O(n^2)
def stringSearch(longer: str, substring: str) -> int:
    count = 0
    for i in range(len(longer)):
        for j in range(len(substring)):
            if (i+j) >= len(longer) or longer[i+j] != substring[j]:
                break

            if j == len(substring)-1:
                count += 1
    return count

assert stringSearch('harold said haha in hamburg', 'ha') == 4
assert stringSearch('hharold said haha in hamburgh', 'ha') == 4
assert stringSearch('wowomgzomg', 'omg') == 2
assert stringSearch('wowomgzomg', 'wow') == 1
assert stringSearch('wowomgzomg', 'asd') == 0
assert stringSearch('wowomgzomgom', 'omg') == 2
assert stringSearch('aaaabaaa', 'aa') == 5
print('naive ok')