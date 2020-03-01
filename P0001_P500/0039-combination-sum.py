"""
https://leetcode.com/problems/combination-sum/

Given a set of candidate numbers (candidates) (without duplicates) and a target number (target), 
find all unique combinations in candidates where the candidate numbers sums to target.

The same repeated number may be chosen from candidates unlimited number of times.

Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: candidates = [2,3,6,7], target = 7,
A solution set is:
[
  [7],
  [2,2,3]
]
Example 2:

Input: candidates = [2,3,5], target = 8,
A solution set is:
[
  [2,2,2,2],
  [2,3,3],
  [3,5]
]

思路： 递归的循环数组里的每个数，并从 target 里面减掉，加到 out 里面，当 target==0 时， 将 out 加入 res
"""


class Solution:
    def combinationSum(self, candidates, target):
        res = []
        self.func(candidates, target, [], res, 0)
        # print(res)
        return res

    def func(self, candidates, target, out, res, start):
        if target < 0:
            return
        if target == 0:
            res.append(out)
            return

        for i in range(start, len(candidates)):
            self.func(candidates, target -
                      candidates[i], out + [candidates[i]], res, i)


S = Solution()
candidates = [2, 3, 5]
target = 8
res = S.combinationSum(candidates, target)
print(res)
