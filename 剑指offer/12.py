"""
解题思路:
这题是回溯法的经典题，回溯法可以看成蛮力法的升级版，它会从解决问题的每一步的所有可能选项系统地选择出一个可行的解决办法。
回溯法非常适合由多个步骤组成的问题，并且每个步骤都有多个选项。回溯法可以用树状结构来表示

首先，我们如果任意选择一点，那么这一点是可以任意上下左右的。
首先设置_index指向word第一位，把第一个点放到stack中
1 从第一个点开始判断，如果这个点=word[_index]，则将_index加1，且使用列表use_points添加当前点左边(x,y)。
2 然后第二个点可以选择第一个点的周围四个点，但要排除边界和已经使用了的点(所以我们需要一个use_points来存储已经使用了的点)
3 添加完后我们要依次判断，所以我们要用stack来存储这四个点的坐标(x,y,_index)，这里存_index是标记这些点是有可能成为第_index个点的点，为什么要这样用呢，后面就解释
4 循环stack，pop出一个需要判断的点(_x,_y,_i)
    - 首先需要判断 _i是否等于_index, 因为假设我们正在找第四个点，发现第三个点周围的点都不行，那么第三个点其实也就不对了，
    这个时候_index就要-1，重新从第二个点周围的其他点找第三个点，而表达出的现象就是stack抛完4级点后抛3级点，而_i就是标记这个点是几级点的。
    当发现抛出点的等级已经和当前要找的点等级不一样了，说明需要回溯到上一级点去了
    - 假如这个点 = word[_index] 说明找对了，判断_index==len(word), 等于说明找完了，return True 否则继续1-4
    - 假如这个点 != word[_index]，就继续步骤4就行了
5 最后循环结束了代表没找到，直接return False

"""
from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n = len(board)
        m = len(board[0])
        w = len(word)

        if w > m * n:
            return False

        for i in range(n):
            for j in range(m):
                stack = [(i, j, 0)]
                _index = 0
                use_points = list()

                while stack:
                    _i, _j, _ind = stack.pop()

                    if use_points and _ind != _index:
                        use_points.pop()
                        _index -= 1
                        stack.append((_i, _j, _ind))
                        continue

                    if board[_i][_j] != word[_index]:
                        continue

                    use_points.append((_i, _j))
                    _index += 1

                    if _index == w:
                        return True

                    # 上方元素
                    if _i > 0 and (_i - 1, _j) not in use_points:
                        stack.append((_i - 1, _j, _index))
                    # 下方元素
                    if _i < n - 1 and (_i + 1, _j) not in use_points:
                        stack.append((_i + 1, _j, _index))
                    # 左方元素
                    if _j > 0 and (_i, _j - 1) not in use_points:
                        stack.append((_i, _j - 1, _index))
                    # 右方元素
                    if _j < m - 1 and (_i, _j + 1) not in use_points:
                        stack.append((_i, _j + 1, _index))

        return False


if __name__ == '__main__':
    board = [["a","b","b","a","b"],["a","a","b","b","a"],["a","a","a","a","b"],["a","a","a","b","a"],["a","a","a","a","a"],["a","b","a","b","b"],["a","b","b","a","b"]]
    word = "abbbbaababaa"
    print(Solution().exist(board, word))

