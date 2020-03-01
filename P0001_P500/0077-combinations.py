"""
https://leetcode.com/problems/combinations/

Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

Example:

Input: n = 4, k = 2
Output:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]

参考39题

"""


class Solution:
    def combine(self, n: int, k: int):
        res = []
        self.func(n, k, [], res, 1)
        return res

    def func(self, n, k, out, res, start):
        if len(out) == k:
            res.append(out)

        for i in range(start, n + 1):
            self.func(n, k, out + [i], res, i + 1)


S = Solution()
n = 4
k = 2
res = S.combine(n, k)
print(res)
