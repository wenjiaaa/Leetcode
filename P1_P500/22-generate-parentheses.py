"""
https://leetcode.com/problems/generate-parentheses/

Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
"""


class Solution:
    def generateParenthesis(self, n: int):
        res = []
        self.func(res, "", n, 0, 0)
        return res

    def func(self, res, out, n, left, right):
        if len(out) == 2 * n:
            res.append(out)
            return
        if left < n:
            self.func(res, out + "(", n, left + 1, right)
        if right < left:
            self.func(res, out + ")", n, left, right+1)


S = Solution()
n = 3
res = S.generateParenthesis(n)
print(res)
