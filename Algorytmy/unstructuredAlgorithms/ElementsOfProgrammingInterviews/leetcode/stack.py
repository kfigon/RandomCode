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
        stak = [] # to keep track of current index, j to move into future
        for j in range(len(prices)):
            while len(stak) != 0 and prices[stak[-1]] >= prices[j]:
                i = stak.pop()
                prices[i] = prices[i] - prices[j]
            stak.append(j)

        return prices

    return stack(prices)

# https://leetcode.com/problems/next-greater-element-i/
def nextGreaterElement(nums1: List[int], nums2: List[int]) -> List[int]:
    def brute(nums1,nums2):
        idx = {}
        for i,v in enumerate(nums2):
            idx[v] = i
        
        def next_el(i):
            nonlocal idx, nums2
            starting_idx = idx.get(i, 0)
            for j in range(starting_idx+1, len(nums2)):
                if nums2[j] > i:
                    return nums2[j]
            return -1

        out = []
        for i in nums1:
            out.append(next_el(i))
        return out

    def foo(nums1, nums2):
        stak = []
        mapping = {} # map val to next larger
        for i in nums2:
            while len(stak) != 0 and i > stak[-1]: # if next is greater than previously processed
                mapping[stak.pop()] = i
            stak.append(i)

        out = []
        for i in nums1:
            out.append(mapping.get(i,-1))
        return out
    
    return foo(nums1, nums2)

# https://leetcode.com/problems/baseball-game
def calPoints(operations: List[str]) -> int:
    stak = []
    for op in operations:
        if op == '+':
            stak.append(stak[-1] + stak[-2])
        elif op == 'D':
            stak.append(stak[-1] * 2)
        elif op == 'C':
            stak.pop()
        else:
            stak.append(int(op))

    return sum(stak)