"""
解题思路:
很简单的一道题，找出最长的递增序列，遍历一次，用临时变量比较大小，记录最大长度就好了
"""


class Solution:
    def findLengthOfLCIS(self, nums):
        _max = 0
        if not nums:
            return _max
        tem = nums[0]
        _sum = 1
        for i in nums[1:]:
            if tem < i:
                _sum += 1
            else:
                if _sum > _max:
                    _max = _sum
                _sum = 1
            tem = i
        if _sum > _max:
            _max = _sum
        return _max


if __name__ == '__main__':
    print(Solution().findLengthOfLCIS([2,2,2,2,2]))
