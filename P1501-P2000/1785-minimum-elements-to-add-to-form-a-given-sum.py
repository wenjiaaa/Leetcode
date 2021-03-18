# https://leetcode.com/problems/minimum-elements-to-add-to-form-a-given-sum/

class Solution(object):
    def minElements(self, nums, limit, goal):
        """
        :type nums: List[int]
        :type limit: int
        :type goal: int
        :rtype: int
        """
        sum_raw = sum(nums)
        target = abs(goal - sum_raw)
        if target <= limit:
            return 1
        else:
            cnt, target = target // limit, target % limit
            if target == 0:
                return cnt
            else:
                return cnt+1
