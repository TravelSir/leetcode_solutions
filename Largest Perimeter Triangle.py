"""
解题思路:
基本解题法是遍历，但是太耗时间了。
所以我们分析一下三角形的特性: 两边之和大于第三边，其实就是满足两条短边之和大于最长边
而我们需要求数组中能组成的最长周长
其实我们只需要将数组降序排序后，从大到小判断最大三个数是否能组成三角形即可。因为如果最大数 > 后两数之和，那么说明数组再后面的数都不能和这个最大数组成三角形了
这题就是排序 + 判断
"""


class Solution:
    def largestPerimeter(self, A):
        A = sorted(A, reverse=True)
        for i in range(len(A)-2):
            if A[i] < A[i+1] + A[i+2]:
                return A[i] + A[i+1] + A[i+2]
        return 0
