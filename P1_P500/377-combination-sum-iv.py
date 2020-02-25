"""
https://leetcode.com/problems/combination-sum-iv/
Given an integer array with all positive numbers and no duplicates, 
find the number of possible combinations that add up to a positive integer target.

Example:

nums = [1, 2, 3]
target = 4

The possible combination ways are:
(1, 1, 1, 1)
(1, 1, 2)
(1, 2, 1)
(1, 3)
(2, 1, 1)
(2, 2)
(3, 1)

Note that different sequences are counted as different combinations.

Therefore the output is 7

参考 39, 40, 216， 递归超时了， 用动态规划
"""


# 递归， 超时
class Solution1:
    def combinationSum4(self, nums, target):
        self.res = 0
        self.func(nums, target)
        return self.res

    def func(self, nums, target):
        if target < 0:
            return
        if target == 0:
            self.res += 1
            return
        for i in range(len(nums)):
            self.func(nums, target - nums[i])


class Solution:
    def combinationSum4(self, nums, target):
        res = [0] * (target + 1)
        for i in range(1, target + 1):
            for j in range(len(nums)):
                if (i - nums[j]) == 0:  # 说明当前还可以把nums[i]加进去，方案数增加1
                    res[i] += 1
                elif (i - nums[j]) > 0:  # 说明可以在target=(i-nums[j])的方案上通过添加nums[j]令和为target
                    res[i] = res[i] + res[i - nums[j]]
        return res[target]


S = Solution()
nums = [1, 2, 3]
target = 4
res = S.combinationSum4(nums, target)
print(res)
