"""
解题思路:
字符串相加也就是大数相加，因为整型的长度是有限制的，整型大小不超过2的32次方。而字符串理论上可以无限长
从我们从小到大的手算经验，两数相加，肯定是从个位向高位计算，有1进1
"""


class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        # 从尾部计算需倒置字符串
        num1 = num1[::-1]
        num2 = num2[::-1]

        len1 = len(num1)
        len2 = len(num2)
        _max = max(len1, len2)

        i = 0
        _sum = []
        # 是否需要进位
        up = False
        while i < _max:
            tem = 0
            if i < len1:
                tem += int(num1[i])
            if i < len2:
                tem += int(num2[i])
            if up:
                tem += 1
            _tem = tem - 10
            if _tem >= 0:
                up = 1
                _sum.append(str(_tem))
            else:
                up = 0
                _sum.append(str(tem))
            i += 1
        if up:
            _sum.append('1')
        return ''.join(_sum[::-1])


if __name__ == '__main__':
    sl = Solution()
    print(sl.addStrings('0', '0'))
