"""
解题思路:
首尾为1，中间的数为上一行的两个数之和。
"""
from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ret = []
        for n in range(numRows):
            if n == 0:
                ret.append([1])
            elif n == 1:
                ret.append([1, 1])
            else:
                row = [1] * (n + 1)
                for i in range(1, n):
                    row[i] = ret[n - 1][i - 1] + ret[n - 1][i]
                ret.append(row)
        return ret
