# https://leetcode-cn.com/problems/add-to-array-form-of-integer/
from typing import List


class Solution:
    def addToArrayForm(self, num: List[int], K: int) -> List[int]:
        res = []
        n1 = len(num) - 1
        carry = 0
        while n1 >= 0 or K != 0:
            x = num[n1] if n1 >= 0 else 0
            y = K % 10 if K != 0 else 0
            sumv = x + y + carry
            carry = sumv // 10
            K = K // 10
            n1 -= 1
            res.insert(0, sumv % 10)
        if carry != 0:
            res.insert(0, 1)
        return res


S = Solution()
A = [1, 2, 6, 9]
K = 34
print(S.addToArrayForm(A, K))
