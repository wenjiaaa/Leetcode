"""
https://leetcode.com/problems/remove-nth-node-from-end-of-list/

Given a linked list, remove the n-th node from the end of list and return its head.

Example:

Given linked list: 1->2->3->4->5, and n = 2.

After removing the second node from the end, the linked list becomes 1->2->3->5.
Note:

Given n will always be valid.

Follow up:

Could you do this in one pass?
"""

# Definition for singly-linked list.


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# 注意边界， 添加一个虚拟头结点
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        tmp = ListNode(0)
        tmp.next = head
        first = tmp
        second = tmp
        for i in range(n+1):
            first = first.next
        while(first != None):
            first = first.next
            second = second.next
        second.next = second.next.next
        return tmp.next


L = ListNode(1)
L.next = ListNode(2)

S = Solution()
n = 2
res = S.removeNthFromEnd(L, n)
while res:
    print(res.val)
    res = res.next
