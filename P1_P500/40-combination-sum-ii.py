"""
https://leetcode.com/problems/combination-sum-ii/

Given a collection of candidate numbers (candidates) and a target number (target), 
find all unique combinations in candidates where the candidate numbers sums to target.

Each number in candidates may only be used once in the combination.

Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: candidates = [10,1,2,7,6,1,5], target = 8,
A solution set is:
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]
Example 2:

Input: candidates = [2,5,2,1,2], target = 5,
A solution set is:
[
  [1,2,2],
  [5]
]

思路：参考39题， 只是需要去重

"""


class Solution:
    def combinationSum2(self, candidates, target):
        res = []
        self.func(candidates, target, [], 0, res)
        return res

    def func(self, candidates, target, out, start, res):
        if target < 0:
            return
        if target == 0:
            out.sort()
            if out not in res:
                res.append(out)
            return

        for i in range(start, len(candidates)):
            self.func(candidates, target -
                      candidates[i], out + [candidates[i]], i + 1, res)


S = Solution()
candidates = [10, 1, 2, 7, 6, 1, 5]
target = 8
res = S.combinationSum2(candidates, target)
print(res)
