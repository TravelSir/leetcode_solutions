"""
解题思路：
因为num的范围是在1到3999之间，且罗马数字也是从左到右按最高位数排列。
首先最简单的就是构建一个哈希表，建立单个罗马数字与十进制数对应的关系表。
其实有6种特殊情况。最直接的方法就是也放在哈希表中。
然后将num与罗马数字从大到小比较。
大于说明高位数能转为该罗马数减去该罗马数对应十进制数继续比较，小于则取小一位的罗马数字
"""


RomanNumDict = {
    1: 'I',
    4: 'IV',
    5: 'V',
    9: 'IX',
    10: 'X',
    40: 'XL',
    50: 'L',
    90: 'XC',
    100: 'C',
    400: 'CD',
    500: 'D',
    900: 'CM',
    1000: 'M'
}


class Solution:
    def intToRoman(self, num: int) -> str:
        result = list()
        roman_list = sorted(RomanNumDict.keys(), reverse=True)
        i = 0
        while num > 0:
            if num >= roman_list[i]:
                num -= roman_list[i]
                result.append(RomanNumDict[roman_list[i]])
            else:
                i += 1
        return ''.join(result)


if __name__ == '__main__':
    print(Solution().intToRoman(3999))

