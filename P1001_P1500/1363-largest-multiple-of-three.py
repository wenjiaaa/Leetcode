"""
https://leetcode.com/problems/largest-multiple-of-three/

Given an integer array of digits, return the largest multiple of three that can be formed 
by concatenating some of the given digits in any order.

Since the answer may not fit in an integer data type, return the answer as a string.

If there is no answer return an empty string.

 

Example 1:

Input: digits = [8,1,9]
Output: "981"
Example 2:

Input: digits = [8,6,7,1,0]
Output: "8760"
Example 3:

Input: digits = [1]
Output: ""

思路：把列表的所有子集列出来，对每个子集比较找出最大数值，但是出现了：Memory Limit Exceeded
"""


class Solution:
    def largestMultipleOfThree(self, digits):
        if set(digits) == {0}:
            return "0"
        digits = sorted(digits, reverse=True)
        subsets = self.func(digits)
        # print(subsets)
        max_sum = 0
        res = ""
        for i in range(len(subsets) - 1, 0, -1):
            subset = subsets[i]
            if sum(subset) % 3 == 0 and sum(subset) > max_sum:
                res = "".join([str(i) for i in subset])
                max_sum = sum(subset)
        return res

    def func(self, nums):
        res = [[]]
        for i in range(len(nums)):
            tmp = [item + [nums[i]] for item in res]
            res = res + tmp
        return res


S = Solution()
digits = [8, 6, 7, 1, 0]
res = S.largestMultipleOfThree(digits)
print(res)
