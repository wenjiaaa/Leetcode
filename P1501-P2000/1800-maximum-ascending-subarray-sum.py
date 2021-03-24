# https://leetcode.com/problems/maximum-ascending-subarray-sum/
class Solution(object):
    def maxAscendingSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        pre = 0
        cur_sum = 0
        for n in nums:
            if n > pre:
                cur_sum += n
            else:
                res = max(res, cur_sum)
                cur_sum = n
            pre = n

        return max(res, cur_sum)


S = Solution()
nums = [12, 17, 15, 13, 10, 11, 12]
print(S.maxAscendingSum(nums))
