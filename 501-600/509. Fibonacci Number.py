"""
解题思路:
动态规划启蒙之题
f(n) = f(n-1) + f(n-2) ...
斐波那契数列首先想到到就是递归，但有个问题就是会有很多重复计算。
这个时候我们可以用一个备忘录来记录已经计算好的结果。这种方法虽然避免了重复计算，但是增加了内存，且还是使用的递归，有调用栈溢出的问题
所以我们使用另一种更好的办法: 自底向上
f(2) = f(1) + f(0)
f(3) = f(2) + f(1)
那我们从2开始一直到n，使用循环，且每次只需要记录两个临时值即可

还有一种数学矩阵方法，不过不太常用
"""


class Solution:
    def fib(self, n: int) -> int:
        # note = [-1] * (n + 1)
        # return self.top_down(n, note)
        return self.down_top(n)

    def top_down(self, n: int, note: list) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        if note[n] != -1:
            return note[n]
        note[n] = self.top_down(n-1, note) + self.top_down(n-2, note)
        return note[n]

    @staticmethod
    def down_top(n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        left, right = 0, 1
        _sum = 1
        for i in range(2, n+1):
            _sum = left + right
            left, right = right, _sum
        return _sum


if __name__ == '__main__':
    print(Solution().fib(45))


