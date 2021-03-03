# https://leetcode.com/problems/closest-dessert-cost/

class Solution(object):
    def closestCost(self, baseCosts, toppingCosts, target):
        """
        :type baseCosts: List[int]
        :type toppingCosts: List[int]
        :type target: int
        :rtype: int
        """
        global ans
        ans = baseCosts[0]
        for i in range(len(baseCosts)):
            self.helper(toppingCosts, target, baseCosts[i], 0)
        return ans

    def helper(self, toppingCosts, target, cost, idx):
        global ans
        if abs(target - cost) < abs(target - ans):
            ans = cost
        elif abs(target - cost) == abs(target - ans):
            ans = min(ans, cost)
        if idx == len(toppingCosts):
            return ans
        # 每个topping可以被选0,1,2次
        for i in range(0, 3):
            self.helper(toppingCosts, target, cost +
                        toppingCosts[idx] * i, idx + 1)


S = Solution()
baseCosts = [10]
toppingCosts = [1]
target = 1
print(S.closestCost(baseCosts, toppingCosts, target))
