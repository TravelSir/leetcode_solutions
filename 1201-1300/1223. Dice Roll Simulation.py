"""
解题思路:
这题是一道典型的动态规划题，因为第二次的结果会基于第一次掷骰的结果。
假设投掷3次，总排列为6 * 6 * 6， 假设不允许1连续出现2次，其他的都可连续出现大于3次
那么，首先第一次投掷，总排列数为6，连续出现1的次数为1，连续出现1的次数为0
第二次投掷，总排列数为 6 * 6, 连续出现1的次数为1的有1*6-1, 连续出现1的次数为2的有1，此时排除(1，1)
第三次投掷，总排列数为 (6 * 6 - 1) * 6, 连续出现1的次数为1的为(6*6-1)-((1*6-1)*1), 连续出现1的次数为2的有1*(6-1)*1

由此可得, n次掷骰连续出现1的次数为
dp1(n, k) = f(n-1) - dp1(n-1, k-1) - ... dp1(n-k, 1)
其中f(n-1)指上次掷骰总排列数，k为连续出现1的最大次数限制. 可知dp1(1, 1) = 1, dp1(2,1) = f(1) - dp(1,1), dp1(3,1) = f(2) - dp(2,1) - dp(1,1)
六个限制都要依次判断。所以这题还比较负责，需要一个6*n的空间来记录已连续掷骰子的记录
"""
from typing import List


class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        roll_note = [
            [0] * (m + 1)
            for m in rollMax
        ]
        for r in roll_note:
            r[0] = 1
        f = 6
        for i in range(n - 1):
            _f = f * 6
            for r in roll_note:
                _sum = 0
                for j in range(len(r)-1, 0, -1):
                    r[j] = r[j-1]
                    _sum += r[j]
                r[0] = f - _sum
                _f -= r[-1]
            f = _f
            print(roll_note, f)
        return f % 1000000007


if __name__ == '__main__':
    rollMax = [2, 1, 4, 4, 1, 1]
    print(Solution().dieSimulator(5, rollMax))
