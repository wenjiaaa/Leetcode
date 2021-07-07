# https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock/
from typing import List

# 假设在第i天卖出，那么一定想找前i-1天里最低的价格买入


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # dp[i] 表示第i天的最大利润
        # dp[i] = max(dp[i-1], prices[i] - min(prices[0:i]))
        dp = 0
        minv = prices[0]
        for i in range(1, len(prices)):
            minv = min(prices[i], minv)
            dp = max(dp, prices[i] - minv)
        return dp


class Solution2:
    def maxProfit(self, prices: List[int]) -> int:
        sell = 0
        buy = -prices[0]
        for i in range(1, len(prices)):
            sell = max(sell, buy + prices[i])
            buy = max(buy, -prices[i])
        return sell


S = Solution()
prices = [7, 1, 5, 3, 6, 4]
print(S.maxProfit(prices))
