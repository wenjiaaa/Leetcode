"""
https://leetcode.com/problems/subsets/

Given a set of distinct integers, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: nums = [1,2,3]
Output:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]

思路：每次往 res 里添加新的数，就是在原来集合里加上n
[[], [1]] + 2 = [[2], [1, 2]]
[1, 2] = [[], [1]] + [[2], [1, 2]]

"""


class Solution:
    def subsets(self, nums):
        nums.sort()
        res = [[], [nums[0]]]
        for n in nums[1:]:
            tmp = [item + [n] for item in res]
            res = res + tmp
        return res


S = Solution()
nums = [1, 2, 3]
res = S.subsets(nums)
print(res)
