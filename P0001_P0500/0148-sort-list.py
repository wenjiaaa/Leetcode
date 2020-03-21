"""
https://leetcode.com/problems/sort-list/

Sort a linked list in O(n log n) time using constant space complexity.

Example 1:

Input: 4->2->1->3
Output: 1->2->3->4
Example 2:

Input: -1->5->3->4->0
Output: -1->0->3->4->5

链表的归并排序和快速排序
"""

# Definition for singly-linked list.


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# 归并排序
class Solution:
    def sortList(self, head):
        if not head or not head.next:
            return head

        # 用快慢指针找出中间结点
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        fast = slow.next
        slow.next = None
        left = self.sortList(head)
        right = self.sortList(fast)
        return self.merge(left, right)

    def merge(self, left, right):
        p = newhead = ListNode(-1)
        while left and right:
            if left.val < right.val:
                p.next = left
                left = left.next
            else:
                p.next = right
                right = right.next
            p = p.next
        p.next = left or right
        return newhead.next


# 快速排序
class Solution1(object):
    def sortList(self, head):
        if not head:
            return head
        self.quicksort(head, None)
        return head

    def partion(self, begin, end):
        # 找分隔点
        key = begin.val
        slow = begin
        fast = begin.next
        while (fast != end):
            if (fast.val < key):
                slow = slow.next
                slow.val, fast.val = fast.val, slow.val  # 交换值
            fast = fast.next
        slow.val, begin.val = begin.val, slow.val
        return slow

    def quicksort(self, begin, end):
        if begin != end:
            p = self.partion(begin, end)
            self.quicksort(begin, p)
            self.quicksort(p.next, end)


L = ListNode(4)
cur = L
for i in [5, 6, 7]:
    cur.next = ListNode(i)
    cur = cur.next
S = Solution1()
res = S.sortList(L)
cur = res
while cur:
    print(cur.val)
    cur = cur.next
