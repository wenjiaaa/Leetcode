"""
https://leetcode.com/problems/peak-index-in-a-mountain-array/

852. Peak Index in a Mountain Array
Easy

918

1325

Add to List

Share
Let's call an array arr a mountain if the following properties hold:

arr.length >= 3
There exists some i with 0 < i < arr.length - 1 such that:
arr[0] < arr[1] < ... arr[i-1] < arr[i]
arr[i] > arr[i+1] > ... > arr[arr.length - 1]
Given an integer array arr that is guaranteed to be a mountain, return any i such that arr[0] < arr[1] < ... arr[i - 1] < arr[i] > arr[i + 1] > ... > arr[arr.length - 1].

 

Example 1:

Input: arr = [0,1,0]
Output: 1
Example 2:

Input: arr = [0,2,1,0]
Output: 1
"""


class Solution(object):
    def peakIndexInMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """

        """
        ##  O(n)
        for i in range(len(arr)):
            if i == 0 and arr[i] >= arr[i + 1]:
                return 0
            elif i == len(arr) - 1 and arr[i] >= arr[i - 1]:
                return len(arr) - 1
            elif arr[i] >= arr[i - 1] and arr[i] >= arr[i + 1]:
                return i
        """

        # O(n^2)
        if arr[0] >= arr[1]:
            return 0
        if arr[-1] >= arr[-2]:
            return len(arr) - 1
        left, right = 0, len(arr)-1
        while (left <= right):
            mid = (left + right) // 2
            if arr[mid] >= arr[mid-1] and arr[mid] >= arr[mid+1]:
                return mid
            elif arr[mid] <= arr[mid+1]:
                left = mid + 1
            elif arr[mid] <= arr[mid-1]:
                right = mid - 1
        return mid


S = Solution()
arr = [3, 4, 5, 1]
print(S.peakIndexInMountainArray(arr))
