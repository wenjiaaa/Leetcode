"""
https://leetcode.com/problems/can-make-arithmetic-progression-from-sequence/

Given an array of numbers arr. A sequence of numbers is called an arithmetic progression if the difference between any two consecutive elements is the same.

Return true if the array can be rearranged to form an arithmetic progression, otherwise, return false.

Input: arr = [3,5,1]
Output: true
Explanation: We can reorder the elements as [1,3,5] or [5,3,1] with differences 2 and -2 respectively, between each consecutive elements.
Example 2:

Input: arr = [1,2,4]
Output: false
Explanation: There is no way to reorder the elements to obtain an arithmetic progression.


"""


class Solution:
    def canMakeArithmeticProgression(self, arr):
        if len(arr) < 2:
            return False
        arr = sorted(arr)
        diff = arr[1] - arr[0]
        for i in range(2, len(arr)):
            if arr[i] - arr[i - 1] != diff:
                return False
        return True


S = Solution()
arr = [1, 2, 4]
res = S.canMakeArithmeticProgression(arr)
print(res)
