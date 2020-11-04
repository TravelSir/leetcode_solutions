"""
解题思路:
首先先排序确定abc为顺序
因为只能移动a和c石子，且a石子永远只能在c石子左边，那么最后移动的组合有三种
abc，bac，acb
首先看最大次数，c能移动的最大次数根据这三种情况分别为
abc: c - b - 1
bac: c - b - 2
acb: c - b
而a的最大移动次数对应为
abc: b - a - 1
bac: b - a
acb: b - a + 1
那么其实a,c的最大移动次数就等于 c - a - 2

再来看最小次数
当ab相邻时，a不用动
当a b只相差2时，只需c动1次，c在哪都无所谓，结果肯定为1
当a b相差2以上时，a必动

"""


class Solution:
    def numMovesStones(self, a, b, c):
        # 先排个序
        array = [a, b, c]
        array.sort()
        a = array[0]
        b = array[1]
        c = array[2]

        _max = c - a - 2

        _min = 0
        if b - a == 2:
            return [1, _max]
        elif b - a > 2:
            _min += 1

        if c - b == 2:
            return [1, _max]
        elif c - b > 2:
            _min += 1
        return [_min, _max]


if __name__ == '__main__':
    print(Solution().numMovesStones(4, 5, 1))
