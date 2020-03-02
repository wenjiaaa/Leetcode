"""
https://leetcode.com/problems/partition-list/

Given a linked list and a value x, partition it such that all nodes less than x come before 
nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

Example:

Input: head = 1->4->3->2->5->2, x = 3
Output: 1->2->2->4->3->5

可用于链表快排，见148题

"""

# Definition for singly-linked list.


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def partition(self, head, x):
        small_head, big_head = ListNode(0), ListNode(0)
        small, big = small_head, big_head
        while head:
            if head.val < x:
                small.next = head
                small = small.next
            else:
                big.next = head
                big = big.next
            head = head.next
        big.next = None
        small.next = big_head.next
        return small_head.next


L = ListNode(1)
cur = L
for v in [4, 3, 2, 5, 2]:
    cur.next = ListNode(v)
    cur = cur.next
x = 3
S = Solution()
res = S.partition(L, x)
cur = res
while cur:
    print(cur.val)
    cur = cur.next
