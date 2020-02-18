"""
https://leetcode.com/problems/reverse-words-in-a-string-iii/

Given a string, you need to reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

Example 1:
Input: "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"
"""


class Solution:
    def reverseWords(self, s: str) -> str:
        s_list = s.split(' ')
        res = []
        for si in s_list:
            si = list(si)
            for i in range(len(si) // 2):
                j = len(si) - 1 - i
                tmp = si[i]
                si[i] = si[j]
                si[j] = tmp
            res.append(''.join(si))
        return ' '.join(res)


S = Solution()
s = "Let's take LeetCode contest"
print(S.reverseWords(s))
