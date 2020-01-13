"""
解题思路:
这题就简单升级了一下，还是用dp来做
因为机器人每次只能向下或向右移动，那么表示终点的前一步肯定是它的上方或左方，那么到终点的路径数就等于上方一个的路径数加左方一格的路径数
那么dp[m][n] = dp[m][n-1] + dp[m-1][n]
1.当遇到的坐标是障碍物时，dp[m][n]=0
2.dp[0][0] = 1
这题采用自顶向下的备忘录方式实现简单一点
"""


class Solution:

    def uniquePathsWithObstacles(self, obstacleGrid) -> int:
        if obstacleGrid[0][0] == 1:
            return 0
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = [[None for i in range(n)] for j in range(m)]
        return self.calculate(m-1, n-1, dp, obstacleGrid)

    def calculate(self, m, n, dp, obstacleGrid):
        if obstacleGrid[m][n] == 1:
            dp[m][n] = 0
            return 0
        if m == 0 and n == 0:
            return 1
        if m == 0:
            dp[m][n] = self.calculate(m, n-1, dp, obstacleGrid)
            return dp[m][n]
        if n == 0:
            dp[m][n] = self.calculate(m-1, n, dp, obstacleGrid)
            return dp[m][n]
        if dp[m][n] is not None:
            return dp[m][n]
        dp[m][n] = self.calculate(m - 1, n, dp, obstacleGrid) + self.calculate(m, n-1, dp, obstacleGrid)
        return dp[m][n]


if __name__ == '__main__':
    l = [[0,0],[1,1],[0,0]]
    print(Solution().uniquePathsWithObstacles(l))
