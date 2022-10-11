"""
解题思路:仅仅执行一次交换，那么只要找出a字符串与b字符串不同的字符进行比较即可
因为交换可以同一字符交换（即不交换），这里可以先判断字符串是否相等，相等则直接返回True
当不同的字符大于两个时，则直接返回False。
"""


class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True
        dif = []
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                dif.append((s1[i], s2[i]))
            if len(dif) > 2:
                return False

        if len(dif) != 2:
            return False

        return dif[0][0] == dif[1][1] and dif[1][0] == dif[0][1]
