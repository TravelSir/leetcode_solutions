"""
求最大和，其实就是要尽可能的多加正数
例如：-2,1,-3,4,-1,2
这里我们使用动态规划的思想，将前面算出的和存起来成tem，开始设定tem为第一个数
tem为负数, 所以我们在加第二个数的时候结果肯定会比第二个数小，所以我们这个时候tem就应该是第二个数
当tem加第三个数时，因为tem是正数，所以加上第三个数结果肯定会比第三个数大，所以tem += 第三个数
以此类推，然后我们在每一次算出tem的时候与max比较就能求出最大的子序和了。这种算法时间复杂度为O(n)

题目的进阶是使用分治法来做，分治法就是将问题拆分为子问题，那么当我们将数组拆分为a,b数组后,最大子序和肯定是在 a的最大子序和，b的最大子序和，
a,b中间连通的最大子序和这三者之间。那么a,b中间连通的最大子序和怎么求呢。其实a,b中间连通的最大子序和就等于a从末尾向前开始的最大子序的和 加上b从开头向后的最大子序和
"""


# 动态规划
class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        max = tem = nums[0]
        for i in range(1, len(nums)):
            if tem <= 0:
                tem = nums[i]
            else:
                tem += nums[i]
            if max < tem:
                max = tem
        return max


# # 分治法
# class Solution:
#     def maxSubArray(self, nums: list[int]) -> int:
#         lens = len(nums)
#         if lens == 1:
#             return nums[0]
#         else:
#             border = lens // 2
#             left = nums[0: border]
#             right = nums[border: lens]
#
#             left_max = self.maxSubArray(left)
#             right_max = self.maxSubArray(right)
#             middle_max = self.get_max_sum(left[::-1]) + self.get_max_sum(right)
#
#             return max(left_max, right_max, middle_max)
#
#     def get_max_sum(self, nums):
#         max_sum = tem = nums[0]
#         for i in nums[1:]:
#             tem += i
#             max_sum = max(tem, max_sum)
#         return max_sum


