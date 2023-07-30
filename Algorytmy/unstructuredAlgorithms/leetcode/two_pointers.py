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

# https://leetcode.com/problems/container-with-most-water/
def maxArea(height: List[int]) -> int:
    maxArea = 0
    left,right = 0, len(height)-1
    while left < right:
        h = min(height[left], height[right])
        width = right - left
        maxArea = max(maxArea,h*width)
        if height[left] > height[right]:
            right-=1
        else:
            left+=1
    return maxArea

# https://leetcode.com/problems/trapping-rain-water/
def trap(height: List[int]) -> int:
    water = 0
    left = 0
    right = len(height)-1

    maxL = height[left]
    maxR = height[right]
    while left < right:
        if height[left] <= height[right]:
            left +=1
            maxL = max(maxL, height[left])
            water += maxL - height[left]
        else:
            right -=1
            maxR = max(maxR, height[right])
            water += maxR - height[right]
    return water

# https://leetcode.com/problems/first-bad-version
def firstBadVersion(n: int) -> int:
# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:
    isBadVersion = lambda x: True
    
    left = 0
    right = n
    mid = None
    while left <= right:
        mid = (right-left)//2 + left
        if isBadVersion(mid):
            right = mid-1
        else:
            left = mid + 1

    return left

# https://leetcode.com/problems/maximum-subarray
def maxSubArray(nums: List[int]) -> int:
    runningSum = nums[0]
    maxS = runningSum
    
    for i in range(1, len(nums)):
        v = nums[i]
        if runningSum < 0:
            runningSum = 0
        runningSum += v
        maxS = max(maxS, runningSum)
    return maxS