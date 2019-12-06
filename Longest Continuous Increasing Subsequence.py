"""
解题思路:
很简单的一道题，找出最长的递增序列，遍历一次，用一个临时变量初始等于第一位，初始长度为1。然后依次从第二位开始比较大小，
若大于第二位则长度加1，若小于，则判断这段递增序列的长度与最大值的大小，然后长度重新变为1，临时变量每次循环末尾变成当前元素。别忘了最后比较一次长度
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
