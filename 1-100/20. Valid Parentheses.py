"""
解题思路:
首先一个有效括号肯定是有一个左括号和一个右括号，且左括号在右括号左边
但假如在一对括号里包含了其他的括号，那为了保证有效，那肯定这对括号里的括号也肯定满足要求。
那么其实从小我们的数字基础就告诉我们，括号是按就近原则的。
那么转换到这道题里
我们可以用栈的方式，每一个左括号都入栈，当有右括号时，判断栈是否为空或栈末元素是否与右括号为同一类型括号，栈为空或不满足同一类型则一定为无效字符串，满足即可出栈继续判断
最后再判断一下栈是否为空，不为空则还有左括号未找到对应右括号，也无效
这里我们把括号转化为数字，方便判断，左括号都大于0，右括号都小于0。相同类型的左右括号之和为0
"""


class Solution:
    def isValid(self, s):
        brackets = {
            '(': 1,
            ')': -1,
            '{': 2,
            '}': -2,
            '[': 3,
            ']': -3
        }
        stack = []
        for i in s:
            if brackets[i] > 0:
                stack.append(brackets[i])
            elif not stack:
                return False
            elif stack[-1] + brackets[i] == 0:
                stack.pop()
            else:
                return False
        if stack:
            return False
        return True
