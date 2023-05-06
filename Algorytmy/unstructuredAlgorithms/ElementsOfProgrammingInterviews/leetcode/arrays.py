from typing import List

# https://leetcode.com/problems/contains-duplicate/
# time o(n), space o(n)
def containsDuplicate(nums: List[int]) -> bool:
    s = set(nums)
    return len(s) != len(nums)

# time o(nlogn), space o(1)
def containsDuplicate2(nums: List[int]) -> bool:
    nums.sort()
    for i in range(len(nums)-1):
        if nums[i] == nums[i+1]:
            return True
    return False

# https://leetcode.com/problems/valid-anagram/
def isAnagram(self, s: str, t: str) -> bool:
    if len(s) != len(t):
        return False    
    # forget about clean code, this is leetcode. Put everything in a single loop
    oc1 = {}
    oc2 = {}
    for i in range(len(s)):
        oc1[s[i]] = oc1.get(s[i], 0) + 1
        oc2[t[i]] = oc2.get(t[i], 0) + 1
    
    for c in oc1:
        if c not in oc2 or oc1[c] != oc2[c]:
            return False
    return True

# https://leetcode.com/problems/two-sum/
def twoSum(nums: List[int], target: int) -> List[int]:
    foo = {}
    # not needed, we can put it in the loop
    # for i,v in enumerate(nums):
    #     foo[v] = i

    for idx,v in enumerate(nums):
        toFind = target - v
        if toFind in foo and foo[toFind] != idx:
            return [idx, foo[toFind]]
        foo[v] = idx
    return []

# https://leetcode.com/problems/group-anagrams/
def groupAnagrams(strs: List[str]) -> List[List[str]]:
    def occurences(s):
        oc = {}
        for i in s:
            oc[i] = oc.get(i, 0) + 1
        return oc
    
    anagramHashes = {}
    for s in strs:
        # i should use array of occurences and then have it as a key, but this is the idea
        occs = occurences(s)
        h = hash(frozenset(occs.items()))
        v = anagramHashes.get(h, [])
        v.append(s)
        anagramHashes[h] = v
    
    return anagramHashes.values()