"""
解题思路:
这题我们使用dp来做
假设第一刀切在i处，分成了i 和 n-i 两段，为了使这两段的乘积最大，所以我们能把问题拆成求i段和n-i段各自最大的乘积
那怎么能知道第一刀i切在哪最大呢，我们只能遍历每种切法，求最大值。
那么dp(n) = max(dp(i) * dp(n-i)), 其中0<i<=n/2, 这个算法的时间复杂度是O(n*n),空间复杂度是O(n)

这里有几个临界点是:
当绳子长度小于2时，无法剪，乘积=0
当绳子长度等于2时，必须剪，只能剪成1*1=1
当绳子长度等于3时，必须剪，剪成1*2=2最大

但当绳子长度大于3时，长度1，长度2，长度3的绳子作为剪过以后的另一段可以不用再剪，那保持它们本身的长度就是最大的
所以dp(1) = 1, dp(2) = 2, dp(3) = 3

这道题还有种贪婪算法解法，但需要数学能力
当绳子长度=4时，切成2*2=4最长
当绳子长度>=5时，我们要尽量多的切出长度为3的绳子，当剩下的绳子长度为4的时候，就停止不切了（其实等同于4切成2*2=4）
这种算法的时间复杂度时O(1)
"""


class Solution:
    def cuttingRope(self, n: int) -> int:
        if n < 2:
            return 0
        if n == 2:
            return 1
        if n == 3:
            return 2

        return self._greed(n)

    @staticmethod
    def _dp(n: int) -> int:
        dp = [0] * (n+1)
        dp[1] = 1
        dp[2] = 2
        dp[3] = 3

        for i in range(4, n+1):
            _max = 0
            for _i in range(1, i//2+1):
                if _max < dp[_i] * dp[i-_i]:
                    _max = dp[_i] * dp[i-_i]
            dp[i] = _max

        return dp[n]

    @staticmethod
    def _greed(n: int) -> int:
        num3 = n // 3

        # 说明剩下的长度为4时，不切了
        if n - num3*3 == 1:
            num3 -= 1

        res = (n - num3 * 3) if (n - num3 * 3) else 1
        for i in range(num3):
            res *= 3
            res %= 1000000007

        return res


if __name__ == '__main__':
    print(Solution().cuttingRope(6))

