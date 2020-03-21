"""
https://leetcode.com/problems/binary-tree-preorder-traversal/

Given a binary tree, return the preorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,2,3]
"""
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def preorderTraversal(self, root: TreeNode):
        res = []
        res = self.func(root, res)
        return res

    def func(self, root, arr):
        if not root:
            return
        arr.append(root.val)
        self.func(root.left, arr)
        self.func(root.right, arr)
        return arr

# 非递归写法


class Solution1:
    def preorderTraversal(self, root: TreeNode):
        res, L = [], []
        while root or L:
            if root:
                res.append(root.val)
                L.append(root)
                root = root.left

            else:
                root = L.pop()
                root = root.right
        return res


cur = TreeNode(1)
cur.right = TreeNode(2)
cur.right.left = TreeNode(3)

S = Solution1()
print(S.preorderTraversal(cur))
