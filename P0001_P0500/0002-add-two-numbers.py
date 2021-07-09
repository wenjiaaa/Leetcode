"""
https://leetcode.com/problems/add-two-numbers/
"""

# Definition for singly-linked list.


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode(0)
        raw_head = head
        carry = 0
        while l1 or l2:
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0
            sumv = x + y + carry
            carry = sumv // 10
            head.next = ListNode(sumv % 10)
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
            head = head.next
        if carry != 0:
            head.next = ListNode(1)
        return raw_head.next


# test
l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)
l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

S = Solution()
cur = S.addTwoNumbers(l1, l2)
while cur:
    print(cur.val)
    cur = cur.next
