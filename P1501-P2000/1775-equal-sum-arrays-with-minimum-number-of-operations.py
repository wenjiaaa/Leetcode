# https://leetcode.com/problems/equal-sum-arrays-with-minimum-number-of-operations/
"""
参考：https://leetcode.com/problems/equal-sum-arrays-with-minimum-number-of-operations/discuss/1085786/JavaPython-3-2-Greedy-codes%3A-sort-and-count-w-brief-explanation-and-analysis.

Method 1: Sort and 2 pointers
1. Sort both arrays and get their sums respectively: sum1 and sum2;
2. Use two pointers in the two arrays; one pointer from left to right in the array with smaller sum and the other from right to left in the array with bigger sum;
3. In the array with smaller sum, check the difference between current element with 6; in the array with bigger sum, check the difference between current element with 1; choose the larger difference and add it to sum1.
4. repeat 3 till sum1 >= sum2.

Time: O(m * logm + n * logn), space: O(m + n), where m = nums1.length, n = nums2.length.
"""


class Solution(object):
    def minOperations(self, nums1, nums2):
        """
        : type nums1: List[int]
        : type nums2: List[int]
        : rtype: int
        """
        if len(nums1) > len(nums2) * 6 or len(nums2) > len(nums1) * 6:
            return - 1
        sum1, sum2 = sum(nums1), sum(nums2)
        if sum1 > sum2:
            return self.minOperations(nums2, nums1)  # 保证第一个数组比第二个数组的和小
        nums1.sort()
        nums2.sort()
        i, j = 0, len(nums2) - 1
        cnt = 0
        while (sum1 < sum2):  # 最后跳出循环时，二者不一定相等。可能是sum1>sum2，但是对结果没影响。
            if j > 0 and i < len(nums1) and 6 - nums1[i] > nums2[j] - 1:
                sum1 += (6 - nums1[i])  # 让nums1中的数字增加到6
                i += 1
            else:
                sum2 -= (nums2[j] - 1)  # 让nums2中的数字减小到1
                j -= 1
            cnt += 1
        return cnt


S = Solution()
nums1 = [1, 2, 3, 4, 5, 6]
nums2 = [1, 1, 2, 2, 2, 2]
print(S.minOperations(nums1, nums2))
