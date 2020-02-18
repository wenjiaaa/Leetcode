"""
https://leetcode.com/problems/first-unique-character-in-a-string/
"""

import collections


class Solution:
    def firstUniqChar(self, s: str) -> int:
        cnt = collections.Counter(s)
        for i in range(len(s)):
            if cnt[s[i]] == 1:
                return i
        return - 1


S = Solution()
s = "loveleetcode"
print(S.firstUniqChar(s))
