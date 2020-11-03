# coding:utf-8
"""
解题思路：
首先循环将字符串拆成a,b两部分，a长度从1到总长度-1，b长度从总长度-1到1
然后再分别循环对a，b做小数点的每个位置的添加，判断添加小数点后数字的有效性，有效就放进一个临时列表
如果循环结束后a,b的临时列表有任意一个为空列表，则代表此次字符串分割无效，则countine
如果列表都不为空，则将两个列表循环拼接出一个长度为len(lista)*len(listb)的列表加入总结果列表中

判断数字是否有效:
1.首先添加小数点时不能添加到字符串第一位和最后一位
2.如果第一位是0且长度大于1,则0后必须跟小数点
3.如果最后一位是0且长度大于1,则整个数字都不能出现小数点
"""


class Solution:

    def ambiguousCoordinates(self, S):
        S = S[1:-1]
        total = len(S)
        if total < 2:
            return []
        res = []
        for i in range(1, total):
            a = S[:i]
            b = S[i:]
            list_a = self.get_add_point_list(a)
            list_b = self.get_add_point_list(b)
            if not list_a or not list_b:
                continue
            for j in list_a:
                for k in list_b:
                    res.append(f'({j}, {k})')
        return res

    def get_add_point_list(self, num):
        res_list = []
        if len(num) < 2:
            res_list.append(num)
            return res_list
        for i in range(len(num)):
            if i == 0:
                tem = num
            else:
                tem = list(num)
                tem.insert(i, '.')
                tem = ''.join(tem)
            check = self.check_num_effective(tem)
            if check:
                res_list.append(tem)
        return res_list

    @staticmethod
    def check_num_effective(num):
        if len(num) < 2:
            return True
        if num[0] == '0':
            if num[1] != '.':
                return False
        if num[-1] == '0':
            if '.' in num:
                return False
        return True


if __name__ == '__main__':
    sl = Solution()
    s = "(123)"
    print(sl.ambiguousCoordinates(s))
