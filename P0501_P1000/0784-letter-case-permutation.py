"""
https://leetcode.com/problems/letter-case-permutation/
Given a string S, we can transform every letter individually to be lowercase or 
uppercase to create another string.  Return a list of all possible strings we could create.

Examples:
Input: S = "a1b2"
Output: ["a1b2", "a1B2", "A1b2", "A1B2"]

Input: S = "3z4"
Output: ["3z4", "3Z4"]

Input: S = "12345"
Output: ["12345"]
"""


class Solution:
    def letterCasePermutation(self, s):
        res = [s]
        for i in range(len(s)):
            if s[i].isalpha():
                tmp = [word[:i] + word[i].swapcase() + word[i + 1:]
                       for word in res]
                res = res + tmp
        return res


S = Solution()
s = "a1b2"
res = S.letterCasePermutation(s)
print(res)
