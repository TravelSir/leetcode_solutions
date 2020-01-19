"""
解题思路:
这题跟反转整数一个思想，只不过多了些条件判断
首先找到第一个非空格字符，如果此字符不是'+'，'-'或数字，即返回0
然后第二个字符开始，必须是数字，如果不是数字则结束循环。
然后判断数大小和反转整数一样
1. 新的数在乘10之前是否小于 INT_MAX // 10
2. 若新的数等于INT_MAX // 10, 其实就需要判断加的最后一位数是否小于6即可（负数则是5）

这题还有一种解法其实利用了python的特性，因为python里整数大小是不受32位符号限制的，所以我们只需正则匹配出满足条件的11位以下整数，再和边界做比较即可
"""


class Solution:
    def myAtoi(self, str) -> int:
        int_max = (1 << 31) - 1
        first, res, flag = True, 0, True

        for s in str:
            if first:
                if s == ' ':
                    continue
                if s == '-':
                    flag = False
                elif s.isdigit():
                    res += int(s)
                elif s != '+':
                    break
                first = False
            elif s.isdigit():
                s = int(s)
                if abs(res) > int_max // 10:
                    res = int_max if flag else ((int_max * -1) - 1)
                    break
                elif abs(res) == int_max // 10:
                    if s > (7 if flag else 8):
                        res = int_max if flag else ((int_max * -1) - 1)
                        break
                if flag:
                    res = res * 10 + s
                else:
                    res = res * 10 - s
            else:
                break
        return res


if __name__ == '__main__':
    print(Solution().myAtoi("-91283472332"))
