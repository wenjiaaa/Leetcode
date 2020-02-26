"""
https://leetcode.com/problems/permutation-sequence/

The set [1,2,3,...,n] contains a total of n! unique permutations.

By listing and labeling all of the permutations in order, we get the following sequence for n = 3:

"123"
"132"
"213"
"231"
"312"
"321"
Given n and k, return the kth permutation sequence.

Note:

Given n will be between 1 and 9 inclusive.
Given k will be between 1 and n! inclusive.
Example 1:

Input: n = 3, k = 3
Output: "213"
Example 2:

Input: n = 4, k = 9
Output: "2314"

"""


# 按照求所有的全排列的方法，取第k个，超时
class Solution1:
    def getPermutation(self, n: int, k: int) -> str:
        nums = [i for i in range(1, n+1)]
        res = []
        self.func(nums, k, "", res)
        return res

    def func(self, nums, k, out, res):
        if not nums:
            res.append(out)
            return

        for i in range(len(nums)):
            self.func(nums[:i] + nums[i + 1:], k, out + str(nums[i]), res)
            if len(res) == k:
                break


# 通过计算阶乘，不断的取余
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        nums = [str(i) for i in range(0, n + 1)]
        if k == 1:
            return "".join(nums[1:])

        facts = self.factorial(n)
        if k == facts[n]:
            return "".join(nums[::-1][:-1])

        res = ""
        for i in range(1, n):
            fact = facts[n - i]
            a, b = divmod(k, fact)
            if b == 0:
                nums_a = nums[a]
                res += nums_a
                nums.pop(a)
                k = fact
            else:
                nums_a = nums[a+1]
                res += nums_a
                nums.pop(a + 1)
                k = b
        res = res + nums[-1]
        return res

    def factorial(self, n):
        res = 1
        facts = [1] * (n+1)
        for i in range(1, n + 1):
            res = res * i
            facts[i] = res
        return facts


S = Solution()
n = 3
k = 3
res = S.getPermutation(n, k)
print(res)
