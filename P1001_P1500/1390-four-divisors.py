"""
https://leetcode.com/problems/four-divisors/

Given an integer array nums, return the sum of divisors of the integers in that array that have exactly four divisors.

If there is no such integer in the array, return 0.

 

Example 1:

Input: nums = [21,4,7]
Output: 32
Explanation:
21 has 4 divisors: 1, 3, 7, 21
4 has 3 divisors: 1, 2, 4
7 has 2 divisors: 1, 7
The answer is the sum of divisors of 21 only.
"""

import math


class Solution:
    def sumFourDivisors(self, nums):
        ans = 0
        for num in nums:
            ans += self.check(num)
        return ans

    def check(self, num):
        mid = math.sqrt(num)
        # 如果这个数能开方，那说明要么有3个divisor，要么有5个及以上，肯定不会是4个
        if int(mid) == mid:
            return 0
        res = []
        for i in range(1, int(mid)+1):
            j = num // i
            if i * j == num:
                res.extend([i, j])
            if len(res) > 4:
                return 0
        if len(res) < 4:
            return 0
        return sum(res)


S = Solution()
nums = [99, 21, 4, 7]
print(S.sumFourDivisors(nums))
