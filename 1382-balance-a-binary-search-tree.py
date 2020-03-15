"""
https://leetcode.com/problems/balance-a-binary-search-tree/

Given a binary search tree, return a balanced binary search tree with the same node values.

A binary search tree is balanced if and only if the depth of the two subtrees of every node never differ by more than 1.

If there is more than one answer, return any of them.

Example 1:
Input: root = [1,null,2,null,3,null,4,null,null]
Output: [2,1,3,null,null,null,4]
Explanation: This is not the only correct answer, [3,1,4,null,2,null,null] is also correct.

思路：首先对树进行中序遍历，找到中间的点作为新树的根节点，然后递归的遍历左右子树构建平衡二叉树
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def balanceBST(self, root):
        inorder = self.inorderTraversal(root)
        return self.build(inorder)

    def inorderTraversal(self, root):
        res, stack = [], []
        while root or stack:
            if root:
                stack.append(root)
                root = root.left
            else:
                root = stack.pop(-1)
                res.append(root)
                root = root.right
        return res

    def build(self, nodes):
        if not nodes:
            return
        mid = len(nodes) // 2
        mid_node = nodes[mid]
        mid_node.left = self.build(nodes[:mid])
        mid_node.right = self.build(nodes[mid + 1:])
        return mid_node
