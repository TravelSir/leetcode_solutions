"""
解题思路：
这题使用并查集的方法来做, 这里我们可以用字典来记录每个节点和对应的父节点。
在并查集中最重要的优化就是要进行路径优化, 而我们为来要求出最长连续序列，那么我们如果把所有结果统计出来后再统计会多消耗时间
所以我们再求最长连续序列的时候，可以在路径优化步骤时计算，那这样我们还需要一个字典来记录父节点对应的集合的长度
而在找两个数的关系时，不可避免的要使用两层循环，但这样就无法满足时间复杂度为O(n)，所以我们再来看一些题目条件，连续序列
例如数2，我们只需要判断数1和数3是否存在即可，不用跟所有数比较。
"""


class Solution:
    def __init__(self):
        self.max = 1

    def longestConsecutive(self, nums):
        lens = len(nums)
        if lens < 2:
            return lens
        # 为保证一次循环，所以我们这采用三个字典，分别存储节点下标与父节点下表， 节点的值与它对应的下标， 父节点对应的最长长度
        dic, num_dic, len_dic = dict(), dict(), dict()
        for i in range(lens):
            # 因为要保证时间复杂度O(n)，所以放到一次循环内来初始化字典
            if nums[i] in num_dic:
                continue
            dic[i] = i
            len_dic[i] = 1
            num_dic[nums[i]] = i

            # 判断之前是否存在与自己连续的数
            if num_dic.get(nums[i]-1) is not None:
                parent = self.find_parent(num_dic.get(nums[i]-1), dic)
                len_dic[parent] += len_dic[i]
                len_dic[i] = len_dic[parent]
                if self.max < len_dic[parent]:
                    self.max = len_dic[parent]
                dic[i] = dic[parent]

            if num_dic.get(nums[i]+1) is not None:
                parent = self.find_parent(num_dic.get(nums[i]+1), dic)
                len_dic[parent] += len_dic[i]
                if self.max < len_dic[parent]:
                    self.max = len_dic[parent]

                # 判断是否已经和i-1相连，相连则把之前的父节点整合过来
                front = self.find_parent(i, dic)
                if i != front:
                    dic[front] = dic[parent]

                dic[i] = dic[parent]

        return self.max

    def find_parent(self, i, dic):
        while i != dic[i]:
            i = dic[i]
        return i


if __name__ == '__main__':
    nums = [1, 2, 0, 1]
    print(Solution().longestConsecutive(nums))
