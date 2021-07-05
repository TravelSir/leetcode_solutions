"""
解题思路:
字符ascii码范围是在128以内的，所以用128大小的数组桶来统计频率是最快的。在遍历过程中记录最大频率
然后再用一个长度为最大频率的桶来按照频率存储出现的字符。最后再倒序输出字符
"""


class Solution:
    def frequencySort(self, s: str) -> str:
        str_bucket = [0] * 128
        _max = 0
        for c in s:
            str_bucket[ord(c)-1] += 1
            _max = max(_max, str_bucket[ord(c)-1])

        times_bucket = [list() for i in range(_max)]

        for i, t in enumerate(str_bucket):
            if t > 0:
                times_bucket[t-1].append(chr(i+1))

        res = ""
        for i in range(_max, 0, -1):
            for c in times_bucket[i-1]:
                res += c * i
        return res


if __name__ == '__main__':
    print(Solution().frequencySort(""))

