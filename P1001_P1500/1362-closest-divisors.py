"""
https://leetcode.com/problems/closest-divisors/

Given an integer num, find the closest two integers in absolute difference whose product equals num + 1 or num + 2.

Return the two integers in any order.

Example 1:

Input: num = 8
Output: [3,3]
Explanation: For num + 1 = 9, the closest divisors are 3 & 3, for num + 2 = 10, 
the closest divisors are 2 & 5, hence 3 & 3 is chosen.
Example 2:

Input: num = 123
Output: [5,25]
Example 3:

Input: num = 999
Output: [40,25]


"""

import math


class Solution:
    def closestDivisors(self, num: int):
        v1 = num + 1
        v2 = num + 2
        num_sqrt = math.ceil(num ** 0.5)
        for i in range(num_sqrt, -1, -1):
            if v1 / i == v1 // i:
                return [i, v1 // i]
            if v2 / i == v2 // i:
                return [i, v2 // i]


S = Solution()
num = 999
res = S.closestDivisors(num)
print(res)
