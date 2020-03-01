"""
https://leetcode.com/problems/next-permutation/

Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

The replacement must be in-place and use only constant extra memory.

Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.

1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1

STL next_permutation剖析:
Find the largest index k such that a[k] < a[k + 1]. If no such index exists, the permutation is the last permutation.
Find the largest index l such that a[k] < a[l]. Since k+1 is such an index, l is well defined and satisfies k < l.
Swap a[k] with a[l].
Reverse the sequence from a[k+1] up to and including the last element a[n].
第一步找出一个k，使得k之后的为递减序列。（k之后的就没有全排列的结果了。想一下4321这种，都是逆序的）

接下来，我们需要找到一个最大的下标L使得 a[k]<a[L]，交换a[k]和a[L] （就是说递减序列中比a[k]大的最小的元素， 这样和位置k的进行交换，位置k之后的就又有全排列了）

最后对k+1之后的逆置即可（在纸上试试），这样就变成了升序。

eg: 1 4 3  2  k=0 L=3  swap-> 2431 逆置-> 2134
 
"""


class Solution:
    def nextPermutation(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        i = len(nums) - 2
        while i >= 0:
            if nums[i] < nums[i + 1]:
                break
            i -= 1

        if i < 0:
            return nums.sort()
        j = len(nums) - 1
        while i < j:
            if nums[i] < nums[j]:
                break
            j -= 1

        nums[i], nums[j] = nums[j], nums[i]
        nums[i + 1:] = nums[i + 1:][::-1]

        return nums


S = Solution()
nums = [4, 3, 2, 1]
S.nextPermutation(nums)
print(nums)
