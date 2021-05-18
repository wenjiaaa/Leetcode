# https://leetcode-cn.com/problems/maximum-subarray/
from typing import List


class Solution1:
    def maxSubArray(self, nums: List[int]) -> int:
        res = 0
        tmp_sum = 0
        for i in range(len(nums)):
            tmp_sum += nums[i]
            if tmp_sum < 0:
                tmp_sum = 0
            res = max(res, tmp_sum)

        return res


class Solution:
    # 方法二：动态规划，dp[i]表示到到第i个元素为止的最大连续子序列和
    def maxSubArray(self, nums: List[int]) -> int:
        dp = nums[0]
        res = nums[0]
        for i in range(1, len(nums)):
            dp = max(dp + nums[i], nums[i])
            res = max(res, dp)
        return res


S = Solution()
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(S.maxSubArray(nums))
