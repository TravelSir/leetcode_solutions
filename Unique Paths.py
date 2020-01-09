"""
解题思路:
因为机器人每次只能向下或向右移动，那么表示终点的前一步肯定是它的上方或左方，那么到终点的路径数就等于上方一个的路径数加左方一格的路径数
那么dp[m][n] = dp[m][n-1] + dp[m-1][n]
而当两个下标任意一个为1的时候，就代表机器人只能一直向右或一直向下到达目标点，那么此时的路径数就是肯定为1的
这题采用自定向下的备忘录方式实现简单一点
"""


class Solution:

    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0 for i in range(n)] for j in range(m)]
        return self.calculate(m-1, n-1, dp)

    def calculate(self, m, n, dp):
        if m == 0 or n == 0:
            dp[m][n] = 1
            return 1
        if dp[m][n]:
            return dp[m][n]
        dp[m][n] = self.calculate(m - 1, n, dp) + self.calculate(m, n-1, dp)
        return dp[m][n]


if __name__ == '__main__':
    print(Solution().uniquePaths(100, 100))
