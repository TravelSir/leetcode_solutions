"""
解题思路:
判断一个括号是否有效的最基础判断就是，在括号的任意一个位置，它前面的符号中左括号的数量必须是大于等于右括号数的。
方法一: 最暴力的方法则是穷举出n个左括号加n个右括号的排列组合，再判断是否有效，总共的排列组合有2^2n，再加上一次判断遍历n次。时间复杂度为O(n*2^2n)
方法二: 基于方法一，在遍历的过程中加入判断，当左括号数等于右括号数时，只能添加左括号，时间复杂度的计算则要基于卡特兰数(俺也不会,超范围)
方法三: 一个左括号一定有一个右括号与之对应。那么一个有效的括号应该是(x)y，x和y都应为有效括号或空。那么问题可以拆分成子问题，这不就是典型的动态规划吗
f(n) = '(' + f(i) + ')' + f(n-i-1), 其中i为 0<=i<n
这题就可以用自底向上的备忘录法去做咯
"""
from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        fn_list = [[''], ['()']]
        for i in range(1, n):
            _fn = list()
            for j in range(i+1):
                left = fn_list[j]
                right = fn_list[i-j] if i-j >= 0 else ['']
                for l in left:
                    for r in right:
                        _fn.append(f'({l}){r}')
            fn_list.append(_fn)
        return fn_list[-1]


if __name__ == '__main__':
    r = Solution().generateParenthesis(5)
    print(r)
