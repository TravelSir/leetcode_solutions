"""
动态规划经典题
跳第一阶只有一种跳法
dp(1) = 1
跳第二阶有两种，一种跳两次一步，一种跳两步
dp(2) = 2
跳第三阶，那就有111，12，21 三种，不难发现，111和21都是从第二阶跳过来，而12则是从第一阶跳过来
其实dp(3) = dp(2) + dp(1)
那其实就是一个斐波那契数列
"""


class Solution:
    def numWays(self, n: int) -> int:
        if n == 0:
            return 1
        if n == 1:
            return 1
        left, right = 1, 1
        _sum = 2
        for i in range(2, n+1):
            _sum = left + right
            _sum %= 1000000007
            left, right = right, _sum
        return _sum
