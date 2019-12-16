"""
解题思路:
找朋友的题是典型的并查集算法, 我们可以用一个字数组来记录学生与对应根学生的对应关系，
当遍历完后确定了关系，再判断数组内有多少学生对应的根学生是自己就是朋友圈总数了
"""


class Solution:
    def findCircleNum(self, M):
        lens = len(M)
        relations = [i for i in range(lens)]
        for i in range(lens):
            for j in range(lens):
                if i == j:
                    continue
                if M[i][j] == 1:
                    i_parent = self.find_parent(i, relations)
                    j_parent = self.find_parent(j, relations)
                    if i_parent != j_parent:
                        # 合并合集并压缩路径
                        relations[i] = i_parent
                        relations[j] = i_parent
                        relations[j_parent] = i_parent
        # 统计朋友圈
        _sum = 0
        for i, v in enumerate(relations):
            if i == v:
                _sum += 1
        return _sum

    # 寻找根节点
    @staticmethod
    def find_parent(index, relations):
        parent = relations[index]
        while parent != index:
            index = parent
            parent = relations[index]
        return parent


if __name__ == '__main__':
    m = [[1,1],
         [1,1]]
    print(Solution().findCircleNum(m))
