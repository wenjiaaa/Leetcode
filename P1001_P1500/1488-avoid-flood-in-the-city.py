"""
    https://leetcode.com/problems/avoid-flood-in-the-city/


Your country has an infinite number of lakes. Initially, all the lakes are empty, but when it rains over the nth lake, the nth lake becomes full of water. If it rains over a lake which is full of water, there will be a flood. Your goal is to avoid the flood in any lake.

Given an integer array rains where:

rains[i] > 0 means there will be rains over the rains[i] lake.
rains[i] == 0 means there are no rains this day and you can choose one lake this day and dry it.
Return an array ans where:

ans.length == rains.length
ans[i] == -1 if rains[i] > 0.
ans[i] is the lake you choose to dry in the ith day if rains[i] == 0.
If there are multiple valid answers return any of them. If it is impossible to avoid flood return an empty array.

Notice that if you chose to dry a full lake, it becomes empty, but if you chose to dry an empty lake, nothing changes. (see example 4)

Example 1:

Input: rains = [1,2,3,4]
Output: [-1,-1,-1,-1]
Explanation: After the first day full lakes are [1]
After the second day full lakes are [1,2]
After the third day full lakes are [1,2,3]
After the fourth day full lakes are [1,2,3,4]
There's no day to dry any lake and there is no flood in any lake.

思路参考：https://www.youtube.com/watch?v=8sxeQyumrYc

"""

import bisect


class Solution:
    def avoidFlood(self, rains):
        last_rain = {}  # 存储每个湖最后一天下雨的日期
        sun = []   # 晴天
        res = [-1] * len(rains)
        for day, lake in enumerate(rains):
            if lake == 0:
                sun.append(day)
                res[day] = 1
            elif lake in last_rain:
                it = bisect.bisect_left(
                    sun, last_rain[lake])  # 二分查找，最接近上一次下雨的晴天
                if it == len(sun):
                    return []  # 无解
                else:
                    res[sun[it]] = lake
                    sun.pop(it)
            last_rain[lake] = day
        return res


S = Solution()
rains = [0, 1, 3, 0, 2, 0, 1, 2]
res = S.avoidFlood(rains)
print(res)
