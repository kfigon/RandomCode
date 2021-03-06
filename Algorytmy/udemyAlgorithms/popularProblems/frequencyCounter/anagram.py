from typing import Dict

# given 2 strings - determine is the second string an anagram of 1st
# anagram - rearrange

# brute force - zagniezdzone petle + frequencyCounter pattern
# lepsze - mapa wystapien

def countFreq(a: str) -> Dict[str, int]:
    out : Dict[str, int] = {}
    for i in a:
        out[i] = 1 if i not in out else out[i] + 1
    return out

# O(2n) -> O(n)
def isAnagram(a: str, b: str) -> bool:
    if len(a) != len(b):
        return False

    freqA = countFreq(a)
    for i in b:
        if i not in freqA or freqA[i] < 1:
            return False
        else:
            freqA[i] -= 1
    return True


assert isAnagram('', '') == True
assert isAnagram('aaz', 'zza') == False
assert isAnagram('anagram', 'nagaram') == True
assert isAnagram('cinema', 'iceman') == True
assert isAnagram('cat', 'cat') == True
assert isAnagram('rat', 'car') == False
assert isAnagram('awesome', 'awesom') == False
assert isAnagram('qwerty', 'qeywrt') == True
assert isAnagram('texttwisttime', 'timetwisttext') == True