"""
1391. Check if There is a Valid Path in a Grid

https://leetcode.com/problems/check-if-there-is-a-valid-path-in-a-grid/

Given a m x n grid. Each cell of the grid represents a street. The street of grid[i][j] can be:
1 which means a street connecting the left cell and the right cell.
2 which means a street connecting the upper cell and the lower cell.
3 which means a street connecting the left cell and the lower cell.
4 which means a street connecting the right cell and the lower cell.
5 which means a street connecting the left cell and the upper cell.
6 which means a street connecting the right cell and the upper cell.

You will initially start at the street of the upper-left cell (0,0).
A valid path in the grid is a path which starts from the upper left cell (0,0)
and ends at the bottom-right cell (m - 1, n - 1). The path should only follow the streets.

Notice that you are not allowed to change any street.

Return true if there is a valid path in the grid or false otherwise.

Example 1:
Input: grid = [[2,4,3],[6,5,2]]
Output: true
Explanation: As shown you can start at cell (0, 0) and visit all the cells of the grid to reach (m - 1, n - 1).


Example 2:
Input: grid = [[1,2,1],[1,2,1]]
Output: false
Explanation: As shown you the street at cell (0, 0) is not connected with any street of any other cell
and you will get stuck at cell (0, 0)

思路： 模拟路径的走法 
参考了解答，还可以用DFS

"""

import numpy as np

direct = {
    1: ['left', 'right'],
    2: ['upper', 'lower'],
    3: ['left', 'lower'],
    4: ['right', 'lower'],
    5: ['left', 'upper'],
    6: ['upper', 'right']
}

# 上一步和下一步方向的连接关系
relations = {
    'right': 'left',
    'left': 'right',
    'upper': 'lower',
    'lower': 'upper'
}


class Solution_my:
    def hasValidPath(self, grid):
        grid = np.array(grid)
        if grid.shape == (1, 1):
            return True

        start = grid[0, 0]
        # 如果第一个是4的话，最开始有两种走法
        if start == 4:
            res1 = self.check(grid, first='right', second='lower')
            res2 = self.check(grid, first='lower', second='right')
            return res1 or res2
        return self.check(grid)

    def check(self, grid, first='right', second='lower'):

        start = grid[0, 0]
        now_direct_list = direct[start]
        if first in now_direct_list:
            now_direct = first
        elif second in now_direct_list:
            now_direct = second
        else:
            return False
        i, j = 0, 0
        m, n = len(grid), len(grid[0])
        while i < m and j < n and i >= 0 and j >= 0:
            if now_direct == 'right':
                j += 1
            elif now_direct == 'lower':
                i += 1
            elif now_direct == 'left':
                j -= 1
            else:
                i -= 1
            if i < 0 or i >= m or j < 0 or j >= n:
                return False

            next_direct_list = direct[grid[i, j]]
            if relations[now_direct] in next_direct_list:
                if i == m - 1 and j == n - 1:
                    return True
                now_direct = next_direct_list[0] if next_direct_list[1] == relations[now_direct] else next_direct_list[1]
            else:
                return False


# DFS
class Solution:
    def hasValidPath(self, grid):
        if not grid:
            return True
        directions = {1: [(0, -1), (0, 1)],
                      2: [(-1, 0), (1, 0)],
                      3: [(0, -1), (1, 0)],
                      4: [(0, 1), (1, 0)],
                      5: [(0, -1), (-1, 0)],
                      6: [(0, 1), (-1, 0)]}
        visited = set()
        goal = (len(grid)-1, len(grid[0]) - 1)

        def dfs(i, j):
            visited.add((i, j))
            if (i, j) == goal:
                return True
            for d in directions[grid[i][j]]:
                ni, nj = i+d[0], j+d[1]
                if 0 <= ni < len(grid) and 0 <= nj < len(grid[0]) and (ni, nj) not in visited and (-d[0], -d[1]) in directions[grid[ni][nj]]:
                    if dfs(ni, nj):
                        return True
            return False
        return dfs(0, 0)


grid = [[2], [2], [2], [2], [2], [2], [6]]
S = Solution()
print(S.hasValidPath(grid))
