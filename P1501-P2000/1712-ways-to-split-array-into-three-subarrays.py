"""
https://leetcode.com/problems/ways-to-split-array-into-three-subarrays/

A split of an integer array is good if:

The array is split into three non-empty contiguous subarrays - named left, mid, right respectively from left to right.
The sum of the elements in left is less than or equal to the sum of the elements in mid, and the sum of the elements in mid is less than or equal to the sum of the elements in right.
Given nums, an array of non-negative integers, return the number of good ways to split nums. As the number may be too large, return it modulo 109 + 7.

Example 1:

Input: nums = [1,1,1]
Output: 1
Explanation: The only good way to split nums is [1] [1] [1].
Example 2:

Input: nums = [1,2,2,2,5,0]
Output: 3
Explanation: There are three good ways of splitting nums:
[1] [2] [2,2,5,0]
[1] [2,2] [2,5,0]
[1,2] [2,2] [5,0]
Example 3:

Input: nums = [3,2,1]
Output: 0
Explanation: There is no good way to split nums.
"""


# O(n^2) 数组被分成3段，那么就有2个隔板i,j,遍历这两个隔板
# O（nlogn） 首选循环j, 然后用二分法确定i的位置
import bisect


class Solution:
    def waysToSplit(self, nums):
        prefix = [0]
        for x in nums:
            prefix.append(prefix[-1] + x)
        # prefix[i] <= prefix[j] - prefix[i] <= prefix[-1] - prefix[j]
        # prefix[j] >= 2* prefix[i]
        # prefix[k] <= (prefix[-1] + prefix[i]) // 2
        ans = 0
        for i in range(1, len(prefix)):
            j = bisect.bisect_left(prefix, 2*prefix[i])  # 左边界
            k = bisect.bisect_right(prefix, (prefix[i] + prefix[-1])//2)  # 右边界
            ans += max(0, min(len(nums), k) - max(i+1, j))
        return ans % 1_000_000_007


S = Solution()
nums = [0, 3, 3]
print(S.waysToSplit(nums))
