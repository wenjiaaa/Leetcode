"""
https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/

\Given a sorted array nums, remove the duplicates in-place such that duplicates appeared at most twice 
and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place 
with O(1) extra memory.

Example 1:

Given nums = [1,1,1,2,2,3],

Your function should return length = 5, with the first five elements of nums being 1, 1, 2, 2 and 3 respectively.

It doesn't matter what you leave beyond the returned length.
Example 2:

Given nums = [0,0,1,1,1,1,2,3,3],

Your function should return length = 7, with the first seven elements of nums being modified to 0, 0, 1, 1, 2, 3 
and 3 respectively.

It doesn't matter what values are set beyond the returned length.

"""


class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 3:
            return len(nums)
        l = 1
        for i in range(2, len(nums)):
            if nums[i] != nums[l] or nums[i] == nums[l] and nums[i] != nums[l-1]:
                l += 1
                nums[l] = nums[i]
        return l+1


S = Solution()
nums = [1, 1, 1, 2, 2, 3]
res = S.removeDuplicates(nums)
print(res, nums)
