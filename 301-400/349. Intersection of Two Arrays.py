"""
解题思路:
最基础的解法就是，双重循环遍历比较两个数组的所有元素，这种方法的时间复杂度是O(m*n),太耗时了
再看题干，我们要保证输出结果每个元素是唯一的且不考虑顺序，那么用空间换时间，我们就可以用到哈希表
遍历一个数组建立一个哈希表，遍历另一个数组去哈希表中查询，时间复杂度其实就变成了O(m+n)
补充: 不探究算法，实际应用中直接return list(set(nums1) & set(nums2))即可
"""


class Solution:
    def intersection(self, nums1, nums2):
        num_dict = dict()
        for i in nums1:
            num_dict[i] = True
        res = list()
        for j in nums2:
            if num_dict.get(j):
                res.append(j)
                num_dict[j] = False
        return res

