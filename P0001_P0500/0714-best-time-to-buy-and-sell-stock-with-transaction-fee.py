# https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/

from typing import List


class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        sell = 0
        buy = -prices[0]
        for i in range(1, len(prices)):
            sell = max(sell, buy + prices[i] - fee)
            buy = max(buy, sell - prices[i])
        return sell


S = Solution()
prices = [1, 3, 2, 8, 4, 9]
fee = 2
print(S.maxProfit(prices, fee))
