"""
解题思路:
又是一道回溯题，类似找单词但更简单。一样使用一个栈存储待进入的点，
这里再用一个大小为m*n的数组v来记录是否已访问该节点，节点在数组中的位置按照从左到右，从上到下排序，那么节点位置=x*n+y
用check函数判断是否能进入
"""


class Solution:
    def movingCount(self, m: int, n: int, k: int) -> int:
        v = [0] * m * n

        stack = [(0, 0)]
        while stack:
            x, y = stack.pop()

            if self.check(x, y, k) and not v[x*n+y]:
                v[x*n+y] = 1
                if x > 0 and not v[(x-1)*n+y]:
                    stack.append((x-1, y))
                if x < m - 1 and not v[(x+1)*n+y]:
                    stack.append((x+1, y))
                if y > 0 and not v[x*n+y-1]:
                    stack.append((x, y-1))
                if y < n - 1 and not v[x*n+y+1]:
                    stack.append((x, y+1))
        count = 0
        for i in v:
            if i == 1:
                count += 1

        return count

    @staticmethod
    def check(x, y, k):
        _sum = 0
        for i in (x, y):
            while i >= 10:
                _sum += i % 10
                i //= 10
            _sum += i
        return _sum <= k
