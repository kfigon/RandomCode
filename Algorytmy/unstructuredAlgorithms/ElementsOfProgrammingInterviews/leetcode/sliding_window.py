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

# https://leetcode.com/problems/substrings-of-size-three-with-distinct-characters
def countGoodSubstrings(s: str) -> int:
    startIdx = 0
    occ = {}
    goodString = 0
    goodStringLimit = 3
    for i in range(len(s)):
        c = s[i]
        occ[c] = occ.get(c, 0) + 1
        
        if sum(occ.values()) != goodStringLimit:
            continue

        if len(occ) == goodStringLimit:
            goodString += 1
            
        occ[s[startIdx]] -=1
        if occ[s[startIdx]] == 0:
            occ.pop(s[startIdx])
        startIdx += 1
    
    return goodString

# https://leetcode.com/problems/number-of-sub-arrays-of-size-k-and-average-greater-than-or-equal-to-threshold/
def numOfSubarrays(arr: List[int], k: int, threshold: int) -> int:
    start = 0
    out = 0
    pendingSum =0
    for i,v in enumerate(arr):
        pendingSum += v

        if start+i+1 < k:
            continue # collect more
        
        if (pendingSum/k) >= threshold:
            out += 1

        pendingSum -= arr[start]
        start+=1
            
    return out

# https://leetcode.com/problems/max-consecutive-ones-iii/
def longestOnes(nums: List[int], k: int) -> int:
    occ = {}
    start = 0
    longest = 0
    for i,v in enumerate(nums):
        occ[v] = occ.get(v,0)+1
        
        if occ.get(0,0) <= k:
            longest = max(longest, i-start+1)
        else:
            while occ.get(0,0) > k:
                occ[nums[start]]-=1
                start+=1

    return longest

# https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length
def maxVowels(s: str, k: int) -> int:
    vowels = set(['a','e','i','o','u'])
    currentVowels = 0
    start = 0
    count = 0
    for i,c in enumerate(s):
        if c in vowels:
            currentVowels += 1

        if i-start+1 != k:
            continue # collect more
        
        count = max(currentVowels, count)
        if s[start] in vowels:
            currentVowels -=1
        start += 1
        
    return count