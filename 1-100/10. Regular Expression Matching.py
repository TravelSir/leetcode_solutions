# coding=utf-8
"""
解题思路：
首先我们分析模式串，用两个指针分别指向模式串和字符串的头部:
- 1.1当模式串字符为除.*外的普通字符
    - 2.1后面是*:
        - 3.1模式串跳过字符和*, 因为*可以为0次,走1.1或1.2
        - 3.2匹配一次字符
            - 4.1如果没匹配到，则直接走3.1
            - 4.2匹配到了,则继续分别走3.1和3.2
    - 2.2后面不是*: 一一匹配
- 1.2当模式串字符为.(*不能单用)
    - 2.3后面是*:
        - 3.3模式串跳过.*，因为*可以为0次，走1.1或1.2
        - 3.4字符串右移一位,继续分别走3.3或3.4
    - 2.4后面不是*: 因为.可以匹配空字符
        - 3.5模式串移动1位
        - 3.6模式串和字符串都右移

最后判断模式串和字符串的指针最后是否都还停留在原串内。未停留则标识匹配成功，直接返回True

按照上面的思路实现动态规划的算法:
假设i为s要匹配的后i位字符，j为模式串p用于匹配的后j位字符
ls为s长度， lp为p长度

f(i,j) = {
    false,  当j==0 and i >0
    true,  当j==0 and i==0
    {
        false, 当j==1 or p[lp-j+1] != '*'
        f(i, j-2), 当p[lp-j+1] == '*'
    }, 当i==0
    {
        f(i-1, j-1),  当p[lp-j+1] != '*' or j==2
        f(i-1, j-2) or f(i-1, j), 当[lp-j+1] == '*'
    }, 当s[ls-i] == p[lp-j]
    {
        {
            false,   当p[lp-j+1] !='*' or j==2
            f(i, j-2),  当[lp-j+1] == '*'
        },  当p[lp-j] != '.'
        {
            f(i-1, j-1),  当p[lp-j+1] != '*' or j==1
            f(i-1, j-2) or f(i-1, j) or f(i, j-2),  当p[lp-j+1] == '*'
        },  当p[lp-j] == '.'
    }, 当s[ls-i] != p[lp-j] or i == 0
}



"""
from typing import List, Any


class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """

        ls = len(s)
        lp = len(p)

        note = [[0 for i in range(lp+1)] for j in range(ls+1)]
        return self.dp(ls, lp, s, p, note)

    def dp(self, i: int, j: int, s: str, p: str, note: List[List[Any]]) -> bool:
        if note[i][j] != 0:
            return note[i][j]

        ls = len(s)
        lp = len(p)
        if j == 0 and i == 0:
            note[i][j] = True
        elif j == 0:
            note[i][j] = False
        elif i == 0:
            if j == 1 or p[lp-j+1] != '*':
                note[i][j] = False
            else:
                note[i][j] = self.dp(i, j-2, s, p, note)
        elif s[ls-i] != p[lp-j]:
            if p[lp-j] == '.':
                if j == 1 or p[lp-j+1] != '*':
                    note[i][j] = self.dp(i-1, j-1, s, p, note)
                else:
                    note[i][j] = self.dp(i-1, 0 if j == 1 else j-2, s, p, note) or self.dp(i-1, j, s, p, note) or (False if j==1 else self.dp(i, j-2, s, p, note))
            else:
                if j == 1 or p[lp-j+1] != '*':
                    note[i][j] = False
                else:
                    note[i][j] = self.dp(i, 0 if j == 1 else j-2, s, p, note)
        else:
            if j == 1 or p[lp-j+1] != '*':
                note[i][j] = self.dp(i-1, j-1, s, p, note)
            else:
                note[i][j] = self.dp(i-1, 0 if j == 1 else j-2, s, p, note) or self.dp(i-1, j, s, p, note) or (False if j==1 else self.dp(i, j-2, s, p, note))

        return note[i][j]


if __name__ == '__main__':
    s = "ab"
    p = ".*.."
    print(Solution().isMatch(s, p))

