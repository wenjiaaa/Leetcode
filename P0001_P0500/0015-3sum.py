"""
https://leetcode.com/problems/3sum/

Given an array nums of n integers, are there elements a, b, c in nums 
such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:

The solution set must not contain duplicate triplets.

Example:

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
"""


# 双指针， O(n^2)， 这个方法适用于任何target，不一定非要和等于0
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        if len(nums) < 3:
            return res
        nums.sort()
        for k in range(len(nums)):
            # 由于数组是升序排列，因此如果第一个数大于0，那和肯定不可能为0了
            if nums[k] > 0:
                break
            # 如果连续两个数相等，则需要去重，跳过
            if nums[k] == nums[k-1] and k != 0:
                continue
            target = -nums[k]
            i = k+1
            j = len(nums) - 1
            while i < j:
                if nums[i] + nums[j] == target:
                    if [nums[k], nums[i], nums[j]] not in res:
                        res.append([nums[k], nums[i], nums[j]])
                    i += 1
                    j -= 1
                elif nums[i] + nums[j] < target:
                    i += 1
                else:
                    j -= 1
        return res

# 参考答案里面的O(n)的解法， 把数组分为正数， 负数， 和必须是0


class Solution1:
    def threeSum(self, nums):
        res = set()
        pos = set()
        neg = set()
        D = {}
        for num in nums:
            D[num] = D.get(num, 0) + 1
            if num > 0:
                pos.add(num)
            elif num < 0:
                neg.add(num)
        if D.get(0, 0) >= 3:  # 如果0的个数大于等于3说明肯定有解
            res.add((0, 0, 0))
        for m in pos:
            D[m] -= 1
            for n in neg:
                D[n] -= 1
                target = -(m + n)
                if target in D and D[target] > 0:
                    # 排序去重
                    res.add(tuple(sorted((m, n, target))))
                D[n] += 1
            D[m] += 1
        return list(res)


S = Solution1()
nums = [-2, -2, 0, 0, 2, 2]
res = S.threeSum(nums)
print(res)
