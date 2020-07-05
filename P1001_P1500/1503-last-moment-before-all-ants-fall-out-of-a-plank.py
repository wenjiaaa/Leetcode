"""
https://leetcode.com/problems/last-moment-before-all-ants-fall-out-of-a-plank/

We have a wooden plank of the length n units. Some ants are walking on the plank, each ant moves with speed 1 unit per second. Some of the ants move to the left, the other move to the right.

When two ants moving in two different directions meet at some point, they change their directions and continue moving again. Assume changing directions doesn't take any additional time.

When an ant reaches one end of the plank at a time t, it falls out of the plank imediately.

Given an integer n and two integer arrays left and right, the positions of the ants moving to the left and the right. Return the moment when the last ant(s) fall out of the plank.

"""


class Solution:
    def getLastMoment(self, n, left, right):
        if len(left) == 0 and len(right) == 0:
            return 0
        elif len(right) == 0:
            return max(left)
        elif len(left) == 0:
            return n - min(right)
        else:
            return max(max(left), n-min(right))


S = Solution()
n = 9
left = [5]
right = [4]
res = S.getLastMoment(n, left, right)
print(res)
