"""
解题思路:
找规律: 从1到n的方法数为: 1, 2, 3, 5, 8, 13 ...
这不就是 斐波那契数列吗
那就是道典型的动态规划题
这里使用备忘录法，用空间换时间
斐波那契数列的解法很多，最简单快速的其实是代公式,但是用公式在量级过大时会有误差，但其实量级过大时其他算法内存都撑不住了
"""


class Solution:
    def climbStairs(self, n: int) -> int:
        return self.fibonacci(n, [1, 2])

    def fibonacci(self, n, tem):
        if n <= len(tem):
            return tem[n-1]
        tem.append(self.fibonacci(n-1, tem) + self.fibonacci(n-2, tem))
        return tem[-1]


if __name__ == '__main__':
    sl = Solution()
    print(sl.climbStairs(35))
