"""
https://leetcode.com/problems/binary-tree-postorder-traversal/

Given a binary tree, return the postorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [3,2,1]

思路： 前序遍历：根左右， 后续遍历：左右根， 其实就是前序遍历反转一下，但是要注意左右顺序
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def postorderTraversal(self, root: TreeNode):
        res, L = [], []
        while root or L:
            if root:
                res.insert(0, root.val)
                L.append(root)
                root = root.right
            else:
                root = L.pop()
                root = root.left
        return res

# 递归写法


class Solution1:
    def postorderTraversal(self, root: TreeNode):
        res = []
        self.func(root, res)
        return res

    def func(self, root, arr):
        if not root:
            return
        self.func(root.left, arr)
        self.func(root.right, arr)
        arr.append(root.val)


cur = TreeNode(1)
cur.right = TreeNode(2)
cur.right.left = TreeNode(3)

S = Solution()
print(S.postorderTraversal(cur))
