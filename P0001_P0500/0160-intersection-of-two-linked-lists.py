# https://leetcode-cn.com/problems/intersection-of-two-linked-lists/

from typing import List
# Definition for singly-linked list.


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution1:
    # 方法一： 获取两个链表的长度差， 然后从相同的位置出发开始遍历
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        pA, pB = headA, headB
        lenA, lenB = 0, 0
        while(pA):
            lenA += 1
            pA = pA.next
        while(pB):
            lenB += 1
            pB = pB.next
        diff = abs(lenA - lenB)
        if lenA > lenB:
            for i in range(diff):
                headA = headA.next
        else:
            for i in range(diff):
                headB = headB.next
        while(headB and headB):
            if headA == headB:
                return headA
            headA = headA.next
            headB = headB.next
        return None


class Solution:
    # 方法二： 双指针，遍历一遍
    # 时间复杂度：O（m+n）, 空间复杂度：O（1）
    # 创建两个指针 pApA 和 pBpB，分别初始化为链表 A 和 B 的头结点。然后让它们向后逐结点遍历。
    # 当 pApA 到达链表的尾部时，将它重定位到链表 B 的头结点(你没看错，就是链表 B)
    # 类似的，当 pBpB 到达链表的尾部时，将它重定位到链表 A 的头结点。
    # 若在某一时刻 pApA 和 pBpB 相遇，则 pApA/pBpB 为相交结点。

    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if headA == None or headB == None:
            return None
        pA, pB = headA, headB
        while(pA != pB):
            if pA != None:
                pA = pA.next
            else:
                pA = headB
            if pB != None:
                pB = pB.next
            else:
                pB = headA
        # 若遍历到最后二者都没相交，那么pA = pB = None，因此返回其中一个即可
        return pA
