"""
https://leetcode.com/problems/letter-tile-possibilities/

You have a set of tiles, where each tile has one letter tiles[i] printed on it.  
Return the number of possible non-empty sequences of letters you can make.

 

Example 1:

Input: "AAB"
Output: 8
Explanation: The possible sequences are "A", "B", "AA", "AB", "BA", "AAB", "ABA", "BAA".
Example 2:

Input: "AAABBC"
Output: 188

思路： 先求出所有的子集（参考：78.subsets），再对每个子集求全排列（参考: 46,47）
"""


class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        self.res = 0
        subsets = self.subsets(tiles)
        for subset in subsets:
            if not subset:
                continue
            if len(set(subset)) == len(subset):
                sub_res = 1
                for i in range(1, len(subset) + 1):
                    sub_res = sub_res * i
                self.res += sub_res
            else:
                self.permutation(subset)
        return self.res

    def subsets(self, tiles):
        tiles = list(tiles)
        tiles.sort()
        res = [[]]
        for i in range(len(tiles)):
            tmp = []
            for item in res:
                if item + [tiles[i]] not in res:
                    tmp.append(item + [tiles[i]])
            res = res + tmp
        return res

    def permutation(self, nums):
        if not nums:
            self.res += 1
        for i in range(len(nums)):
            if nums[i] == nums[i - 1] and i > 0:
                continue
            self.permutation(nums[:i] + nums[i + 1:])


S = Solution()
tiles = 'AAABBC'
res = S.numTilePossibilities(tiles)
print(res)
