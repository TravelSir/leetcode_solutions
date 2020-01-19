"""
解题思路:
反转整数其实就是按位剥离再组成新的数，为了防止溢出，其实只需要在反转的最后一步判断一下
1. 新的数在乘10之前是否小于 INT_MAX // 10
2. 若新的数等于INT_MAX // 10, 其实就需要判断加的最后一位数是否小于6即可（负数则是5）
"""


class Solution:
    def reverse(self, x: int):
        res, flag = 0, False
        if x < 0:
            x = abs(x)
            flag = True

        while x >= 10:
            res = res * 10 + x % 10
            x //= 10

        int_max = (1 << 31) - 1
        if res > int_max // 10:
            return 0
        elif res == int_max // 10:
            if x > (8 if flag else 7):
                return 0
        return (res * 10 + x) * (-1 if flag else 1)


if __name__ == '__main__':
    print(Solution().reverse(-2147483412))
