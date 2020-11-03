"""
解题思路:
首先我们要尽可能的多拿到钱，其次我们不能进两个相邻的房间，
所以我们从第一个房间出来后，可以去三或第四个房间。
那么倒推，要么我们进最后一个房间，要么进倒数第二个房间。
进倒数第二个房间，就代表求的是n-1个房间的最大收益
如果进最后一个房间，那么就代表之前我们可以去倒数第三或第四的房间，那就相当于n-2个房间的最大收益加上最后一个房间的收益
那么根据动态规划:
dp(n) = max(dp(n-1), dp(n-2) + nums[n])

看了官方题解发现其实可以采取自底向上的方式，只记下两个最大值，更节约了内存
"""


# 自顶向下备忘录
class Solution:
    def rob(self, nums):
        if not nums:
            return 0
        elif len(nums) < 2:
            return nums[0]
        tem = [nums[0], max(nums[0], nums[1])]
        return self.get_max_money(len(nums) - 1, nums, tem)

    def get_max_money(self, n, nums, tem):
        if n < len(tem):
            return tem[n]
        tem.append(max(self.get_max_money(n-1, nums, tem), self.get_max_money(n-2, nums, tem) + nums[n]))
        return tem[n]
#

# 自底向上
# class Solution:
#     def rob(self, nums):
#         max_first = max_second = 0
#         for i in nums:
#             tem = max_first
#             max_first = max(max_first, max_second + i)
#             max_second = tem
#         return max_first


if __name__ == '__main__':
    sl = Solution()
    print(sl.rob([1, 3, 4, 3]))
