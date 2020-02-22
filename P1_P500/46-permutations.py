"""
https://leetcode.com/problems/permutations/

Given a collection of distinct integers, return all possible permutations.

Example:

Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]


递归： 想象一下手写全排列的步骤，每次拿出一个来作为第一个

"""


class Solution:
    def permute(self, nums):
        res = []
        self.func(nums, [], res)
        return res

    def func(self, nums, arr, res):
        if not nums:
            res.append(arr)
            return
        for i in range(len(nums)):
            self.func(nums[:i] + nums[i + 1:], arr + [nums[i]], res)


S = Solution()
nums = [1, 2, 3]
res = S.permute(nums)
print(res)
