"""
解题思路:
首先分析题的意思: 爱丽丝先手, 两个人以最佳状态参与游戏, 意思就是两个人都想赢
那怎么样才能赢呢, 因为N % x = 0, 那只要N还大于1, 那N就还能继续切割下去,那么其实想赢就是要尽量把N减到1
而每次N能减1或减自身的除数。其实f(n) = not all(f(n-1), f(n-除数1), f(n-除数2) ...)
相当于我们只要子问题有一个为False,让别人拿到False的结果，自己就能赢。
所以这是典型的动态规划,我们这里用自底向上的方式

最优解是数学问题: 转化成奇偶问题
奇数的约数必定是奇数, 所以奇数减约数必定是偶数
偶数的约数可能是奇数，也可能是偶数，那么偶数减约数既可能是约数也可能是偶数
当数字为1时, 输
数字为2时,赢
当你为偶数时，选择减成奇数，这样对手减完你就能继续得到偶数,那最后得到2的一定是你
所以其实就是偶数赢, 奇数输
"""
import math


class Solution:
    def divisorGame(self, N):
        if N == 1:
            return False
        fn = [False, True]
        for i in range(3, N+1):
            flag = True
            for j in range(1, math.ceil(i / 2)):
                if i % j == 0 and not fn[i-j-1]:
                    fn.append(True)
                    flag = False
                    break
            if flag:
                fn.append(False)
        return fn[-1]


if __name__ == '__main__':
    sl = Solution()
    print(sl.divisorGame(998))
    print(sl.divisorGame(30))

