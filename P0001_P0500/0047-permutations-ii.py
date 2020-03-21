"""
https://leetcode.com/problems/permutations-ii/

Given a collection of numbers that might contain duplicates, return all possible unique permutations.

Example:

Input: [1,1,2]
Output:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]

参考 46.permutations
如何去重，先排序把重复的数字都挨在一起，然后加入的时候遇到重复的跳过。 注意排序是必须的。
"""


res = 0


class Solution:
    def permuteUnique(self, nums):
        self.res = res
        nums.sort()
        self.func(nums, [])
        return self.res

    def func(self, nums, arr):
        if not nums:
            self.res += 1
        for i in range(len(nums)):
            if nums[i] == nums[i - 1] and i > 0:
                continue
            self.func(nums[:i] + nums[i + 1:], arr + [nums[i]])


S = Solution()
nums = [3, 0, 3]
res = S.permuteUnique(nums)
print(res)
