# https://leetcode-cn.com/problems/add-strings/
from typing import List


class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        n1 = len(num1) - 1
        n2 = len(num2) - 1
        val = 0
        res = ""
        while n1 >= 0 or n2 >= 0:
            # 返回 ASCII 数值
            x = ord(num1[n1]) - ord("0") if n1 >= 0 else 0
            y = ord(num2[n2]) - ord("0") if n2 >= 0 else 0
            tmp = x + y + val
            val = tmp // 10
            res = str(tmp % 10) + res
            n1, n2 = n1-1, n2 - 1
        if val != 0:
            res = str(val) + res
        return res


S = Solution()
num1 = "1929"
num2 = "222"
print(S.addStrings(num1, num2))
