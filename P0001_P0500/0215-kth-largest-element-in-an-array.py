# https: // leetcode-cn.com/problems/kth-largest-element-in-an-array/
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return self.quicksort(nums, 0, len(nums) - 1, k)

    def quicksort(self, nums: List[int], left: int, right: int, k: int) -> int:
        v = self.partition(nums, left, right)
        if v == len(nums) - k:
            return nums[v]
        elif len(nums) - k < v:
            return self.quicksort(nums, left, v - 1, k)

        else:
            return self.quicksort(nums, v + 1, right, k)

    def partition(self, nums, left, right):
        l, r = left, right
        key = nums[left]
        while (l < r):
            while (l < r and nums[r] > key):
                r -= 1
            if (l < r):
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
            while (l < r and nums[l] < key):
                l += 1
            if (l < r):
                nums[l], nums[r] = nums[r], nums[l]
                r -= 1
        return l


S = Solution()
nums = [47, 29, 71, 99, 78, 19, 24, 47]
print(S.findKthLargest(nums,  2))
