# coding=utf-8
"""
    解题思路：
    由于不允许使用整数转换为字符串的形式。
    所以这里将x循环除以10，从个位开始拆出每一位，拆出的每一位数字会加在另一个数字s上，x每除一次10，s就乘10并加上x。
    这样当x拆完时，组合成的s就是x的颠倒整数，再判断就好了
"""


class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        tem = x
        s = 0
        while(tem > 0):
            s = s*10 + tem % 10
            tem //= 10
        if s == x:
            return True
        else:
            return False


if __name__ == '__main__':
    sl = Solution()
    print(sl.isPalindrome(1231321))
