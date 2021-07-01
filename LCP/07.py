"""
解题思路:
每个玩家之间的关系是多对多的图关系。
从0开始，到n-1结束。需要遍历所有从0开始，步长为k的路径，判断最后落点是否为n-1
则首先需要根据二维数组归纳出每个玩家能传递给谁，同样用一个数组记录，下标为玩家下标
"""
from typing import List


class Solution:
    def numWays(self, n: int, relation: List[List[int]], k: int) -> int:
        player = [list() for i in range(n)]
        for r in relation:
            player[r[0]].append(r[1])

        path = [0]
        for i in range(k):
            tem = []
            for p in path:
                tem.extend(player[p])
            path = tem
        return path.count(n-1)


if __name__ == '__main__':
    n = 5
    rel = [[0, 2], [2, 1], [3, 4], [2, 3], [1, 4], [2, 0], [0, 4]]
    k = 3
    print(Solution().numWays(n, rel, k))

