# https://leetcode.com/problems/maximum-average-pass-ratio/

import heapq


class Solution(object):
    def maxAverageRatio(self, classes, extraStudents):
        """
        :type classes: List[List[int]]
        :type extraStudents: int
        :rtype: float
        """
        res = 0
        for i in range(1, extraStudents + 1):
            min_ratio = 0
            for idx, item in enumerate(classes):
                if i == 1:
                    res += item[0]/item[1]
                ratio_diff = (item[0] + 1) / (item[1] + 1) - item[0] / item[1]
                if ratio_diff > min_ratio:
                    min_ratio = ratio_diff
                    change_idx = idx
            res += (classes[change_idx][0]+1)/(classes[change_idx][1]+1) - \
                classes[change_idx][0]/classes[change_idx][1]
            classes[change_idx] = [classes[change_idx]
                                   [0] + 1, classes[change_idx][1] + 1]

        return round(res/len(classes), 5)

# 用最大堆


class Solution2(object):
    def maxAverageRatio(self, classes, extraStudents):
        maxheap = []
        for a, b in classes:
            heapq.heappush(maxheap, [-(a + 1) / (b + 1) + a / b, a, b])
        for i in range(extraStudents):
            [diff, a, b] = heapq.heappop(maxheap)
            a += 1
            b += 1
            heapq.heappush(maxheap, [-(a + 1) / (b + 1) + a / b, a, b])
        res = 0
        for _, a, b in maxheap:
            res += a / b
        return round(res/len(classes), 5)


S = Solution2()
classes = [[2, 4], [3, 9], [4, 5], [2, 10]]
extraStudents = 4
print(S.maxAverageRatio(classes, extraStudents))
