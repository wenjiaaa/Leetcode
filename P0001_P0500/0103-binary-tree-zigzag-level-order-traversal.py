# https://leetcode-cn.com/problems/binary-tree-zigzag-level-order-traversal/
from typing import List
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        queue = [root]
        res = []
        layer = 1
        while len(queue) != 0:
            tmp = []
            for i in range(len(queue)):
                cur = queue.pop(0)
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
                if layer % 2 == 0:
                    tmp.insert(0, cur.val)
                else:
                    tmp.append(cur.val)
            res.append(tmp)
            layer += 1
        return res
