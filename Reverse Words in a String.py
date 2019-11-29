"""
解题思路:
python一行代码，分隔加切片
return " ".join(s.split()[::-1])
不用split的话，就是遍历一次，遇到字母先用临时列表存下来，然后遇到空格，将临时列表的单词丢入最终列表，也很简单
"""


class Solution:
    def reverseWords(self, s: str) -> str:

        # return " ".join(s.split()[::-1])

        tem = []
        res = []
        for c in s:
            if c == ' ':
                if tem:
                    res.append(''.join(tem))
                    tem = []
            else:
                tem.append(c)
        if tem:
            res.append(''.join(tem))
        print(res)
        return ' '.join(res[::-1])


if __name__ == '__main__':
    sl = Solution()
    print(sl.reverseWords("the sky is  blue"))
