# https://leetcode.com/problems/maximum-value-at-a-given-index-in-a-bounded-array/
class Solution(object):
    def maxValue(self, n, index, maxSum):
        """
        :type n: int
        :type index: int
        :type maxSum: int
        :rtype: int
        """
        def check(target):
            # 先处理[0:index)，个数index
            if target <= index:
                sum1 = (1 + target - 1) * (target - 1) // 2 + \
                    (index - target + 1)
            else:
                sum1 = (target - index + target - 1) * index // 2

            # 再处理[index:n) ，个数 n-index
            if target < n - index:
                sum2 = (1 + target) * target // 2 + (n - index - target)
            else:
                sum2 = (target - (n - index - 1) + target) * (n - index) // 2
            return sum1 + sum2

        left, right = 1, maxSum
        while (left < right):
            mid = (left + right) // 2
            S = check(mid)
            if S == maxSum:
                return mid
            elif S < maxSum:
                left = mid + 1
            else:
                right = mid - 1
        if check(left) <= maxSum:
            return left
        else:
            return left - 1


S = Solution()
n = 5
index = 0
maxSum = 28
print(S.maxValue(n, index, maxSum))
