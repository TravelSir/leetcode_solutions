"""
解题思路:
第一个人不知道自己的票, 那可以拆解成三种情况:
1. 刚好坐到自己的位置   1/n的机率
2. 刚好坐到第n个人的位置  1/n的机率
3. 坐到除了自己和第n个人的位置  n-2/n的机率
那么第n个人坐到自己位置的机率就等于
1. 百分百坐到自己位置  1/n * 1
2. 百分百坐不到自己位置  1/n * 0
3. 因为有一个人坐不到自己的位置就会乱坐, 所以n坐到自己位置的概率等于在一个人乱坐的n-1个座位中坐到自己的位置 f(n-1)
那么当一个人乱坐时:
1.坐到n的位置 1/(n-1) * 0
2.坐到坐自己位置的人的位置上 1/(n-1) * 1
2.坐到另一个人的位置 ==> 变成了n在一个人乱坐的n-2个座位中坐到自己位置 f(n-2)
(n-3)/(n-1) * f(n-2)
会发现两种逻辑公式都是一样:
s(n) = 1/n + (n-2)/n * s(n-1)

这里有个隐藏坑:
公式用Fraction分数类型,不然会丢失精度,但n过大的时候Fraction计算就会很耗时
但如果是正常的计算概率肯定会在小数点后很多位丢失

但是这道题的数学逻辑避免了这种情况:
已知: s(1) = 1 s(2) = 0.5
那:s(3) = 1/3 + (3-2)/3 * s(2) = 1/3 + (3-1)/6 = (2+3-2) / 6 = 0.5
那其实假设s(n-1)为0.5
那么s(n) = 1/n + (n-2)/n * 0.5 = 2/2n + (n-2)/2n = (2+n-2)/2n = 1/2
所以正因为s(2) = 0.5
所以往上推的所有s(n)结果都会为0.5
其实优化动态规划后的数学解法就是:
n=1 时返回1.0
n>1 时返回0.5
"""


# 动态规划算法
class Solution:
    def nthPersonGetsNthSeat(self, n: int) -> float:
        if n <= 2:
            return 1/n
        fn = 0.5
        for i in range(3, n+1):
            fn = 1/i + (i-2)/i * fn
        return fn


if __name__ == '__main__':
    sl = Solution()
    print(sl.nthPersonGetsNthSeat(20000))
