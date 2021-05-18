# https://leetcode-cn.com/problems/swap-nodes-in-pairs/
from typing import List
# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution1:
    # 方法一：递归
    # 时间复杂度：O(n)，空间复杂度：O(n)
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        newhead = head.next
        head.next = self.swapPairs(newhead.next)
        newhead.next = head
        return newhead


class Solution:
    # 方法二：迭代
    # 时间复杂度：O(n)，空间复杂度：O(1)
    def swapPairs(self, head: ListNode) -> ListNode:
        dummyHead = ListNode(0)
        dummyHead.next = head
        temp = dummyHead
        while(temp.next and temp.next.next):
            node1 = temp.next
            node2 = temp.next.next
            temp.next = node2
            node1.next = node2.next
            node2.next = node1
            temp = node1
        return dummyHead.next


test = ListNode()
head = test
for i in range(1, 5):
    node = ListNode(i)
    head.next = node
    head = head.next
S = Solution()
new_list = S.swapPairs(test)
newhead = new_list
while(newhead):
    print(newhead.val)
    newhead = newhead.next
