"""
https://leetcode.com/problems/add-two-numbers/
"""

# Definition for singly-linked list.


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1, l2):
        dummy = ListNode(-1)
        cur = dummy
        n = 0
        while l1 or l2:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            n, res = divmod(val1 + val2 + n, 10)
            cur.next = ListNode(res)
            cur = cur.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        if n:
            cur.next = ListNode(n)
        return dummy.next


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
