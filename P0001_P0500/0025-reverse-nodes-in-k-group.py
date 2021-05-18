# https://leetcode-cn.com/problems/reverse-nodes-in-k-group/
from typing import List
# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        # 先定义一个伪头节点
        # 时间复杂度：O（n）,空间复杂度：O(1)
        hair = ListNode(0)
        hair.next = head
        pre = hair
        while head:
            tail = pre
            # 查看剩余部分长度是否大于等于 k
            for _ in range(k):
                tail = tail.next
                if not tail:
                    return hair.next
            nxt = tail.next
            head, tail = self.reverseList(head, tail)
            # 把翻转好的子链表与原链表拼起来
            pre.next = head
            tail.next = nxt
            pre = tail
            head = tail.next
        return hair.next

    def reverseList(self, head, tail):
        # 先把内部翻转: 翻转一个子链表，并且返回新的头与尾，参考LeetCode206
        prev = tail.next
        p = head
        while prev != tail:
            nxt = p.next
            p.next = prev
            prev = p
            p = nxt
        return tail, head
