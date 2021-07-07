from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        sell = 0
        buy = -prices[0]
        for i in range(1, len(prices)):
            sell = max(sell, buy + prices[i])
            buy = max(buy, sell - prices[i])
        return sell


S = Solution()
prices = [7, 1, 5, 3, 6, 4]
print(S.maxProfit(prices))
