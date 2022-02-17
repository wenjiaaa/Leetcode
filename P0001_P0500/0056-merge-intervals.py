# https://leetcode-cn.com/problems/merge-intervals/
from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 0:
            return []
        res = []
        intervals = sorted(intervals, key=lambda x: x[0])
        res.append(intervals[0])
        for i in range(1, len(intervals)):
            last = res[-1]
            if intervals[i][0] <= last[1]:
                res[-1][1] = max(last[1], intervals[i][1])
            else:
                res.append(intervals[i])
        return res


S = Solution()
intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
res = S.merge(intervals)
print(res)
