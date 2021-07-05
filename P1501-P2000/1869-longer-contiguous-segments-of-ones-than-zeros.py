# https://leetcode-cn.com/problems/longer-contiguous-segments-of-ones-than-zeros/
from typing import List


class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        max_1, max_0 = 0, 0
        tmp_1, tmp_0 = 0, 0
        for i in range(len(s)):
            if s[i] == '1':
                tmp_1 += 1
                tmp_0 = 0
            else:
                tmp_1 = 0
                tmp_0 += 1
            max_1 = max(max_1, tmp_1)
            max_0 = max(max_0, tmp_0)
        return max_1 > max_0


S = Solution()
s = "110100010"
print(S.checkZeroOnes(s))
