"""
解题思路:
首先我们需要分析题目，一个平衡字符串就是要所有字符的出现次数一致都为n/4
那么假设字符Q多了1个，其余必定有一个字符少了1个。那么我们就需要找到一个Q，将其替换成缺少的那个字符
那么首先我们遍历一遍字符串，得到所有字符出现的频次，得出哪些需要增加，哪些需要减少。假设出现次数最高的字符为n/4 + 3 次，那么我们的字串最少也是三位
所以我们初始字串长度就为次数最多的字符次数x-n/4
那么我们左指针指向字符串头，右指针指向x-n/4。 字符串可以变成任意字符串，那么每次我们都减去原来的字符数，如果剩下的四个字符出现的次数都小于等于n/4，那肯定就满足
"""


class Solution:
    def balancedString(self, s: str) -> int:
        chr_dict = {'Q': 0, 'W': 0, 'E': 0, 'R': 0}
        for c in s:
            chr_dict[c] += 1

        sub_length = max(chr_dict.values()) - int(len(s)/4)
        if sub_length == 0:
            return 0

        left = 0
        right = sub_length
        while sub_length < len(s):
            sub_chr_dict = {'Q': 0, 'W': 0, 'E': 0, 'R': 0}
            for c in s[left: right]:
                sub_chr_dict[c] += 1
            _left = left
            _right = right
            while _right < len(s):
                flag = True
                for k in chr_dict:
                    if chr_dict[k] - sub_chr_dict.get(k, 0) > int(len(s)/4):
                        flag = False
                if flag:
                    return sub_length
                _left += 1
                _right += 1
                if _right < len(s):
                    sub_chr_dict[s[_left]] -= 1
                    if s[_right] in sub_chr_dict:
                        sub_chr_dict[s[_right]] += 1
                    else:
                        sub_chr_dict[s[_right]] = 1
            right += 1
            sub_length += 1

        return -1


if __name__ == '__main__':
    _s = "WWQQRRRRQRQQ"
    print(Solution().balancedString(_s))