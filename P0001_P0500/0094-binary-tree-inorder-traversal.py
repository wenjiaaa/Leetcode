"""
https://leetcode.com/problems/binary-tree-inorder-traversal/

Given a binary tree, return the inorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,3,2]
"""
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def inorderTraversal(self, root):
        res = []
        self.func(root, res)
        return res

    def func(self, root, arr):
        if (not root):
            return
        self.func(root.left, arr)
        arr.append(root.val)
        self.func(root.right, arr)


# 非递归写法
class Solution1:
    def inorderTraversal(self, root):
        res, L = [], []
        while root or L:
            if root:
                L.append(root)
                root = root.left
            else:
                root = L.pop()
                res.append(root.val)
                root = root.right
        return res


cur = TreeNode(1)
cur.right = TreeNode(2)
cur.right.left = TreeNode(3)

S = Solution1()
print(S.inorderTraversal(cur))
