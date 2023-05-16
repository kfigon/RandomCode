from typing import List

# https://leetcode.com/problems/valid-parentheses
def isValid(s: str) -> bool:
    bracers = {
        '(': ')',
        '[': ']',
        '{': '}',
    }
    stack = []
    for c in s:
        if c in bracers: # opening
            stack.append(c)
        elif len(stack) == 0 or c != bracers[stack.pop()]: # closing matched
            return False
            
    return len(stack) == 0