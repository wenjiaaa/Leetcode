
"""
https://leetcode.com/problems/validate-binary-tree-nodes/
You have n binary tree nodes numbered from 0 to n - 1 where node i has two children leftChild[i] and rightChild[i], 
return true if and only if all the given nodes form exactly one valid binary tree.

If node i has no left child then leftChild[i] will equal -1, similarly for the right child.

Note that the nodes have no values and that we only use the node numbers in this problem.


Example 1:
Input: n = 4, leftChild = [1,-1,3,-1], rightChild = [2,-1,-1,-1]
Output: true

Example 2:
Input: n = 4, leftChild = [1,-1,3,-1], rightChild = [2,3,-1,-1]
Output: false

Example 3:
Input: n = 2, leftChild = [1,0], rightChild = [-1,-1]
Output: false

Example 4:
Input: n = 6, leftChild = [1,-1,-1,4,-1,-1], rightChild = [2,-1,-1,5,-1,-1]
Output: false

思路：判断每个孩子节点是否有合理的唯一的父亲节点
"""


class Solution:
    def validateBinaryTreeNodes(self, n, leftChild, rightChild):
        D = {}
        for i, (left, right) in enumerate(zip(leftChild, rightChild)):
            if left != -1:
                if left in D or i > left:
                    return False
                else:
                    D[left] = i
            if right != -1:
                if right in D or i > right:
                    return False
                else:
                    D[right] = i
        if len(D) < n - 1:
            return False
        return True


S = Solution()
n = 4
leftChild = [1, -1, 3, -1]
rightChild = [2, 3, -1, -1]
res = S.validateBinaryTreeNodes(n, leftChild, rightChild)
print(res)
