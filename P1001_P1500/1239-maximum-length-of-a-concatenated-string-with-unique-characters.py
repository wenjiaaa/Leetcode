"""
https://leetcode.com/problems/maximum-length-of-a-concatenated-string-with-unique-characters/

Given an array of strings arr. String s is a concatenation of a sub-sequence of arr which have unique characters.

Return the maximum possible length of s.


Example 1:

Input: arr = ["un","iq","ue"]
Output: 4
Explanation: All possible concatenations are "","un","iq","ue","uniq" and "ique".
Maximum length is 4.
Example 2:

Input: arr = ["cha","r","act","ers"]
Output: 6
Explanation: Possible solutions are "chaers" and "acters".
Example 3:

Input: arr = ["abcdefghijklmnopqrstuvwxyz"]
Output: 26

"""


class Solution:
    def maxLength(self, arr):
        subsets = [""]
        res = 0
        for a in arr:
            new_sub = []
            for item in subsets:
                tmp = item + a
                if len(set(tmp)) == len(tmp):
                    res = max(res, len(tmp))
                    # 只添加没有重复字母的子集
                    new_sub.append(tmp)
            subsets += new_sub
        print(subsets)
        return res


S = Solution()
arr = ["cha", "r", "act", "ers"]
res = S.maxLength(arr)
print(res)
