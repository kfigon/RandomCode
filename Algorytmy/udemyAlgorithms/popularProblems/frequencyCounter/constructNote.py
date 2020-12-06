from typing import Dict

# write a fun that accepts 2 strings - message and some letters
# fun should return true if the message can be built with the letters 
# that you are given

# assume lowercase, not special chars and no spaces

# space - O(N)
# time - O(N+M)

def buildDict(letters: str) -> Dict[str, int]:
    d: Dict[str, int] = {}
    for c in letters:
        if c in d:
            d[c] += 1
        else:
            d[c] = 1
    return d

def constructNote(message: str, letters: str) -> bool:
    d = buildDict(letters)
    for c in message:
        if c not in d or d[c] <= 0:
            return False
        d[c] -= 1

    return True

assert constructNote('aa', 'abc') == False
assert constructNote('abc', 'dcba') == True
assert constructNote('aabbcc', 'bcabcaddff') == True
assert constructNote('kamil', 'kamil') == True
assert constructNote('kaamil', 'kamil') == False

print('ok')