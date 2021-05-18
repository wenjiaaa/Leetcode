from typing import List


class Solution:
    def minSideJumps(self, obstacles: List[int]) -> int:
        dp = [[999999] * len(obstacles) for _ in range(3)]
        # 初始化dp
        dp[0][0] = 1
        dp[1][0] = 0
        dp[2][0] = 1
        for j in range(1, len(obstacles)):
            if obstacles[j] != 1:
                dp[0][j] = dp[0][j - 1]
            if obstacles[j] != 2:
                dp[1][j] = dp[1][j - 1]
            if obstacles[j] != 3:
                dp[2][j] = dp[2][j - 1]
            if obstacles[j] != 1:
                dp[0][j] = min(dp[0][j], min(dp[1][j], dp[2][j]) + 1)
            if obstacles[j] != 2:
                dp[1][j] = min(dp[1][j], min(dp[0][j], dp[2][j]) + 1)
            if obstacles[j] != 3:
                dp[2][j] = min(dp[2][j], min(dp[1][j], dp[0][j]) + 1)

        return min(dp[0][-1], dp[1][-1], dp[2][-1])


# 采用DFS， 把obstacles数组改成二位的矩阵，有石头的地方标记为1
# 枚举到达最右侧的所有的路径，找到跳跃次数最小的路径
class Solution1:
    def minSideJumps(self, obstacles: List[int]) -> int:
        res = 999999
        mapp = [[0] * len(obstacles) for _ in range(3)]
        vis = [[0] * len(obstacles) for _ in range(3)]
        for i in range(len(obstacles)):
            if obstacles[i] != 0:
                mapp[obstacles[i] - 1][i] = 1
        Next = [[0, 1],  # 向右走1步
                [1, 0],  # 向上走1步
                [2, 0],  # 向上走2步
                [-1, 0],  # 向下走1步
                [-2, 0]]  # 向下走2步s

        def dfs(x, y, step):
            nonlocal res

            if (y == len(obstacles) - 1):
                # 到达终点时，更新结果
                res = min(step, res)
            for k in range(len(Next)):
                tx = x + Next[k][0]
                ty = y + Next[k][1]

                if ty >= len(obstacles) or tx < 0 or tx >= 3:
                    continue
                # 若是往右走，则跳跃次数不变
                if mapp[tx][ty] == 0 and vis[tx][ty] == 0 and k == 0:
                    vis[tx][ty] = 1
                    dfs(tx, ty, step)
                    vis[tx][ty] = 0
                    #ty += 1

                # 若是往下或往上走，跳跃次数加1
                elif mapp[tx][ty] == 0 and vis[tx][ty] == 0 and k != 0:
                    vis[tx][ty] = 1
                    dfs(tx, ty, step + 1)
                    vis[tx][ty] = 0
        vis[1][0] = 1
        dfs(1, 0, 0)

        return res


S = Solution1()
obstacles = [0, 1, 2, 3, 0]
print(S.minSideJumps(obstacles))
