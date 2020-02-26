"""
https://leetcode.com/problems/longest-increasing-subsequence/

Given an unsorted array of integers, find the length of longest increasing subsequence.

Example:

Input: [10,9,2,5,3,7,101,18]
Output: 4 
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4. 
Note:

There may be more than one LIS combination, it is only necessary for you to return the length.
Your algorithm should run in O(n2) complexity.
Follow up: Could you improve it to O(n log n) time complexity?

"""


# O(n^2)
class Solution1:
    def lengthOfLIS(self, nums):
        if not nums:
            return 0
        res = [0] * len(nums)
        res[0] = 1
        for i in range(len(nums)):
            tmp = 0
            for j in range(0, i):
                if nums[j] < nums[i]:
                    tmp = max(tmp, res[j])
            res[i] = tmp + 1
        return max(res)


# O(nlogn)
class Solution:
    def lengthOfLIS(self, nums):
        if not nums:
            return 0
        res = [nums[0]]
        for i, n in enumerate(nums[1:]):
            if n > res[-1]:
                res.append(n)
            else:
                idx = self.bisearch(res, 0, len(res)-1, n)
                res[idx] = n
        return len(res)

    def bisearch(self, nums, left, right, target):
        while left < right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left += 1
            else:
                right -= 1
        assert left == right
        return right


S = Solution()
nums = [5, 2, 3, 7, 4, 1, 2]
res = S.lengthOfLIS(nums)
print(res)
