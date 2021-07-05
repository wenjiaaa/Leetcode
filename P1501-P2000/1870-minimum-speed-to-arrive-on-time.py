# https://leetcode-cn.com/problems/minimum-speed-to-arrive-on-time/
from typing import List
import math


class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        # 确定速度的上下界，对于二分的上界，
        # 我们考虑 hours 为两位小数，因此对于最后一段路程，最小的时限为 0.01，
        # 所以最高时速就是dist[i]/0.01， dist[i]最大为10^5，因此时速最高为10^7
        # 最高时速为10^7, dist[-1]/0.01 均可
        left, right = 1, dist[-1] * 100
        n = len(dist)
        # 前 n - 1 段至少需要 n - 1 时间完成，同时最后一段的花费时间必定为正数。
        # 因此如果时限 hour <= n-1，那么显然无法完成，此时应返回 -1
        if hour <= n-1:
            return -1
        while left < right:
            mid = (left + right) // 2
            cost = self.time_cost(mid, dist)
            if cost <= hour:
                right = mid
            else:
                left = mid + 1
        return left

    def time_cost(self, speed, dist):
        # 计算给定速度时，花费的总时长。前n-1段需要向上取整，最后一段只要dist[i]/speed即可
        cost = 0
        for i in range(len(dist)):
            cost += dist[i]/speed
            if i != len(dist) - 1:
                cost = math.ceil(cost)
        return cost


S = Solution()
dist = [1, 3, 2]
hour = 1
print(S.minSpeedOnTime(dist, hour))
