from typing import Dict
# find longest substring with distinct chars

# O(n)
def findLongestSubstring(input: str) -> int:
    chars : Dict[str, int] = {}
    length = 0
    start = 0
    for i in range(len(input)):
        char = input[i]
        if char in chars:
            start = max(start, chars[char])

        length = max(length, i-start +1)
        chars[char] = i+1
    return length

assert findLongestSubstring('') == 0
assert findLongestSubstring('rithmschool') == 7
assert findLongestSubstring('thisisawesome') == 6
assert findLongestSubstring('thecatinthehat') == 7
assert findLongestSubstring('bbbbbb') == 1
assert findLongestSubstring('longestsubstring') == 8
assert findLongestSubstring('thisishowwedoit') == 6

# todo: not done by myself ;(