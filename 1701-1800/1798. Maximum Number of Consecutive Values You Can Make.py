"""
解题思路:
这道题太有意思了。由于从最暴力的解题思路来看，由于求和的树是不限的，所以都不是两层循环的事了，甚至到了n层循环，根本无法找到优化的方向
所以还是要继续分析题目的特性。
假设我们已有一串长度为n的硬币组合，满足0到x的连续整数区间[0, x]。
这时候新增一个数y，那么可得到[y, x+y]的连续整数区间。 那么只要y <= x，那么两个区间就能合并起来成为[0,y]的区间
所以在每一次遍历都判断是否有小于等于x的未被选择的数，有则说明符合，无则直接返回

所以这里我们直接将数组排序后，其实就可以依次取数与x进行判断
"""
from typing import List


class Solution:
    def getMaximumConsecutive(self, coins: List[int]) -> int:
        coins.sort()
        x = 0
        for i in range(0, len(coins)):
            if coins[i] <= x + 1:
                x += coins[i]
            else:
                break
        return x + 1


if __name__ == '__main__':
    print(Solution().getMaximumConsecutive([3]))

