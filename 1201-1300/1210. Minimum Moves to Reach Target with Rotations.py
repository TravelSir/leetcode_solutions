"""
解题思路:
首先这题的巨坑: 这货根本不是贪吃蛇，是个螃蟹。当不旋转时，蛇头和蛇尾会整体移动，如水平时，蛇头向上，蛇尾不是停留在蛇头的位置，而是跟着水平向上。。。
然后第二坑: 只能往右或下走。。。
经典的最短路径题，那基本上就是BFS了。下面具体分析
首先我们来分析蛇的体积是占用两个格子，若蛇为水平状态，蛇头上下移动则蛇尾页上下移动。若水平移动则蛇尾移动至上次蛇头位置。 垂直状态同理
那么我们再来分析蛇头下次能移动的位置为，上下左右 + 蛇尾左右(竖直状态) + 蛇尾上下(水平状态)，其中需要排除的情况是蛇头不能移动到蛇尾的位置，可移动格子要为0
那么在每次遍历或回溯的时候，我们需要知道的信息为，当前蛇头蛇尾的位置，以及已移动的次数。
这里我们将信息以字典的方式存储，并以队列的形式进行BFS
"""
from typing import List


class Solution:
    def minimumMoves(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        target_nodes = [(n - 1, m - 2), (n - 1, m - 1)]
        queue = list()
        init_snake = {
            'head': (0, 1),
            'tail': (0, 0),
            'move': 0,
        }
        node_records = set()
        queue.append(init_snake)
        while queue:
            _node = queue.pop(0)
            node_records.add((_node['head'], _node['tail']))
            if _node['tail'] == target_nodes[0] and _node['head'] == target_nodes[1]:
                return _node["move"]
            move_nodes = self.get_can_move_node(_node, grid, node_records)
            node_records = node_records.union(set(move_nodes))
            for n in move_nodes:
                _item = {
                    'head': n[0],
                    'tail': n[1],
                    'move': _node['move'] + 1,
                }
                queue.append(_item)
        return -1

    def get_can_move_node(self, node, grid, grids):
        node_head = node.get('head')
        node_tail = node.get('tail')
        move_nodes = []
        direction = self.judge_node_direction(node_head, node_tail)
        # # 上节点
        # _head = (node_head[0] - 1, node_head[1])
        # if direction == 'horizontal':
        #     _tail = (node_tail[0] - 1, node_tail[1])
        # else:
        #     _tail = node_head
        # if _head[0] >= 0 and grid[_head[0]][_head[1]] == 0 and _head != node_tail and grid[_tail[0]][
        #     _tail[1]] == 0 and (_head, _tail) not in grids:
        #     move_nodes.append((_head, _tail))

        # 下节点
        _head = (node_head[0] + 1, node_head[1])
        if direction == 'horizontal':
            _tail = (node_tail[0] + 1, node_tail[1])
        else:
            _tail = node_head
        if _head[0] < len(grid) and grid[_head[0]][_head[1]] == 0 and _head != node_tail and grid[_tail[0]][
            _tail[1]] == 0 and (_head, _tail) not in grids:
            move_nodes.append((_head, _tail))

        # # 左节点
        # _head = (node_head[0], node_head[1] - 1)
        # if direction == 'vertical':
        #     _tail = (node_tail[0], node_tail[1] - 1)
        # else:
        #     _tail = node_head
        # if _head[1] > 0 and grid[_head[0]][_head[1]] == 0 and _head != node_tail and grid[_tail[0]][_tail[1]] == 0 and (
        #         _head, _tail) not in grids:
        #     move_nodes.append((_head, _tail))

        # 右节点
        _head = (node_head[0], node_head[1] + 1)
        if direction == 'vertical':
            _tail = (node_tail[0], node_tail[1] + 1)
        else:
            _tail = node_head
        if _head[1] < len(grid[0]) and grid[_head[0]][_head[1]] == 0 and _head != node_tail and grid[_tail[0]][
            _tail[1]] == 0 and (_head, _tail) not in grids:
            move_nodes.append((_head, _tail))

        if direction == 'horizontal':
            # 水平方向
            # # 上节点
            # x = node_tail[0] - 1
            # y = node_tail[1]
            # if x >= 0 and grid[x][y] == 0 and (_head, _tail) not in grids:
            #     move_nodes.append(((x, y), node_tail))

            # 下节点
            x = node_tail[0] + 1
            y = node_tail[1]
            if x < len(grid) and grid[x][y] == 0 and grid[x][y + 1] == 0 and ((x, y), node_tail) not in grids:
                move_nodes.append(((x, y), node_tail))
        else:
            # 垂直方向
            # # 左节点
            # x = node_tail[0]
            # y = node_tail[1] - 1
            # if y >= 0 and grid[x][y] == 0 and (_head, _tail) not in grids:
            #     move_nodes.append(((x, y), node_tail))

            # 右节点
            x = node_tail[0]
            y = node_tail[1] + 1
            if y < len(grid[x]) and grid[x][y] == 0 and grid[x+1][y] == 0 and ((x, y), node_tail) not in grids:
                move_nodes.append(((x, y), node_tail))

        return move_nodes

    @staticmethod
    def judge_node_direction(head, tail):
        if head[0] == tail[0]:
            return 'horizontal'
        else:
            return 'vertical'


if __name__ == '__main__':
    grids = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
             [0, 1, 0, 0, 0, 0, 0, 1, 0, 1],
             [1, 0, 0, 1, 0, 0, 1, 0, 1, 0],
             [0, 0, 0, 1, 0, 1, 0, 1, 0, 0],
             [0, 0, 0, 0, 1, 0, 0, 0, 0, 1],
             [0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
             [1, 0, 0, 1, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [1, 1, 0, 0, 0, 0, 0, 0, 0, 0]]
print(Solution().minimumMoves(grids))
