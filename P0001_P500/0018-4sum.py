"""
https://leetcode.com/problems/4sum/

Given an array nums of n integers and an integer target, are there elements a, b, c, and d in nums 
such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

Note:

The solution set must not contain duplicate quadruplets.

Example:

Given array nums = [1, 0, -1, 0, -2, 2], and target = 0.

A solution set is:
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]

"""


# 双指针 O(n^3)
class Solution:
    def fourSum(self, nums, target):
        nums.sort()
        res = []
        for i in range(len(nums) - 3):
            a = nums[i]
            if nums[i] == nums[i-1] and i > 0:
                continue
            for j in range(i + 1, len(nums) - 2):
                b = nums[j]
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                tmp = self.twoSum(a, b, nums[j + 1:], target)
                res.extend(tmp)
        return res

    def twoSum(self, a, b, nums, target):
        res = []
        i = 0
        j = len(nums) - 1
        while (i < j):
            if a + b + nums[i] + nums[j] == target:
                if [a, b, nums[i], nums[j]] not in res:
                    res.append([a, b, nums[i], nums[j]])
                i += 1
                j -= 1
            elif a + b + nums[i] + nums[j] < target:
                i += 1
            else:
                j -= 1
        return res


S = Solution()
nums = [1, 0, -1, 0, -2, 2]
target = 0
res = S.fourSum(nums, target)
print(res)
