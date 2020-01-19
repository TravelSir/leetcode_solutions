"""
解题思路:
这种有规律，且需要对前面已计算出结果的值再进行计算的题，应该是要使用动态规划去做
在进行子问题计算时，这题有一种非常巧妙的算法，就是使用三指针
当从1开始时，这是取的是1乘以2，3，5中最小的积2作为第2个数
那取第三个数时，其实就是取1乘以2，3，5和2乘以2，3，5中的积最小的数。
但是在这里，因为2就是1乘以2以后的结果，所以1乘以2能产出的丑数顺序已经确定了，所以接下来只需要判断1乘以3，5的积就可以了
那么2乘以2，3，5，其实我们会发现，因为1还能乘以3，5产出丑数，那么2本身就比1大，那么2乘以3，5的结果肯定比1要大，那么其实只需要判断2乘以2的结果就行了
所以我们会发现，在确定下一个丑数时，我们只需要进行三次乘法比较，分别乘以2，3，5。而我们需要确定的就是每次谁和2相乘，谁和3相乘，谁和5相乘。
所以我们设置三个指针，分别指向2的乘数，3的乘数，5的乘数。最开始都指向第一个数1。
当三个指针乘法过后谁的积更小，那这个积就是下一个顺序的丑数，且对应的指针就向后移动一位
但这里有个特殊情况就是，有可能两个指针乘法过后的积都是最小的，那么这两个指针都应该往后
"""


class Solution:
    def nthUglyNumber(self, n: int) -> int:
        dp = [1]
        p2 = p3 = p5 = 0
        for i in range(1, n):
            _min = min(dp[p2] * 2, dp[p3] * 3, dp[p5] * 5)
            dp.append(_min)
            if dp[p2] * 2 == _min:
                p2 += 1
            if dp[p3] * 3 == _min:
                p3 += 1
            if dp[p5] * 5 == _min:
                p5 += 1
        return dp[n-1]


if __name__ == '__main__':
    sl = Solution()
    print(sl.nthUglyNumber(1600))