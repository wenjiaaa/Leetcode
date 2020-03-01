"""
https://leetcode.com/problems/combination-sum-iii/

Find all possible combinations of k numbers that add up to a number n, 
given that only numbers from 1 to 9 can be used and each combination should be a unique set of numbers.

Note:

All numbers will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: k = 3, n = 7
Output: [[1,2,4]]
Example 2:

Input: k = 3, n = 9
Output: [[1,2,6], [1,3,5], [2,3,4]]

"""


class Solution:
    def combinationSum3(self, k, n):
        res = []
        self.func(n, [], res, 1, k)
        return res

    def func(self, target, out, res, start, k):
        if target < 0:
            return
        if target == 0:
            if len(out) == k and out not in res:
                res.append(out)
            return

        for i in range(start, 10):
            self.func(target - i, out + [i], res, i + 1, k)


S = Solution()
k = 3
n = 9
res = S.combinationSum3(k, n)
print(res)
