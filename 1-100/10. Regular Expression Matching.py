# coding=utf-8
"""
解题思路：
首先我们分析模式串，用两个指针i, j分别指向字符串和模式串的尾部:
- 当j所指字符为除*外的字符
    - j所指字符与i所指匹配(两个字符相等或j所指字符为.且i不为空字符), 则两个指针都往左移一位
    - 不匹配，则为false
- 当j所指字符为*,因为*不能单用，所以需把j-1和j联合使用，会分叉出多种情况，只要有一种为true就为true
    - *使用0次，则直接舍弃j和j-1所指字符，j指针向左移动两位
    - *使用多次，则判断i所指字符与j-1所指字符是否匹配（这j不移动的原因，在于假如匹配成功了，等同与子问题使用*0次丢弃的情况）
        - 匹配，则i向左移动一位
        - 不匹配，则False


按照上面的思路实现动态规划的算法，从下到上的实现速度会快很多
那么我们用f(i,j)表示s的前i个字符和p中的前j个字符能否匹配。

f(i,j) = {
    {
        f(i-1, j-1),   match(s[i], p[j])
        false,         else
    },                 p[j] != '*'
    f(i, j-2) or ({
        f(i-1, j),     match(s[i], p[j-1])
        false,         else
    }),                p[j] == '*'
}

采用自下而上的实现方式，i从0开始，j从1开始，循环记录下前i个字符去匹配前j个字符的结果
首先f(0, 0) = True


"""


class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """

        def match(i: int, j: int) -> bool:
            if i == 0:
                return False
            if p[j-1] == '.' or s[i-1] == p[j-1]:
                return True
            return False

        m, n = len(s), len(p)

        note = [[False] * (n + 1) for _ in range(m + 1)]
        note[0][0] = True

        for i in range(m + 1):
            for j in range(1, n + 1):
                if p[j - 1] != '*':
                    if match(i, j):
                        note[i][j] = note[i-1][j-1]
                else:
                    note[i][j] = note[i][j-2] or (note[i-1][j] if match(i, j-1) else False)

        return note[m][n]


if __name__ == '__main__':
    s = "aaaaaaaaaaaaab"
    p = "a*a*a*a*a*a*a*a*a*a*b"
    print(Solution().isMatch(s, p))

