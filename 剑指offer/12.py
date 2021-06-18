"""
解题思路:
这题是回溯法的经典题，回溯法可以看成蛮力法的升级版，它会从解决问题的每一步的所有可能选项系统地选择出一个可行的解决办法。
回溯法非常适合由多个步骤组成的问题，并且每个步骤都有多个选项。回溯法可以用树状结构来表示

首先，我们如果任意选择一点，那么这一点是可以任意上下左右的。
"""
from typing import List


# TODO
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n = len(board)
        m = len(board[0])
        w = len(word)

        if w > m * n:
            return False

        for i in range(n):
            for j in range(m):
                stack = [(i, j)]
                _index = 0
                use_points = list()

                while stack:
                    _i, _j = stack.pop()
                    if board[_i][_j] != word[_index]:
                        if use_points and use_points[-1] == (_i, _j):
                            use_points.pop()
                            _index -= 1
                        continue

                    use_points.append((_i, _j))
                    _index += 1
                    # 上方元素
                    if _i > 0 and (_i - 1, _j) not in use_points:
                        stack.append((_i - 1, _j))
                    # 下方元素
                    if _i < n - 1 and (_i + 1, _j) not in use_points:
                        stack.append((_i + 1, _j))
                    # 左方元素
                    if _j > 0 and (_i, _j - 1) not in use_points:
                        stack.append((_i, _j - 1))
                    # 右方元素
                    if _j < n and (_i, _j + 1) not in use_points:
                        stack.append((_i, _j + 1))



