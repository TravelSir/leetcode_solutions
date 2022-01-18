"""
解题思路:
最直接的思路是多层循环遍历。时间复杂度约为O(3^n),n为数字长度
我们仔细分析，对于数字2对应的a，b，c来说，他们之后的字母组合都肯定是完全相同的，不同的只是abc
所以我们可以从最后一位开始列出组合，每前进一位，都会将之前的组合全部复制一遍
"""
from typing import List


Digit_Dict = {
    '2': ['a', 'b', 'c'],
    '3': ['d', 'e', 'f'],
    '4': ['g', 'h', 'i'],
    '5': ['j', 'k', 'l'],
    '6': ['m', 'n', 'o'],
    '7': ['p', 'q', 'r', 's'],
    '8': ['t', 'u', 'v'],
    '9': ['w', 'x', 'y', 'z'],
}


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        res = ['']
        for i in range(len(digits)-1, -1, -1):
            char_list = Digit_Dict[digits[i]]
            tem = []
            for c in char_list:
                for r in res:
                    tem.append(c+r)
            res = tem

        return res


if __name__ == '__main__':
    print(Solution().letterCombinations("2"))
