"""
https://leetcode.com/problems/palindrome-linked-list/

Given a singly linked list, determine if it is a palindrome.

Example 1:

Input: 1->2
Output: false
Example 2:

Input: 1->2->2->1
Output: true
"""
# Definition for singly-linked list.


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# 转换成列表，判断列表是否是回文
class Solution1:
    def isPalindrome(self, head):
        arr = []
        while head:
            arr.append(head.val)
            head = head.next
        return arr == arr[::-1]


# 反转列表
class Solution:
    def isPalindrome(self, head):
        if not head or not head.next:
            return True
        mid = self.reverse(self.findmid(head))
        while mid:
            if mid.val != head.val:
                return False
            head, mid = head.next, mid.next
        return True

    def findmid(self, head):
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow.next

    def reverse(self, head):
        left = None
        while head:
            right = head.next
            head.next = left
            left = head
            head = right
        return left


L = ListNode(1)
cur = L
for i in [2, 2, 2, 1]:
    cur.next = ListNode(i)
    cur = cur.next
S = Solution()
res = S.isPalindrome(L)
print(res)
