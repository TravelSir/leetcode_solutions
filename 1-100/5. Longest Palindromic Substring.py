"""
解题思路:
回文串的特点是倒过来是一致的，其实就是以中点为中心相互对称。
那当a是回文串时，在回文串的左右新加一个字符都相等的话那新的字符串也是回文串， 例如bab也是回文串，那这样我们就能确定所有奇数回文串
当两个字符组成的字符串aa是回文串时，也是在首位加一个字符，这样就能确定所有偶数回文串
我们用动态规划的思想来表示就是:
初始为
dp[i][i] = True,  这表示单个字符都是回文字符串
dp[i][i+1] = True if s[i] == s[i+1] else False,  如果相邻的两个字符相同，那就这两个字符组成的字符串就是回文字符串
则
dp[i][j] = True if dp[i+1][j-1] is True and s[i]==s[j] else False
此算法的时间复杂度为O(n*n)

但对于求最长子回文串，有一个时间复杂度为O(n)的算法Manager(马拉车)算法

"""


class Solution:
    def longestPalindrome(self, s: str) -> str:
        lens = len(s)
        if lens < 2:
            return s
        # 初始化dp
        dp = list()

        left, right = 0, 0
        for i in range(lens):
            _dp = [0] * lens
            _dp[i] = True
            dp.append(_dp)
        for i in range(lens-1):
            if s[i] == s[i + 1]:
                dp[i][i+1] = True
                left, right = i, i+1
            else:
                dp[i][i + 1] = False

        for k in range(lens):
            i, j = self.center_expand(k, k, dp, s)
            if j - i > right - left:
                left, right = i, j
            if k > 1:
                i, j = self.center_expand(k-1, k, dp, s)
                if j - i > right - left:
                    left, right = i, j

        return s[left: right+1]

    # 中心扩展
    @staticmethod
    def center_expand(i, j, dp, s):
        lens = len(s)
        flag = False
        while i > 0 and j < lens-1:
            if dp[i-1][j+1] == 0:
                dp[i-1][j+1] = True if (dp[i][j] is True and s[i-1] == s[j+1]) else False

            if dp[i-1][j+1] is False:
                break
            else:
                flag = True
            i -= 1
            j += 1
        if flag:
            return i, j
        else:
            return 0, 0


if __name__ == '__main__':
    print(Solution().longestPalindrome('cadcc'))
