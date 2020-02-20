"""
https://leetcode.com/problems/two-sum/
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""


# 双指针, O(n)
class Solution1:
    def twoSum(self, nums, target):
        L = []
        for idx, v in enumerate(nums):
            L.append((v, idx))
        L = sorted(L, key=lambda x: x[0])
        i = 0
        j = len(L) - 1
        while i <= len(L) - 1 and j >= 0:
            if L[i][0] + L[j][0] == target:
                break
            elif L[i][0] + L[j][0] < target:
                i += 1
            else:
                j -= 1
        return [L[i][1], L[j][1]]


# 采用 hash, O(n)
class Solution:
    def twoSum(self, nums, target):
        L = {}
        for idx, v in enumerate(nums):
            L[v] = idx
        for i in range(len(nums)):
            n = nums[i]
            m = target - n
            if m in L and L[m] != i:
                return [i, L[m]]


S = Solution()
nums = [3, 3]
target = 6
print(S.twoSum(nums, target))
