# https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/

class Solution(object):
    def shipWithinDays(self, weights, D):
        """
        :type weights: List[int]
        :type D: int
        :rtype: int
        """
        low, high = max(weights), sum(weights)
        while (low <= high):
            mid = (low + high) // 2
            day = self.days(weights, mid)
            print(low, high, mid, day)
            if day <= D:
                high = mid - 1
            else:
                low = mid + 1
        # if self.days(weights, low) <= D:
        #    return low
        return mid

    def days(self, weights, cap):
        day = 1
        cur_cap = 0
        for w in weights:
            cur_cap += w
            if cur_cap > cap:
                day += 1
                cur_cap = w

        return day


weights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
D = 5
#weights = [3, 2, 2, 4, 1, 4]
#D = 3
S = Solution()
print(S.shipWithinDays(weights, D))
