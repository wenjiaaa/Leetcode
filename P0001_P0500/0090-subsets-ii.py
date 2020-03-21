"""
https://leetcode.com/problems/subsets-ii/

Given a collection of integers that might contain duplicates, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: [1,2,2]
Output:
[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]
"""


class Solution:
    def subsetsWithDup(self, nums):
        nums.sort()
        res = [[]]
        for i in range(len(nums)):
            new_subset = []
            for tmp in res:
                tmp_new = tmp + [nums[i]]
                if tmp_new not in res:
                    new_subset.append(tmp_new)
            res = res + new_subset
        return res


S = Solution()
nums = [4, 4, 4, 1, 4]
res = S.subsetsWithDup(nums)
print(res)
