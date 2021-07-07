# https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-iv/
from typing import List


class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        if n == 0:
            return 0
        if k == 1:
            return self.fun(prices)
        if k >= n//2:
            k = n//2

        sell = [0] * (k+1)
        buy = [-prices[0]] * (k+1)
        for i in range(1, n):
            for ki in range(1, k+1):
                sell[ki] = max(sell[ki], buy[ki] + prices[i])
                buy[ki] = max(buy[ki], sell[ki - 1] - prices[i])
        return sell[k]

    def fun(self, prices):
        n = len(prices)
        sell = 0
        buy = -prices[0]
        for i in range(1, n):
            sell = max(sell, buy + prices[i])
            buy = max(buy, -prices[i])
        return sell


S = Solution()
k = 2
prices = [3, 3, 5, 0, 0, 3, 1, 4]
print(S.maxProfit(k, prices))
