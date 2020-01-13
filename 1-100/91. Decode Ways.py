"""
解题思路:
首先我们分析，字符串解码，可以一位一位的解码，也可以两位两位的解码（在满足两位数小于26时）
那么我们用动态规划的思维来看
从第一位开始，如果选择解一位，那么dp(n) = dp(n-1)
如果选择解两位，如果两位数大于26，则不能解，如果小于等于26，那么dp(n) = dp(n-2)
那么dp(n) = dp(n-1) + dp(n-2) if s[len(s) - n::2] <= 26 else 0
这里需要考虑一个特殊情况，就是当数字中间有0时，因为0不能单独被解码，所以需要联合他前面一位进行解码
所以当组成当两位数是两个0或大于20时，说明这个字符串不能被解码了
而两位数是10，20时，那说明dp(n)只能等于dp(n-2)，因为0不能作为单独的一位数来解码
"""


class Solution:
    def numDecodings(self, s: str) -> int:
        lens = len(s)
        if s[0] == '0':
            return 0
        if lens < 2:
            if s == '0':
                return 0
            else:
                return 1
        i = 0
        dp_l = dp_r = 1
        while lens > 1:
            _sum = int(s[i]) * 10 + int(s[i+1])
            if s[i+1] == '0':
                if _sum == 0 or _sum > 20:
                    return 0
                dp_r = dp_l
                lens -= 1
                i += 1
            elif s[i] == '0':
                return 0
            else:
                tem = dp_r
                dp_r = dp_r + (dp_l if int(s[i]) * 10 + int(s[i+1]) <= 26 else 0)
                dp_l = tem
            lens -= 1
            i += 1
        if s[-1] == '0' and s[-2] == '0':
            return 0
        return dp_r


if __name__ == '__main__':
    print(Solution().numDecodings('01'))
