"""
解题思路:
这题采用自底向上的动态规划会节约空间，我们利用数组本身的空间来存储计算的结果
因为机器人每次只能向下或向右移动，
grid[m][n] = min(grid[m][n+1], grid[m+1][n]) + grid[m][n]

"""




class Solution:

    def minPathSum(self, grid) -> int:
        m = len(grid)
        n = len(grid[0])
        dp = [[None for i in range(n)] for j in range(m)]
        return self.calculate(m-1, n-1, dp, grid)

    def calculate(self, m, n, dp, grid):
        if m == 0 and n == 0:
            return grid[m][n]
        if m == 0:
            dp[m][n] = self.calculate(m, n-1, dp, grid) + grid[m][n]
            return dp[m][n]
        if n == 0:
            dp[m][n] = self.calculate(m-1, n, dp, grid) + grid[m][n]
            return dp[m][n]
        if dp[m][n] is not None:
            return dp[m][n]
        dp[m][n] = min(self.calculate(m - 1, n, dp, grid) + grid[m][n], self.calculate(m, n-1, dp, grid) + grid[m][n])
        return dp[m][n]


if __name__ == '__main__':
    l = [
        [1, 3, 1],
        [1, 5, 1],
        [4, 2, 1]
    ]
    print(Solution().minPathSum(l))
