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


# https://leetcode.com/problems/maximum-nesting-depth-of-the-parentheses
def maxDepth(s: str) -> int:
    stak = [] # technically this could be just an integer, we don't care about the values
    max_d = 0
    for c in s:
        if c == '(':
            stak.append('(')
            max_d = max(max_d, len(stak))
        elif c == ')':
            stak.pop()
        
    return max_d

# https://leetcode.com/problems/remove-outermost-parentheses
def removeOuterParentheses(s: str) -> str:
    stak = 0
    part_idx = []
    for (i,c) in enumerate(s):           
        if c == '(':
            if stak == 0:
                part_idx.append(i)
            stak += 1
        elif c == ')':
            stak -= 1
            if stak == 0:
                part_idx.append(i)

    out = ""
    for i in range(len(part_idx)-1):
        out += s[part_idx[i]+1:part_idx[i+1]]
    return out

# https://leetcode.com/problems/final-prices-with-a-special-discount-in-a-shop
def finalPrices(prices: List[int]) -> List[int]:
    def brute(prices: List[int]) -> List[int]:
        out = []
        for i in range(len(prices)):
            j = i+1
            found = False
            while j < len(prices):
                if prices[j] <= prices[i]:
                    found = True
                    out.append(prices[i] - prices[j])
                    break
                j+=1
            if not found:
                out.append(prices[i])

        return out
    
    def stack(prices: List[int]) -> List[int]:
        stak = []
        for j in range(len(prices)):
            while len(stak) != 0 and prices[stak[-1]] >= prices[j]:
                i = stak.pop()
                prices[i] = prices[i] - prices[j]
            stak.append(j)

        return prices

    return stack(prices)
