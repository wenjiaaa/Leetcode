"""
https://leetcode.com/problems/linked-list-cycle-ii/
Given a linked list, return the node where the cycle begins. If there is no cycle, return null.

To represent a cycle in the given linked list, we use an integer pos which represents 
the position (0-indexed) in the linked list where tail connects to. If pos is -1, 
then there is no cycle in the linked list.

Note: Do not modify the linked list.

Example 1:

Input: head = [3,2,0,-4], pos = 1
Output: tail connects to node index 1
Explanation: There is a cycle in the linked list, where tail connects to the second node.

Example 2:

Input: head = [1,2], pos = 0
Output: tail connects to node index 0
Explanation: There is a cycle in the linked list, where tail connects to the first node.
"""

# Definition for singly-linked list.


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if head == None or head.next == None:
            return
        first, second = head, head
        while second and second.next:
            first = first.next
            second = second.next.next
            if first == second:
                break

        if second and second.next:
            first = head
            while first != second:
                first = first.next
                second = second.next
            return first

        return None


L = ListNode(1)
S = Solution()
res = S.detectCycle(L)
print(res)
