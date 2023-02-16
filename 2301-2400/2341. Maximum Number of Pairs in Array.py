"""
解题思路:
这题很简单，就是以数组第一个数字为准，依次遍历找到第一个相同的数字去除。
第一种最简单的方法就是从第一个数字开始遍历一遍，找到满足条件的剔除，不满足则直接返回。满足再继续遍历新数组。这种方法的时间复杂度为O(n*n)
第二种则是遍历一遍数组，将每个数字的位置信息顺序存储(队列)，再将数字与位置信息存储为一个哈希表。这个时候我们只就可以根据哈希表找到对应数字的位置关系来进行判断，时间复杂度会小很多。

无语了，以上是建立在只能从左开始找，如果没匹配就结束的逻辑分析的。
事实是题意中从0开始只是个废话。
那这题就遍历依次，用一个哈希表来记录数字是否存在。当存在的数字每次变为偶数时，数对+1
"""
from typing import List


class Solution:
    # def numberOfPairs(self, nums: List[int]) -> List[int]:
    #     num_dict = dict()
    #     for i, n in enumerate(nums):
    #         if n in num_dict:
    #             num_dict[n].append(i)
    #         else:
    #             num_dict[n] = [i]
    #
    #     used_index_dict = dict()
    #     _index = 0
    #     while _index < len(nums):
    #         _num = nums[_index]
    #         if used_index_dict.get(_index):
    #             _index += 1
    #             continue
    #         _num_list = num_dict.get(_num) or []
    #         if len(_num_list) < 2:
    #             break
    #         num_dict[_num] = _num_list[2:]
    #         used_index_dict[_num_list[0]] = 1
    #         used_index_dict[_num_list[1]] = 1
    #         _index += 1
    #
    #     return [len(used_index_dict) // 2, len(nums) - len(used_index_dict)]

    def numberOfPairs(self, nums: List[int]) -> List[int]:
        count_dict = dict()
        ret = 0
        for n in nums:
            if n in count_dict:
                count_dict[n] += 1
            else:
                count_dict[n] = 1
            if count_dict[n] % 2 == 0:
                ret += 1
        return [ret, len(nums) - ret * 2]


if __name__ == '__main__':
    print(Solution().numberOfPairs([1,0,0]))