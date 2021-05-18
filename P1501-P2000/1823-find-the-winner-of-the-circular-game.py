# https: // leetcode-cn.com/problems/find-the-winner-of-the-circular-game/
from typing import List


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        if k == 1:
            return n
        # 创建一个循环链表
        head = ListNode(1)
        cur = head
        for i in range(2, n + 1):
            p = ListNode(i)
            cur.next = p
            cur = cur.next
        cur.next = head
        nums = [i for i in range(1, n+1)]
        begin = head
        while (len(nums) != 1):
            p = begin
            for i in range(k-2):
                p = p.next
            tmp = p.next  # 被删除的那个
            p.next = tmp.next
            begin = tmp.next
            nums.remove(tmp.val)
        return nums[0]
