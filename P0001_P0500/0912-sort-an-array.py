# https://leetcode-cn.com/problems/sort-an-array/
from typing import List

# 冒泡排序，直接选择排序，直接插入排序，快速排序，归并排序，堆排序，希尔排序


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        self.quicksort(nums, 0, len(nums)-1)
        return nums

    def bubble_sort(self, nums):
        # 冒泡排序
        # 时间复杂度：O(N^2)，空间复杂度：O（1）
        n = len(nums)
        for i in range(n):
            flag = False
            for j in range(1, n - i):
                # 大的沉下去，小的浮上来。如果相邻两个数相等，不会发生交换，所以是稳定排序
                if nums[j - 1] > nums[j]:
                    nums[j], nums[j-1] = nums[j-1], nums[j]
                    flag = True
            # 如果某一轮已经没有交换了，那就退出
            if flag == False:
                break
        return nums

    def select_sort(self, nums):
        # 直接选择排序：每次选择最小的元素
        # 时间复杂度：O(N^2)，空间复杂度：O（1）
        n = len(nums)
        for i in range(n):
            min_num = nums[i]
            min_idx = i
            for idx in range(i+1, n):
                num = nums[idx]
                if num < min_num:
                    min_num = num
                    min_idx = idx
            # 第i个元素可能会排到相等元素之后，造成排序的不稳定
            nums[i], nums[min_idx] = nums[min_idx], nums[i]
        return nums

    def insert_sort(self, nums):
        # 直接插入排序
        n = len(nums)
        for i in range(n):
            # 将nums[i]插入到nums[0:i]中合适的位置
            v = nums[i]
            j = i - 1
            while j >= 0:
                # 从后往前看，若nums[j]大于v，则往后赋值
                if nums[j] > v:
                    nums[j + 1] = nums[j]
                else:
                    break
                j -= 1
            nums[j+1] = v
        return nums

    def patition(self, nums, left, right):
        tmp = nums[left]
        i, j = left, right
        # 如果有两个相同的数，快排的交换可能改变其顺序，因此不稳定
        while(i < j):
            while(i < j and nums[j] >= tmp):
                j -= 1
            if i < j:
                nums[i] = nums[j]
                i += 1
            while(i < j and nums[i] <= tmp):
                i += 1
            if i < j:
                nums[j] = nums[i]
                j -= 1
        nums[i] = tmp
        return i

    def quicksort(self, nums, left, right):
        # 快速排序
        # 时间复杂度：O(N*log(N))，当数组基本有序时，时间复杂度最坏为O（N^2）,空间复杂度：O（1）
        if left > right:
            return
        k = self.patition(nums, left, right)
        self.quicksort(nums, left, k - 1)
        self.quicksort(nums, k + 1, right)

    def merge_sort(self, nums, left, right):
        # 归并排序
        # 时间复杂度：O(N*log(N))，空间复杂度：O（N）
        # 稳定排序
        if (left < right):
            mid = (left + right) // 2
            self.merge_sort(nums, left, mid)
            self.merge_sort(nums, mid + 1, right)
            self.merge(nums, left, right, mid)

    def merge(self, nums, left, right, mid):
        # 归并两个有序数组
        tmp = []
        i, j = left, mid + 1
        while i <= mid and j <= right:
            if nums[i] < nums[j]:
                tmp.append(nums[i])
                i += 1
            else:
                tmp.append(nums[j])
                j += 1
        # 比较完可能还有剩下的，直接添加进去
        while (i <= mid):
            tmp.append(nums[i])
            i += 1
        while (j <= right):
            tmp.append(nums[j])
            j += 1
        # 更新原数组
        nums[left:right + 1] = tmp

    def heap_sort(self, nums):
        # 堆排序
        # 不稳定
        # 时间复杂度：O(N*log(N))，空间复杂度：O（1）
        length = len(nums)
        for i in range(length // 2):
            self.heap_adjust(nums, i, len(nums))
        # 每次把最大堆的堆顶元素拿出来，放到最后一个位置i，然后再调整堆
        for i in range(len(nums) - 1, 0, -1):
            nums[0], nums[i] = nums[i], nums[0]
            self.heap_adjust(nums, 0, i)

    def heap_adjust(self, nums, i, length):
        # 递归调整堆
        lc = i * 2 + 1  # 左孩子节点
        rc = i * 2 + 2  # 右孩子节点
        maxidx = i
        if (lc < length and nums[lc] > nums[maxidx]):
            maxidx = lc
        if (rc < length and nums[rc] > nums[maxidx]):
            maxidx = rc
        # 交换，并且递归调整堆
        if maxidx != i:
            nums[maxidx], nums[i] = nums[i], nums[maxidx]
            self.heap_adjust(nums, maxidx, length)

    def shell_sort(self, nums):
        # 希尔排序
        # 由于分组的存在，若两个相同的元素被分在了不同的组，则有可能交换顺序，因此不稳定
        # 时间复杂度：最好O（N），最坏O（N^2）,空间复杂度O（1）
        length = len(nums)
        # 希尔排序的gap，逐渐除以2
        d = length//2
        while d >= 1:
            # 进行gap为d的直接插入排序
            for i in range(d, length):
                v = nums[i]
                j = i - d
                while (j >= 0):
                    if nums[j] > v:
                        nums[j + d] = nums[j]
                    else:
                        break
                    j -= d
                nums[j + d] = v

            d = d // 2
        return nums


S = Solution()
nums = [5, 1, 1, 2, 0, 0]

# S.bubble_sort(nums)
# S.select_sort(nums)
# S.insert_sort(nums)
# S.quicksort(nums, 0, len(nums) - 1)
# S.merge_sort(nums, 0, len(nums) - 1)
# S.heap_sort(nums)
S.shell_sort(nums)

print(nums)
