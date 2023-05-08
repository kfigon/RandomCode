from typing import List

# https://leetcode.com/problems/valid-palindrome/
def isPalindrome(s: str) -> bool:
    validChar = lambda c: c.isalpha() or c.isdigit()
    i = 0
    backI = len(s)-1
    while i <= backI:
        c = s[i]
        cBack = s[backI]
        if not validChar(c):
            i+=1
            continue
        elif not validChar(cBack):
            backI -= 1
            continue
        elif c.lower() != cBack.lower():
            return False
        i += 1
        backI -=1
    return True

# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
def twoSum(numbers: List[int], target: int) -> List[int]:
    left,right = 0, len(numbers)-1
    while left < right:
        got = numbers[left] + numbers[right]
        if got == target:
            return [left+1, right+1]
        elif got > target:
            right-=1
        else:
            left+=1
    return []

# https://leetcode.com/problems/3sum
def threeSum(nums: List[int]) -> List[List[int]]:
    nums.sort()
    out = []
    for i in range(len(nums)):
        if i != 0 and nums[i-1] == nums[i]:
            continue

        l,r = i+1,len(nums)-1
        while l<r:
            aSum = nums[i] + nums[l]+ nums[r]
            if aSum > 0:
                r-=1
            elif aSum < 0:
                l+=1
            else:
                out.append([nums[i],nums[r],nums[l]])
                l+=1
                while nums[l] == nums[l-1] and l < r:
                    l+=1
            
    return out