"""
解题思路
一种是新分配内存来做，一种是原地转换。
因为在python中字符串是不变的常量，所以需转换成数组来做(模拟C++字符串原地)
原地转换的思路是:
因为空格转%20，每一次转换需多占用2个长度的内存。
所以在保证原字符串后有可分配的连续内存时，可以通过扩展字符串长度后再替换空格达到原地转换的效果，目的是节约内存

在原地转换基础上，当我们转换一次空格时，%替换空格位置，20需一次替换空格后两个字符，所以需将后面的字符依次后移，但这样的时间复杂度在最坏情况下需要O(n*n)
所以我们可以先确定替换后的字符串总长度，从后往前替换，这样能保证每次替换不影响未替换的字符。用双指针一个指向原字符串末尾，另外一个指向扩充后的字符串末尾
"""


class Solution:
    def replaceSpace(self, s: str) -> str:
        s_list = list(s)
        # 计算有多少空格
        n = 0
        for i in s_list:
            if i == " ":
                n += 1

        if not n:
            return s

        # 扩展数组,extend函数在内存够的情况下是原地扩展，可通过id函数查看extend前后数组内存地址一样
        s_list.extend([""] * (2 * n))

        left = len(s) - 1
        right = len(s_list) - 1

        for i in range(left, -1, -1):
            if s_list[i] == " ":
                s_list[right] = '0'
                right -= 1
                s_list[right] = '2'
                right -= 1
                s_list[right] = '%'
            else:
                s_list[right] = s_list[i]
            right -= 1

        return ''.join(s_list)


if __name__ == '__main__':
    print(Solution().replaceSpace('     '))
