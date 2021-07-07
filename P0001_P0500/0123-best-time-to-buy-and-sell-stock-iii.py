# https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-iii/
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        left = [0] * n
        right = [0] * n
        minv = prices[0]
        for i in range(1, len(prices)):
            left[i] = max(left[i-1], prices[i] - minv)
            minv = min(minv, prices[i])
        res = left[n-1] + right[n-1]
        maxv = prices[n-1]
        for j in range(n-2, -1, -1):
            right[j] = max(right[j+1], maxv - prices[j])
            maxv = max(maxv, prices[j])
            res = max(res, left[j] + right[j])
        return res

# 方法二：考虑每天可能出现的状态


class Solution2:
    def maxProfit(self, prices: List[int]) -> int:
        buy1 = buy2 = -prices[0]
        sell1 = sell2 = 0
        for i in range(1, len(prices)):
            buy1 = max(buy1, -prices[i])
            sell1 = max(sell1, buy1 + prices[i])
            buy2 = max(buy2, sell1 - prices[i])
            sell2 = max(sell2, buy2 + prices[i])
        return sell2


S = Solution()
prices = [3, 3, 5, 0, 0, 3, 1, 4]
print(S.maxProfit(prices))
