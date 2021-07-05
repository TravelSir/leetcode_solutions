"""
解题思路:
一道典型的动态规划题
丢1次: 肯定有6种结果
丢2次: 上一次的结果*6 - 不能连续丢2次的结果
丢3次: 上一次丢结果*6 - 不能连续丢2次的结果 - 不能连续丢3次的结果
以此类推
那其实上一次的结果*6很好计算,但不能连续丢2次的结果和不能连续丢3次的结果怎么算呢
不能连续丢2次的结果就是上一次连续丢1次的结果
假设dp[i][n][m], 其中 1 <= m <= 6, m表示骰子点数,n表示连续几次,i表示第几轮, 最后的结果就是出现的次数
f[n][i] = dp[i][n-1][1] + dp[i][n-1][2] + ... + dp[i][n-1][6], f[n][i]表示丢i次 不能连续丢n次的结果
那么s[i] = s[i-1] * 6 - f[1][i] - f[2][i] - ... - f[3][i] 表示丢n次的不同点数序列数
其中 n = rollMax[m-1], s[1] = 6
且未满2次也就是只丢1次, 那肯定f[2][1] 到 f[6][1] 都是0, 未满3次则f[3][2] 到 f[6][2] 都是0，以此类推
且若骰数1被限制只能扔1次，则不能连续扔3次，4次的结果肯定是0
例如:
    假设rollMax = [1,1,1,1,1,1], 那么 dp[1][1][1] = 1, 表示丢1次，骰子1连续出现1次的次数为1, 以此类推dp[1][1][2]..., 而s[1] = 6 表示丢1次的不同点数序列数（其实第一次的结果都是固定的）
    那么dp[2][1][1] = s[1] - dp[1][1][1] = 5, f[2][2] = d[1][1][1] + ... + d[1][1][6] = 6, s[2] = s[1] * 6 - f[2][2] = 30
    那么dp[3][1][1] = s[2] - dp[2][1][1] = 25, f[2][2] = d[2][1][1] + ... +d[2][1][6] = 30, s[3] = s[2] * 6  = 150

"""
import math


class Solution:
    def dieSimulator(self, n, rollMax):
        s = 6
        dp = [[[0 for i in range(6)] for j in range(15)] for i in range(15)]
        for index, i in enumerate(rollMax):
            dp[i-1][i-1][index] = 1
        f = [0 for i in range(15)]
        mod = math.pow(10, 9) + 7
        for i in range(1, n):
            for k in range(min(n, max(rollMax))):
                tem = 0
                for j in range(6):
                    # if rollMax[j] <= k+1:
                    tem += dp[i-1][k][j]
                    if dp[i-1][k][j]:
                        dp[i][k][j] = s - dp[i-1][k][j]
                    # else:
                        # tem += 0
                f[k] = tem

            s = s * 6 - sum(f)

        return int(s % mod)


if __name__ == '__main__':
    sl = Solution()
    n = 4
    rollMax = [1, 1, 2, 2, 2, 3]
    print(sl.dieSimulator(n, rollMax))

