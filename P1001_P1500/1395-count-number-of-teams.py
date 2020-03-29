"""
https://leetcode.com/problems/count-number-of-teams/

There are n soldiers standing in a line. Each soldier is assigned a unique rating value.

You have to form a team of 3 soldiers amongst them under the following rules:

Choose 3 soldiers with index (i, j, k) with rating (rating[i], rating[j], rating[k]).
A team is valid if:  (rating[i] < rating[j] < rating[k]) or (rating[i] > rating[j] > rating[k]) 
where (0 <= i < j < k < n).
Return the number of teams you can form given the conditions. (soldiers can be part of multiple teams).

 

Example 1:

Input: rating = [2,5,3,4,1]
Output: 3
Explanation: We can form three teams given the conditions. (2,3,4), (5,4,1), (5,3,1). 
Example 2:

Input: rating = [2,1,3]
Output: 0
Explanation: We can't form any team given the conditions.
Example 3:

Input: rating = [1,2,3,4]
Output: 4

参考了讨论区解法：https://leetcode.com/problems/count-number-of-teams/discuss/554918/Python-Easy-O(N2)-DP-solution
"""

from collections import defaultdict


class Solution:
    def numTeams(self, rating):
        if len(rating) < 3:
            return 0
        greater = defaultdict(int)
        less = defaultdict(int)
        res = 0
        for i in range(len(rating) - 1):
            for j in range(i + 1, len(rating)):
                if rating[j] > rating[i]:
                    greater[i] += 1
                else:
                    less[i] += 1
        for i in range(len(rating) - 2):
            for j in range(i + 1, len(rating)):
                if rating[j] > rating[i]:
                    res += greater[j]
                else:
                    res += less[j]
        return res
