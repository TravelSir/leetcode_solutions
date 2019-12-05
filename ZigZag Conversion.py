# coding=utf-8
"""
解题思路：
遍历一次str，初始化拥有n个空str的list中 同一行char存在list同一位置的str中，最后顺序相加list中的str即可
时间复杂度为O(3n),空间复杂度也为O(n)
利用flag来标记当前char的排列规则，排列规则就两种，一种向下，一种斜上。
"""


class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        str_list = [''] * numRows
        i = 0
        flag = 'down'
        if numRows < 2:
            return s
        for ch in s:
            str_list[i] += ch
            if flag == 'up':
                i -= 1
                if i + numRows == 0:
                    i = 0
                    flag = 'down'
            else:
                i += 1
                if i == numRows:
                    if numRows == 2:
                        i = 0
                    else:
                        i = -2
                        flag = 'up'
        res = ''
        for st in str_list:
            res += st
        return res


if __name__ == '__main__':
    sl = Solution()
    s = "ABC"
    numRows = 2
    print(sl.convert(s, numRows))

