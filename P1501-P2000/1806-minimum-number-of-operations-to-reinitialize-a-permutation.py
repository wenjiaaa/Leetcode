# https://leetcode.com/problems/minimum-number-of-operations-to-reinitialize-a-permutation/
class Solution(object):
    def reinitializePermutation(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = 0
        perm = [i for i in range(n)]
        arr = [0] * n
        init = [i for i in range(n)]
        while arr != init:
            for i in range(n):
                if i % 2 == 0:
                    arr[i] = perm[i // 2]
                    #print(i, arr[i], perm)
                else:
                    arr[i] = perm[n // 2 + (i - 1) // 2]
                    #print(i, arr[i], perm)

            perm = arr.copy()

            res += 1
        return res


S = Solution()
n = 4
print(S.reinitializePermutation(n))
