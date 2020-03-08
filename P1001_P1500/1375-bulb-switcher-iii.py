"""
https://leetcode.com/problems/bulb-switcher-iii/
There is a room with n bulbs, numbered from 1 to n, arranged in a row from left to right. 
Initially, all the bulbs are turned off.

At moment k (for k from 0 to n - 1), we turn on the light[k] bulb. A bulb change color to blue 
only if it is on and all the previous bulbs (to the left) are turned on too.

Return the number of moments in which all turned on bulbs are blue.
Example 1:
Input: light = [2,1,3,5,4]
Output: 3
Explanation: All bulbs turned on, are blue at the moment 1, 2 and 4.

Example 2:
Input: light = [3,2,4,1,5]
Output: 2
Explanation: All bulbs turned on, are blue at the moment 3, and 4 (index-0).

Example 3:
Input: light = [4,1,2,3]
Output: 1
Explanation: All bulbs turned on, are blue at the moment 3 (index-0).
Bulb 4th changes to blue at the moment 3.
 
"""


class Solution(object):
    def numTimesAllBlue(self, light):
        """
        :type light: List[int]
        :rtype: int
        """
        res = 0
        max_number = 0
        S = 0
        for i in range(len(light)):
            light_number = light[i]
            S += light_number
            max_number = max(max_number, light_number)
            full_sum = (1 + max_number) * max_number // 2
            if S == full_sum:
                res += 1
        return res


S = Solution()
light = [4, 1, 2, 3]
res = S.numTimesAllBlue(light)
print(res)
