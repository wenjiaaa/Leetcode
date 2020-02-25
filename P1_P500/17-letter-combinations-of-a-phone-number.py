"""
https://leetcode.com/problems/letter-combinations-of-a-phone-number/

Given a string containing digits from 2-9 inclusive, return all possible letter combinations 
that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below. 
Note that 1 does not map to any letters.


Example:

Input: "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].

思路： 递归的在每个按钮上选一个字母加入到结果中
"""


class Solution:
    def letterCombinations(self, digits: str):
        if digits == "":
            return []
        self.D = {
            '1': "",
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        res = []
        self.func(digits, 0, "", res)
        return res

    def func(self, digits, level, out, res):
        # print(out)
        if level == len(digits):
            res.append(out)
            return

        cand = self.D[digits[level]]
        for c in cand:
            out = out + c
            self.func(digits, level + 1, out, res)
            out = out[:-1]
            # print(out)
            #out = ""


S = Solution()
digits = "23"
res = S.letterCombinations(digits)
print(res)
