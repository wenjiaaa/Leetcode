# https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        sell = 0
        buy = -prices[0]
        pre_sell = 0
        for i in range(1, n):
            nextsell = max(sell, buy + prices[i])
            nextbuy = max(buy, pre_sell - prices[i])
            pre_sell = sell
            sell = nextsell
            buy = nextbuy
        return sell


S = Solution()
prices = [1, 2, 3, 0, 2]
print(S.maxProfit(prices))
