from typing import List

# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
def maxProfit(prices: List[int]) -> int:
    # in fact it's a two pointers solution
    profit = 0
    buyPrice = prices[0]
    for sellPrice in prices:
        if buyPrice > sellPrice:
            buyPrice = sellPrice
        
        profit = max(profit, sellPrice-buyPrice)


    return profit

# https://leetcode.com/problems/longest-substring-without-repeating-characters/
def lengthOfLongestSubstring(s: str) -> int:
    startIdx = 0
    runningSet = set()
    maxLen = 0
    for c in s:
        while c in runningSet:
            runningSet.remove(s[startIdx])
            startIdx += 1
        runningSet.add(c)
        maxLen = max(maxLen, len(runningSet))
    return maxLen

# https://leetcode.com/problems/longest-repeating-character-replacement/submissions/949849942/
def characterReplacement(s: str, k: int) -> int:
    startIdx = 0
    maxLen = 0
    freq = {}
    currentLen = lambda i: i - startIdx +1

    for i,c in enumerate(s):
        freq[c] = freq.get(c,0)+1
        while (currentLen(i) - max(freq.values())) > k: # still o(n) -> o(26*n)
            freq[s[startIdx]] -= 1
            startIdx += 1      
        maxLen = max(maxLen, currentLen(i))
            
    return maxLen