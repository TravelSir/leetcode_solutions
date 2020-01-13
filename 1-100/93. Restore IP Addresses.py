"""
解题思路:
首先我们知道, ip地址的格式是4部分数字组成，每一部分数字范围在0-255之间
那么字符串的长度肯定在4-12之间。每一部分的数字长度是1到3。
我们首先算出所有排列组合，然后再对组成的数字进行大小筛选
当我们进行分组的时候，可以从第一部分取一位开始，但是如果第一部分只取一位，那说明总长度-1肯定要小于等于3*3=9且大于等于3，才能保证有效
第二部分同理，剩下的位数要小于等于6位并且大于等于2位，这样我们就能在长度较长时排除一大部分无效组合
但这其中有个特殊格式，就是像00，000是不能作为有效ip部分的,判断条件就是以0开头且长度大于1就无效
使用递归回溯思想避免写4次循环
"""


class Solution:
    def __init__(self):
        self.res = []

    def restoreIpAddresses(self, s):
        self.get_effective_ip(s, 3, [])
        return self.res

    def get_effective_ip(self, s, limit, ip):
        tem = ip.copy()

        # 结束处理
        if limit == 0:
            if s[0] == '0' and len(s) > 1:
                return
            if int(s) <= 255:
                tem.append(s)
                self.res.append('.'.join(tem))
            return

        lens = len(s)
        for i in range(1, min(4, lens)):
            if s[0] == '0' and len(s[:i]) > 1:
                break
            if lens - i > limit * 3:
                continue
            if lens - i < limit - 1:
                break
            if int(s[:i]) > 255:
                break
            else:
                tem.append(s[:i])
                self.get_effective_ip(s[i:], limit - 1, tem)
                tem.pop()


if __name__ == '__main__':
    sl = Solution()
    print(sl.restoreIpAddresses('0000'))
