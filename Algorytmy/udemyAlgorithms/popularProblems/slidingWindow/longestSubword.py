from typing import List

# O(n^2)
def longestSequenceOfUniqueCharsBrute(input: str) -> str:
    out = []
    word = input[0]
    for i in range(1,len(input)):
        if input[i] in word:
            out.append(word)
            word = input[i]
        else:
            word += input[i]

    if word != '':
        out.append(word)

    print(out)
    sort = sorted(out, key=lambda x: len(x))
    return sort[-1]

def longestSequenceOfUniqueChars(input: str) -> str:
    return ''


assert longestSequenceOfUniqueCharsBrute('hellothere') == 'lother'
assert longestSequenceOfUniqueCharsBrute('abcdef') == 'abcdef'
assert longestSequenceOfUniqueCharsBrute('aabcdef') == 'abcdef'
assert longestSequenceOfUniqueCharsBrute('fabcdef') == 'fabcde'

assert longestSequenceOfUniqueChars('hellothere') == 'lother'
assert longestSequenceOfUniqueChars('abcdef') == 'abcdef'
assert longestSequenceOfUniqueChars('aabcdef') == 'abcdef'
assert longestSequenceOfUniqueChars('fabcdef') == 'fabcde'