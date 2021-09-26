"""
解题思路:
斐波那契数列的变种，整体思路一样，也是使用动态规划，自底向上的备忘录法做, 这里的备忘录就需要存储3个值
"""


class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        if n < 3:
            return 1

        note = [0, 1, 1]
        for i in range(3, n+1):
            tem = sum(note)
            note.pop(0)
            note.append(tem)
        return note[-1]
