"""
https://leetcode.com/problems/single-element-in-a-sorted-array/

You are given a sorted array consisting of only integers where every element appears exactly twice, except for one element which appears exactly once. Find this single element that appears only once.

Follow up: Your solution should run in O(log n) time and O(1) space.

 

Example 1:

Input: nums = [1,1,2,3,3,4,4,8,8]
Output: 2
Example 2:

Input: nums = [3,3,7,7,10,11,11]
Output: 10

"""


class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]
        if nums[0] != nums[1]:
            return nums[0]
        if nums[-1] != nums[-2]:
            return nums[-1]
        # 根据下标是否能被2整除，来判断目标是在左边还是右边
        left, right = 0, len(nums) - 1
        while (left <= right):
            mid = (left + right) // 2
            if nums[mid] != nums[mid - 1] and nums[mid] != nums[mid + 1]:
                return nums[mid]
            elif (nums[mid] == nums[mid - 1] and (mid - 1) % 2 == 0) or (nums[mid] == nums[mid + 1] and mid % 2 == 0):
                left = mid + 1
            elif (nums[mid] == nums[mid - 1] and (mid - 1) % 2 != 0) or (nums[mid] == nums[mid + 1] and mid % 2 != 0):
                right = mid - 1


nums = [3, 3, 7, 7, 10, 11, 11]
S = Solution()
print(S.singleNonDuplicate(nums))
