"""
https://leetcode.com/problems/count-submatrices-with-all-ones/

Given a rows * columns matrix mat of ones and zeros, return how many submatrices have all ones.

Example 1:

Input: mat = [[1,0,1],
              [1,1,0],
              [1,1,0]]
Output: 13
Explanation:
There are 6 rectangles of side 1x1.
There are 2 rectangles of side 1x2.
There are 3 rectangles of side 2x1.
There is 1 rectangle of side 2x2. 
There is 1 rectangle of side 3x1.
Total number of rectangles = 6 + 2 + 3 + 1 + 1 = 13.
Example 2:

Input: mat = [[0,1,1,0],
              [0,1,1,1],
              [1,1,1,0]]
Output: 24
Explanation:
There are 8 rectangles of side 1x1.
There are 5 rectangles of side 1x2.
There are 2 rectangles of side 1x3. 
There are 4 rectangles of side 2x1.
There are 2 rectangles of side 2x2. 
There are 2 rectangles of side 3x1. 
There is 1 rectangle of side 3x2. 
Total number of rectangles = 8 + 5 + 2 + 4 + 2 + 2 + 1 = 24.
Example 3:

Input: mat = [[1,1,1,1,1,1]]
Output: 21
Example 4:

Input: mat = [[1,0,1],[0,1,0],[1,0,1]]
Output: 5

"""


class Solution(object):
    def numSubmat(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """

        # 首先记录每一行连续的1的个数
        left = []

        max_width, max_hight = len(matrix[0]), len(matrix)
        for i in range(max_hight):
            left_line = []
            cnt = 0
            for j in range(max_width):
                if matrix[i][j]:
                    cnt += 1
                else:
                    cnt = 0
                left_line.append(cnt)
            left.append(left_line)

        # 以matrix[i][j]为矩阵的右下角，往上找可能的矩阵个数
        res = 0
        for i in range(max_hight):
            for j in range(max_width):
                if matrix[i][j] == 0:
                    continue
                n = max_width
                for k in range(i, -1, -1):
                    if matrix[k][j] == 0:
                        break
                    # 第k行到第i行，以matrix[i][j]作为右下角元素的个数
                    n = min(n, left[k][j])
                    res += n
        return res


S = Solution()
mat = [[0, 1, 1, 0],
       [0, 1, 1, 1],
       [1, 1, 1, 0]]
print(S.numSubmat(mat))
