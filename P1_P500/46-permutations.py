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

参考 31.next-permutation
递归的想法是：nums的全排列相当于：

nums[0] + permute(nums \ nums[0])  # 表示除了0以外的数的全排列

nums[1] + permute(nums \ nums[1])

….

nums[n-1] + permute(nums \ nums[n-1])

"""


class Solution:
    def permute(self, nums):
        res = []
        self.func(0, nums, res)
        return res

    def func(self, cur, nums, res):
        if cur == len(nums) - 1:
            res.append(nums)
            return

        for i in range(cur, len(nums)):
            #print(nums[cur], nums[i])
            nums[cur], nums[i] = nums[i], nums[cur]
            #print(nums[cur], nums[i])
            self.func(cur + 1, nums, res)
            nums[cur], nums[i] = nums[i], nums[cur]


S = Solution()
nums = [1, 2, 3]
res = S.permute(nums)
print(res)
