"""
解题思路:
二进制加法的实现，末位进1.
首先将数字转成十进制的int来计算会有超大数据加减的问题，所以还是老老实实的用我们从小学到大的列竖式方法
"""


class Solution:
    def addBinary(self, a, b):
        total = []
        lena = len(a)
        lenb = len(b)
        up = 0
        for i in range(max(lena, lenb)):
            num1 = int(a[lena - i - 1]) if lena > i else 0
            num2 = int(b[lenb - i - 1]) if lenb > i else 0
            _sum = num1 + num2 + up
            up = 1 if _sum >= 2 else 0
            total.append(str(_sum % 2))
        if up:
            total.append('1')
        return ''.join(total[::-1])


if __name__ == '__main__':
    print(Solution().addBinary('1010', '1011'))

