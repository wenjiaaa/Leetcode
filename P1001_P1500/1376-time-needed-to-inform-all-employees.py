"""
https://leetcode.com/problems/time-needed-to-inform-all-employees/submissions/

A company has n employees with a unique ID for each employee from 0 to n - 1. The head of the company 
has is the one with headID.

Each employee has one direct manager given in the manager array where manager[i] is the direct manager 
of the i-th employee, manager[headID] = -1. Also it's guaranteed that the subordination relationships 
have a tree structure.

The head of the company wants to inform all the employees of the company of an urgent piece of news. 
He will inform his direct subordinates and they will inform their subordinates and so on until all 
employees know about the urgent news.

The i-th employee needs informTime[i] minutes to inform all of his direct subordinates (i.e After 
informTime[i] minutes, all his direct subordinates can start spreading the news).

Return the number of minutes needed to inform all the employees about the urgent news.

 
Example 1:

Input: n = 1, headID = 0, manager = [-1], informTime = [0]
Output: 0
Explanation: The head of the company is the only employee in the company.

Example 2:
Input: n = 6, headID = 2, manager = [2,2,-1,2,2,2], informTime = [0,0,1,0,0,0]
Output: 1
Explanation: The head of the company with id = 2 is the direct manager of all the employees in 
the company and needs 1 minute to inform them all.
The tree structure of the employees in the company is shown.
"""


# BFS
from collections import defaultdict


class Solution(object):
    def numOfMinutes(self, n, headID, manager, informTime):
        if n <= 1:
            return 0
        rst = 0
        childs = defaultdict(list)
        for idx, parent in enumerate(manager):
            childs[parent].append(idx)

        q = [(headID, informTime[headID])]
        while q:
            cur_id, cur_time = q[0]
            q.pop(0)
            # calculate max
            rst = max(rst, cur_time)
            for child in childs[cur_id]:
                q.append((child, cur_time + informTime[child]))
        return rst


# DFS
class Solution1:
    def numOfMinutes(self, n, headID, manager, informTime):
        subordinate = dict()  # employee tree
        for i, m in enumerate(manager):
            subordinate.setdefault(m, []).append(i)

        def dfs(node):
            return informTime[node] + max((dfs(n) for n in subordinate.get(node, [])), default=0)

        return dfs(headID)


S = Solution1()
n = 11
headID = 4
manager = [5, 9, 6, 10, -1, 8, 9, 1, 9, 3, 4]
informTime = [0, 213, 0, 253, 686, 170, 975, 0, 261, 309, 337]
res = S.numOfMinutes(n, headID, manager, informTime)
print(res)
