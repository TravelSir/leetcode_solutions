"""
解题思路:
将罗马数字转整数，其实就是将罗马数字按规则相加求和,
III = 1 + 1 + 1 = 3
LX = 50 + 10 = 60
那其实
1.这样得罗马数字就是从左往右每位相加即可，而且从左往右其实每个字符代表的数字大小是从大到小的。
但从特殊规则我们可以看出IV = 4, IX = 9, XL = 40.
那其实我们可以换算成IV = 5 - 1 = 4, IX = X - 1 =9
那结合1得出的结论
2.当左边的字符小于右边的字符所代表的数字大小时，应减去左边字符的大小
那其实我们转化成程序逻辑来理解就是:
循环字符串，有两个指针，分别指向第一个和第二个元素
判断左指针所指元素是否比右指针大, 如果大那说明没有特殊规则，则直接加左指针的值，然后左右指针组成的滑动窗口向后滑动一位
如果左指针所指元素比右指针小，那说明触发了特殊规则，这个时候应该加上右指针的值再减去左指针的值，滑动窗口向后滑动两位
最后当右指针空指后直接加上左指针的值结束，或者左右指针同时空指时就直接结束
"""


class Solution:
    def romanToInt(self, s):
        roman = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        length = len(s)
        left = 0
        total = 0
        while left < length-1:
            if roman[s[left]] < roman[s[left+1]]:
                total += roman[s[left+1]] - roman[s[left]]
                left += 2
            else:
                total += roman[s[left]]
                left += 1

        if left < length:
            total += roman[s[left]]
        return total


if __name__ == '__main__':
    print(Solution().romanToInt('III'))
