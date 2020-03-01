"""
https://leetcode.com/problems/reverse-string-ii/

Given a string and an integer k, you need to reverse the first k characters for every 2k characters counting from the start of the string. 
If there are less than k characters left, reverse all of them. If there are less than 2k but greater than or equal to k characters, 
then reverse the first k characters and left the other as original.

Example:
Input: s = "abcdefg", k = 2
Output: "bacdfeg"
"""


class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        res = ''
        for i in range(0, len(s), 2 * k):
            end = min(i+2*k, len(s))
            si = s[i:end]
            if len(si) <= k:
                si = self.func(si)
            elif len(si) > k:
                si = self.func(si[0:k]) + si[k:]
            res += si
        return res

    def func(self, s):
        s = list(s)
        for i in range(len(s) // 2):
            j = len(s) - 1 - i
            tmp = s[i]
            s[i] = s[j]
            s[j] = tmp
        return ''.join(s)


S = Solution()
s = "abcdefg"
k = 2
print(S.reverseStr(s, k))
